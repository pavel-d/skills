"""Behavioral tests using metadata-only extracts of real Apple responses."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import subprocess
from unittest import TestCase, main
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "catalog.py"
SPEC = importlib.util.spec_from_file_location("hig_catalog", SCRIPT)
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)
FIXTURES = Path(__file__).parent / "fixtures"


def fixture(name):
    return json.loads((FIXTURES / f"{name}.json").read_text())


def parse(name, source=None):
    source = fixture(name) if source is None else source
    return catalog.parse_page(
        f"{catalog.ROOT_PATH}/{name}", json.dumps(source).encode()
    )


class SourceParsingTests(TestCase):
    def test_verified_foundation_children_are_resolved(self):
        result = parse("foundations")
        self.assertEqual(result["title"], "Foundations")
        self.assertEqual(
            result["children"],
            [
                f"{catalog.ROOT_PATH}/accessibility",
                f"{catalog.ROOT_PATH}/app-icons",
            ],
        )
        self.assertEqual(
            result["markdown_url"],
            f"{catalog.ORIGIN}{catalog.ROOT_PATH}/foundations.md",
        )

    def test_real_image_variants_keep_appearance_and_resolve_from_origin(self):
        result = parse("buttons")
        self.assertTrue(result["images"])
        self.assertTrue(
            result["images"][0]["url"].endswith("components-buttons-intro@2x.png")
        )
        for item in result["images"]:
            self.assertTrue(item["url"].startswith(f"{catalog.ASSET_BASE}images/"))
            self.assertTrue(item["in_article"])
        self.assertIn(
            "light", {trait for i in result["images"] for trait in i["traits"]}
        )
        self.assertIn(
            "dark", {trait for i in result["images"] for trait in i["traits"]}
        )

    def test_external_links_are_not_crawled(self):
        source = fixture("foundations")
        source["references"]["outside"] = {
            "type": "topic",
            "url": "https://example.com/design/human-interface-guidelines/fake",
        }
        self.assertNotIn(
            "/design/human-interface-guidelines/fake",
            parse("foundations", source)["related"],
        )

    def test_missing_required_metadata_and_unresolved_children_fail(self):
        for change in (
            lambda p: p.pop("metadata"),
            lambda p: p["references"].clear(),
            lambda p: p.update(schemaVersion={"major": 99}),
        ):
            with self.subTest(change=change):
                source = fixture("foundations")
                change(source)
                with self.assertRaises(ValueError):
                    parse("foundations", source)

    def test_missing_image_variants_and_untrusted_hosts_fail(self):
        source = fixture("buttons")
        identifier = "components-buttons-intro.png"
        source["references"][identifier]["variants"] = []
        with self.assertRaises(ValueError):
            parse("buttons", source)
        source = fixture("buttons")
        source["references"][identifier]["variants"][0]["url"] = (
            "https://example.com/image.png"
        )
        with self.assertRaises(ValueError):
            parse("buttons", source)

    def test_invalid_json_and_download_errors_are_explicit(self):
        with self.assertRaises(json.JSONDecodeError):
            catalog.parse_page(catalog.ROOT_PATH, b"not JSON")
        with patch.object(
            catalog.subprocess,
            "run",
            side_effect=subprocess.CalledProcessError(22, "curl"),
        ):
            with self.assertRaises(subprocess.CalledProcessError):
                catalog.fetch_page(catalog.ROOT_PATH)


class DiscoveryTests(TestCase):
    def test_related_topics_and_cycles_are_discovered_once(self):
        root = catalog.ROOT_PATH
        group_paths = [f"{root}/{group}" for group in catalog.GROUPS]
        leaf = f"{root}/buttons"
        visited = []

        def fetch(path):
            visited.append(path)
            source = parse("buttons")
            source.update(
                slug=path.rsplit("/", 1)[-1],
                url=catalog.ORIGIN + path,
                related=group_paths if path == root else [root, leaf],
            )
            return deepcopy(source)

        with patch.object(catalog, "fetch_page", side_effect=fetch):
            result = catalog.discover()
        self.assertEqual(
            {p["url"] for p in result["pages"]},
            {catalog.ORIGIN + p for p in [root, *group_paths, leaf]},
        )
        self.assertEqual(len(visited), len(set(visited)))

    def test_partial_network_failure_does_not_return_a_catalog(self):
        with patch.object(
            catalog, "fetch_page", side_effect=ValueError("broken source")
        ):
            with self.assertRaisesRegex(ValueError, "broken source"):
                catalog.discover()


if __name__ == "__main__":
    main()
