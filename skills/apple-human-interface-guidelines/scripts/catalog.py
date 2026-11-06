#!/usr/bin/env python3
"""Refresh a HIG metadata catalog or validate its checked-in Markdown references.

Apple's article bodies and image bytes are never written to the repository.
Requires Python 3.11+ and curl; requests use the operating system's TLS trust.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urljoin, urlsplit

ORIGIN = "https://developer.apple.com"
ASSET_BASE = "https://developer.apple.com/tutorials/"
ROOT_PATH = "/design/human-interface-guidelines"
SKILL_DIR = Path(__file__).resolve().parents[1]
REFERENCE_DIR = SKILL_DIR / "references"
CATALOG_PATH = REFERENCE_DIR / "catalog.json"
GROUPS = (
    "getting-started",
    "foundations",
    "patterns",
    "components",
    "inputs",
    "technologies",
)


def hig_path(value: str) -> str | None:
    """Canonicalize only HIG paths; never follow external hosts or fragments."""
    parsed = urlsplit(value)
    if parsed.netloc and parsed.netloc != "developer.apple.com":
        return None
    path = parsed.path.rstrip("/").lower()
    if path == ROOT_PATH or path.startswith(ROOT_PATH + "/"):
        return path
    return None


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def fetch_page(path: str) -> dict:
    url = f"{ORIGIN}/tutorials/data{path}.json"
    result = subprocess.run(
        [
            "curl",
            "--fail",
            "--silent",
            "--show-error",
            "--location",
            "--proto",
            "=https",
            "--proto-redir",
            "=https",
            "--connect-timeout",
            "15",
            "--max-time",
            "60",
            url,
        ],
        check=True,
        capture_output=True,
    )
    return parse_page(path, result.stdout)


def parse_page(path: str, raw: bytes) -> dict:
    """Extract navigation metadata from a verified DocC response shape."""
    url = f"{ORIGIN}/tutorials/data{path}.json"
    page = json.loads(raw)
    require(isinstance(page, dict), f"{url}: expected an object")
    require(
        page.get("schemaVersion", {}).get("major") == 0,
        f"{url}: unsupported DocC schema",
    )
    metadata = page.get("metadata")
    require(
        isinstance(metadata, dict) and isinstance(metadata.get("title"), str),
        f"{url}: missing title",
    )
    refs = page.get("references")
    require(isinstance(refs, dict), f"{url}: missing references")
    require(
        isinstance(page.get("primaryContentSections"), list),
        f"{url}: missing article content",
    )
    topics = []
    for ref in refs.values():
        require(isinstance(ref, dict), f"{url}: invalid reference")
        if ref.get("type") == "topic":
            require(isinstance(ref.get("url"), str), f"{url}: topic has no URL")
            target = hig_path(ref["url"])
            if target:
                topics.append(target)
    children = []
    for section in page.get("topicSections", []):
        for identifier in section["identifiers"]:
            require(identifier in refs, f"{url}: unresolved child {identifier}")
            target = hig_path(refs[identifier]["url"])
            if target:
                children.append(target)
    headings = []
    images = []
    seen_images = set()
    body_images = {}
    for node in walk(page["primaryContentSections"]):
        if node.get("type") == "heading":
            require(isinstance(node.get("text"), str), f"{url}: invalid heading")
            headings.append(node["text"])
        if node.get("type") == "image":
            identifier = node.get("identifier")
            require(
                identifier in refs and refs[identifier].get("type") == "image",
                f"{url}: unresolved body image {identifier}",
            )
            body_images.setdefault(identifier, len(body_images))
    for identifier, ref in sorted(
        refs.items(), key=lambda item: body_images.get(item[0], len(body_images))
    ):
        if ref.get("type") != "image":
            continue
        require(
            isinstance(ref.get("variants"), list) and ref["variants"],
            f"{url}: image has no variants",
        )
        for variant in ref["variants"]:
            require(isinstance(variant.get("url"), str), f"{url}: image has no URL")
            source_url = variant["url"]
            if urlsplit(source_url).scheme:
                image_url = source_url
            else:
                # DocC mounts its /images reference namespace under /tutorials/.
                # This is verified against Apple's HTML base and actual GETs.
                require(
                    source_url.startswith("/images/"),
                    f"{url}: unsupported relative image URL: {source_url}",
                )
                image_url = urljoin(ASSET_BASE, source_url.removeprefix("/"))
            parsed = urlsplit(image_url)
            require(
                parsed.scheme == "https"
                and parsed.hostname
                in {
                    "developer.apple.com",
                    "docs-assets.developer.apple.com",
                    "devimages-cdn.apple.com",
                },
                f"{url}: unexpected image host: {image_url}",
            )
            if image_url not in seen_images:
                traits = variant.get("traits", [])
                require(
                    isinstance(traits, list)
                    and all(isinstance(t, str) for t in traits),
                    f"{url}: invalid image traits",
                )
                images.append(
                    {
                        "url": image_url,
                        "traits": traits,
                        "in_article": identifier in body_images,
                    }
                )
                seen_images.add(image_url)
    return {
        "slug": path.rsplit("/", 1)[-1],
        "title": metadata["title"],
        "url": ORIGIN + path,
        "markdown_url": ORIGIN + path + ".md",
        "data_url": url,
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "children": sorted(set(children)),
        "related": sorted(set(topics)),
        "headings": list(dict.fromkeys(headings)),
        "images": images,
    }


def discover() -> dict:
    pages = {}
    pending = {ROOT_PATH}
    with ThreadPoolExecutor(max_workers=4) as pool:
        while pending:
            batch = sorted(pending)
            pending = set()
            # All downloads and schema checks finish before any repository write.
            for path, page in zip(batch, pool.map(fetch_page, batch), strict=True):
                pages[path] = page
                pending.update(p for p in page["related"] if p not in pages)
            pending.difference_update(pages)
            print(f"Read {len(pages)} topics; {len(pending)} remaining", flush=True)
    for group in GROUPS:
        require(f"{ROOT_PATH}/{group}" in pages, f"Missing HIG category: {group}")
    return {
        "schema_version": 1,
        "retrieved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": ORIGIN + ROOT_PATH,
        "scope": "All HIG pages reachable through topic references from the root; English only.",
        "pages": [pages[path] for path in sorted(pages)],
    }


def md_text(value: str) -> str:
    return re.sub(r"([\\`*_[\]<>|])", r"\\\1", value).replace("\n", " ")


def render(catalog: dict) -> dict[str, str]:
    pages = {urlsplit(p["url"]).path: p for p in catalog["pages"]}
    notes = json.loads((REFERENCE_DIR / "notes.json").read_text())
    unknown = set(notes) - {p["slug"] for p in pages.values()}
    require(not unknown, f"Notes reference missing topics: {sorted(unknown)}")
    files = {}
    lines = [
        "# Apple HIG topic catalog",
        "",
        f"Metadata retrieved: {catalog['retrieved_at']}.",
        "",
        f"Coverage: {len(pages)} pages. {catalog['scope']}",
        "",
        "This catalog contains original notes and source navigation, not Apple's complete text.",
        "Image links load Apple-hosted files and require a network connection.",
        "See [research and provenance](research.md) for download findings and reuse limits.",
        "",
    ]
    categorized = set()
    for group in GROUPS:
        path = f"{ROOT_PATH}/{group}"
        page = pages[path]
        lines += [f"## {md_text(page['title'])}", ""]
        queue = [(path, 0)]
        visited = set()
        while queue:
            current, depth = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            categorized.add(current)
            topic = pages[current]
            lines.append(
                f"{'  ' * depth}- [{md_text(topic['title'])}](topics/{topic['slug']}.md)"
            )
            queue[0:0] = [(child, depth + 1) for child in topic["children"]]
        lines.append("")
    lines += ["## Additional linked topics", ""]
    for path in sorted(set(pages) - categorized):
        page = pages[path]
        lines.append(f"- [{md_text(page['title'])}](topics/{page['slug']}.md)")
    lines.append("")
    files["catalog.md"] = "\n".join(lines)
    for page in pages.values():
        slug = page["slug"]
        lines = [
            f"# {md_text(page['title'])}",
            "",
            f"[Apple HIG]({page['url']}) · [Official full Markdown]({page['markdown_url']})",
            "",
            "[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)",
            "",
        ]
        if slug in notes:
            lines += [
                "## Design notes",
                "",
                "Original application notes; consult Apple for the full guidance.",
                "",
            ]
            lines += [f"- {note}" for note in notes[slug]]
            lines.append("")
        else:
            lines += [
                "This page is indexed for discovery. Read the official full Markdown for its guidance.",
                "",
            ]
        if page["headings"]:
            lines += ["## Source section outline", ""]
            lines += [f"- {md_text(heading)}" for heading in page["headings"]]
            lines.append("")
        if page["children"]:
            lines += ["## Topics", ""]
            lines += [
                f"- [{md_text(pages[p]['title'])}]({pages[p]['slug']}.md)"
                for p in page["children"]
            ]
            lines.append("")
        if page["images"]:
            lines += [
                "## Image references",
                "",
                "Apple-hosted images; copyright Apple. Variants are labeled with source traits.",
                "",
            ]
            preview = next(
                (
                    i
                    for i in page["images"]
                    if i["in_article"] and "dark" not in i["traits"]
                ),
                None,
            )
            if preview:
                lines += [f"![Apple article illustration]({preview['url']})", ""]
            lines += [
                "<details>",
                f"<summary>All {len(page['images'])} image references and variants</summary>",
                "",
            ]
            for index, item in enumerate(page["images"], 1):
                traits = ", ".join(item["traits"]) or "default"
                usage = "article" if item["in_article"] else "related or metadata"
                label = md_text(f"Apple image {index} ({usage}; {traits})")
                lines += [f"![{label}]({item['url']})", ""]
            lines += ["</details>", ""]
        else:
            lines += ["No image references were supplied in this page's JSON.", ""]
        files[f"topics/{slug}.md"] = "\n".join(lines)
    return files


def check(catalog: dict) -> None:
    require(catalog.get("schema_version") == 1, "Unsupported catalog schema")
    pages = catalog["pages"]
    slugs = [page["slug"] for page in pages]
    require(len(slugs) == len(set(slugs)), "Duplicate topic slugs")
    paths = {urlsplit(page["url"]).path for page in pages}
    for page in pages:
        require(hig_path(page["url"]) in paths, "Invalid HIG source URL")
        require(
            set(page["children"] + page["related"]) <= paths,
            f"{page['slug']}: unresolved HIG links",
        )
    expected = render(catalog)
    actual = {f"topics/{p.name}" for p in (REFERENCE_DIR / "topics").glob("*.md")}
    require(
        actual == {name for name in expected if name.startswith("topics/")},
        "Topic Markdown file set differs from catalog",
    )
    for name in expected:
        text = (REFERENCE_DIR / name).read_text()
        require(
            text == expected[name],
            f"Stale generated reference: {name}",
        )
    print(
        f"Valid: {len(pages)} topics, {sum(len(p['images']) for p in pages)} image references"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("refresh", "check"))
    args = parser.parse_args()
    if args.command == "refresh":
        catalog = discover()
        files = render(catalog)
        old_slugs = {p.stem for p in (REFERENCE_DIR / "topics").glob("*.md")}
        new_slugs = {p["slug"] for p in catalog["pages"]}
        require(
            not old_slugs - new_slugs,
            f"Upstream removed topics; review before deleting: {sorted(old_slugs - new_slugs)}",
        )
        (REFERENCE_DIR / "topics").mkdir(parents=True, exist_ok=True)
        CATALOG_PATH.write_text(
            json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
        )
        for name, content in files.items():
            (REFERENCE_DIR / name).write_text(content)
        print("Run make format-hig, then make check-hig.")
    else:
        check(json.loads(CATALOG_PATH.read_text()))


if __name__ == "__main__":
    try:
        main()
    except (
        ValueError,
        KeyError,
        TypeError,
        OSError,
        subprocess.CalledProcessError,
    ) as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
