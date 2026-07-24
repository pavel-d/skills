---
name: architecture-review
description: Review code against Clean Architecture and Domain-Driven Design rulebooks and report violations. Use when reviewing a diff, branch, pull request, or module for boundary violations, dependency-direction problems, framework or persistence leakage into the domain, anemic domain models, primitive obsession, bad aggregate boundaries, god services, layer bypass, or bounded-context leakage — and before merging a change that adds or reshapes layers, aggregates, repositories, or integrations. Do not use for style, formatting, performance, or security review, or for codebases that have deliberately chosen a different architectural style.
---

# Architecture Review

Review code against two binding rulebooks and report violations. Do not modify code as part of the review.

## Before reviewing anything

Load both skills and read their reference documents **in full**:

- `clean-architecture` → `references/clean-architecture.md`
- `domain-driven-design` → `references/domain-driven-design.md`

Those documents are the review criteria. Do not review from memory, from general knowledge of Clean Architecture or DDD, or from the skills' own summaries — read the actual files first, every time. If they cannot be read, say so and stop rather than reviewing without them.

In those documents `MUST` is binding, `MUST NOT` is forbidden, and `SHOULD` is a strong default. Grade findings accordingly.

## Scope

Review the code you were asked to review; default to the working diff against the base branch when no scope is given. Read enough surrounding code to judge dependency direction and boundaries correctly — a violation is about where code sits relative to its layer and context, which a diff alone often does not show.

Establish first, and state in the report:

- Which layer each changed file belongs to: domain, application, interface adapters, or infrastructure.
- Which bounded context it belongs to, and whether that boundary is explicit in the code.
- Whether the area is core domain, supporting, or generic — both rulebooks demand more rigor in the core and explicitly forbid over-modeling elsewhere.

## What to check

Work through the checklists the rulebooks define — Clean Architecture's "Review Checklist" and "Forbidden Patterns", and DDD's "Review Rules", "Review Checklist", and "Forbidden Patterns". Do not substitute a different checklist for theirs.

Pay particular attention to the failures both books call out:

- Source dependencies pointing outward; inner layers importing outer ones.
- Framework, ORM, vendor, or transport types leaking into domain or application code.
- Business rules sitting in controllers, handlers, jobs, gateways, or repository implementations.
- Use cases doing delivery, persistence, or presentation work; layer bypass.
- Anemic entities, missing value objects, primitive obsession, invalid construction paths.
- Aggregates sized for the ORM rather than for invariants; cross-aggregate object references where identity belongs; transactions spanning aggregates.
- Repositories mapped to tables rather than aggregate roots; generic query utilities.
- Bounded context bleeding, missing or implicit translation, foreign vocabulary adopted natively.
- God services; utility, shared, common, or base dumping grounds.
- Core domain buried under generic mechanisms while peripheral code is over-modeled.
- Tests that need the framework, database, or network to exercise business rules.

## Judgment

Both rulebooks warn against their own overapplication: DDD forbids "fake DDD" and over-modeling simple subdomains, and Clean Architecture forbids boundaries whose cost exceeds the option value they preserve. Do not raise a finding merely because a pattern is absent. Every finding must name a rule from the documents and a concrete consequence.

Do not flag pre-existing code outside the reviewed scope unless the change makes it materially worse; mention it separately as context when it explains a finding.

## Reporting

Report findings most severe first. For each:

1. **Location** — `file_path:line`.
2. **Rule** — the specific rule violated, quoted or closely paraphrased, naming the rulebook and section.
3. **Why it matters** — the concrete consequence: what breaks, what becomes untestable, what gets coupled, which future change becomes expensive.
4. **Fix** — a concrete refactoring that follows the rulebooks' own refactoring rules; prefer safe incremental boundary extraction over a rewrite.

Then give the checklist verdict — for each item in both review checklists: pass, fail, or not applicable — and finish with a short summary of the architectural health of the change.

If the change is clean, say so plainly. Do not manufacture findings.

If a constraint genuinely forces an architectural compromise, do not quietly accept it and do not unilaterally endorse it: state the violation, its cost, and the cleaner alternative, and require the user's explicit approval before it stands.
