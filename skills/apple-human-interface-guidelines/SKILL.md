---
name: apple-human-interface-guidelines
description: Design, implement, or review interfaces for iOS, iPadOS, macOS, watchOS, tvOS, and visionOS using Apple's Human Interface Guidelines, including foundations, patterns, components, inputs, and system integrations. Use for Apple platform UX decisions and HIG reviews; not for generic web styling, backend architecture, or API implementation without a design question.
---

# Apple Human Interface Guidelines

Use this skill to make concrete Apple platform design decisions and review their implementation.
The references contain original application notes, a complete discovered topic index, section
outlines, and Apple-hosted image references. They are **not a verbatim or complete offline copy**
of Apple's HIG. Apple supplies a downloadable full Markdown version of each article.

## Workflow

1. Identify the target platforms, supported OS versions, input methods, user task, and existing
   interface conventions. Preserve the user's explicit design choices. A web app running on an
   Apple device does not automatically need to imitate a native Apple app.
2. Read [practical guidance](references/practice.md) and the relevant platform topic under
   [the catalog](references/catalog.md). Find topics by title or search the reference filenames;
   do not read the entire catalog into context.
3. Read the relevant foundation, task pattern, component, and input references. Each topic links
   to Apple's article and **Official full Markdown**. MUST consult the current official article
   before treating a platform detail, size, availability, or conditional recommendation as a
   requirement. The original notes and section outlines omit details.
4. Follow the article's platform considerations. Use system components where they fit the task;
   use custom controls deliberately and account for their interaction states and accessibility.
   MUST distinguish Apple's recommendation, the user's product requirements, and your own design
   judgment. Do not turn a qualified recommendation into a universal prohibition.
5. Check the interaction through its full lifecycle: entry and restoration, loading, empty content,
   success, error recovery, cancellation, and undo when relevant. Include accessibility, privacy,
   localization, appearance, resizing, and every supported input method in the applicable checks.
6. Explain the resulting design decisions. In a review, report the observed behavior and location,
   consequence, relevant HIG article, and a concrete fix. Separate visual observations, source
   inspection, and device or assistive-technology checks; identify unverified behavior.

## Reference routing

- **Platform conventions:** [Getting started](references/topics/getting-started.md), then the
  relevant “Designing for” topic in [the catalog](references/catalog.md).
- **Shared visual and interaction rules:** [Foundations](references/topics/foundations.md),
  particularly accessibility, layout, typography, color, materials, privacy, and writing.
- **Task flows and state:** [Patterns](references/topics/patterns.md), including launching,
  onboarding, loading, feedback, modality, searching, accounts, and undo.
- **Choosing controls:** [Components](references/topics/components.md) routes to content,
  layout and organization, menus and actions, navigation and search, presentation, selection
  and input, status, and system experiences.
- **Interaction methods:** [Inputs](references/topics/inputs.md), including keyboard, pointer,
  gestures, focus, eyes, Apple Pencil, and device controls.
- **System integrations:** [Technologies](references/topics/technologies.md), including Apple Pay,
  Sign in with Apple, Siri, generative AI, HealthKit, and CarPlay. Check their own documentation
  for implementation contracts; HIG guidance is not an API specification.

## Sources, images, and freshness

Apple's [HIG](https://developer.apple.com/design/human-interface-guidelines/) and
[design resources](https://developer.apple.com/design/resources/) are authoritative.
[Research and provenance](references/research.md) describes the download search, scope, source
format, and refresh procedure. The catalog records its retrieval timestamp and each JSON source's
SHA-256. A source hash identifies a snapshot; it does not prove that today's guidance is unchanged.

Images in topic references are remote Markdown embeds with source appearance/resolution traits.
MUST inspect a relevant image before describing its visual details; filenames and generic alt text
do not establish what it depicts. Apple retains rights to its text, images, trademarks, and design
resources; the repository's MIT license does not relicense them. No Apple image bytes or full
article bodies are bundled. Do not copy these example images into a shipping product as assets.

To refresh the metadata catalog, run from the repository root:

```sh
python3 skills/apple-human-interface-guidelines/scripts/catalog.py refresh
make format-hig
make check-hig
```

A refresh updates metadata and navigation, not the authored design notes. Review source changes
and revise those notes when needed. Network, decoding, schema, and removed-topic failures must
be resolved explicitly; do not present a partial refresh as complete coverage.
