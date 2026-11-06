# HIG research, download findings, and provenance

Research date: 2026-11-06. See [catalog.json](catalog.json) for the exact metadata retrieval time,
coverage graph, source URLs, source SHA-256 values, and image variants.

## Official downloadable material

Apple provides a full Markdown response for each HIG page. The HTML entrypoint advertises it with
a “View Markdown” link. Verified examples:

- [HIG entrypoint, Markdown](https://developer.apple.com/design/human-interface-guidelines.md)
- [Buttons, Markdown](https://developer.apple.com/design/human-interface-guidelines/buttons.md)
- [Foundations, Markdown](https://developer.apple.com/design/human-interface-guidelines/foundations.md)

The response contains article metadata in an HTML comment, article text, Markdown images, related
resources, and change logs where the article has them. Individual Markdown download URLs were
successfully fetched for all 173 topics during initial research. These are downloadable pages,
not evidence of a supported bulk archive or an offline documentation bundle.

Searches of Apple's HIG and design-resource pages did not identify a current official all-in-one
HIG PDF, EPUB, Markdown ZIP, or docset. Historical platform-specific PDFs do not establish current
coverage. Third-party converters and archives exist, but their code licenses do not establish
rights to redistribute Apple's article bodies or illustrations. This skill uses direct Apple
sources instead. A search cannot prove that no other download exists.

[Apple Design Resources](https://developer.apple.com/design/resources/) provides downloadable
design templates, UI kits, fonts, and production resources. These serve a different purpose from
the HIG and have their own terms; they are not a downloadable edition of the manual. Apple's
[2022 HIG announcement](https://developer.apple.com/news/?id=v8a3aetj) explains the move to unified
cross-platform guidance and linked platform considerations.

## Structured source and coverage method

The entrypoint's public structured response is
[human-interface-guidelines.json](https://developer.apple.com/tutorials/data/design/human-interface-guidelines.json).
Topic responses use the same `/tutorials/data` prefix followed by the HIG path and `.json`.
The verified response has `schemaVersion`, `metadata.title`, `references`, `topicSections`, and
`primaryContentSections`. Image references contain `variants` with URLs and appearance/resolution
traits. These public endpoints are an observed publishing implementation, not a promised stable
API; the refresh script validates the fields it relies on and fails on malformed data.

An important asset-resolution detail: JSON image paths beginning with `/images/` refer to the
documentation renderer's `/tutorials/images/` namespace, not the website root. The published
HTML declares `/tutorials/` as its base, and direct image GETs confirmed this location. Resolving
those paths as `https://developer.apple.com/images/...` returns 404. Absolute CDN references
retain their original URLs. The parser fixture checks this distinction.

The crawler starts with the HIG root and follows every HIG topic reference to a fixed point,
including related topics that are absent from the root's featured cards. It does not follow
developer API pages, WWDC pages, other language editions, or the entire Apple Developer website.
The initial graph contained 173 pages. Its six category entrypoints contained:

| Category        |                Immediate children |
| --------------- | --------------------------------: |
| Getting started |                                 9 |
| Foundations     |                                18 |
| Patterns        |                                25 |
| Components      | 8 groups, with their own children |
| Inputs          |                                13 |
| Technologies    |                                29 |

Counts of immediate children are not counts of all descendants, and a page can be linked from
multiple places. The catalog deduplicates by canonical HIG path. Source headings are retained as
navigation metadata, not as a substitute for the paragraphs, tables, or qualified guidance beneath
them. Authored notes are concise original commentary and are maintained separately from metadata.

All image variants exposed by each page's reference dictionary are included as remote Markdown
embeds. This includes article illustrations, related-topic cards, and resource/video thumbnails;
it does not mean that every image is an illustration from the article body. The initial snapshot
had 6,305 per-page image references and 3,246 distinct URLs. The verified hosts are
`developer.apple.com`, `docs-assets.developer.apple.com`, and `devimages-cdn.apple.com`. Images
are not downloaded by the refresh script, and URL discovery alone is not an image availability
or visual inspection check. Video playback is not mirrored.

## Reuse and attribution

The source JSON identifies Apple as copyright owner and links to
[Apple Website Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html).
No open redistribution license for the full HIG corpus was found. Apple's downloadable design
resources also carry a separate
[Apple Design Resources license](https://developer.apple.com/support/downloads/terms/apple-design-resources/Apple-Design-Resources-License-20230621-English.pdf).

This repository therefore distributes original skill instructions and application notes, factual
source metadata, source links, and remote image references. It does not vendor Apple's full
article text or image files. The MIT license applies to this repository's original work; it does
not grant rights to Apple material reachable through the links. This distinction is also why this
skill's generated references differ from the repository's verbatim MIT-licensed rulebook sources.

## Maintenance

From the repository root:

```sh
python3 skills/apple-human-interface-guidelines/scripts/catalog.py refresh
make format-hig
make check-hig
```

Requirements: Python 3.11+, curl with system TLS trust, and the repository's pinned Prettier and
Ruff tools for formatting and checks. The refresh uses four concurrent public HTTPS requests and
requires no Apple account or API key. It validates every downloaded page before writing any
catalog output. HTTP failures, invalid JSON, missing required fields, unresolved HIG children,
unknown image hosts, and disappeared topics stop the operation with an error.

Refresh updates metadata and generated topic references. It preserves original notes in
`notes.json`; review them against upstream changes. Added topics without authored notes remain
explicitly marked as discovery entries. Removed topics require a deliberate review rather than
automatic deletion. Check the resulting diff and rerun formatting and validation before committing.

`check` is offline: it validates graph closure, unique paths, the expected topic file set, and
generated text against the manifest and notes. Parser tests use small metadata-only fixtures
derived from verified Apple responses; they do not contain article paragraphs or image bytes.
Neither check establishes that every remote image renders or that current live HIG text still
matches the recorded snapshot. Fetch the relevant official Markdown when applying a specific rule.
