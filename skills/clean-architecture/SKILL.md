---
name: clean-architecture
description: Apply Robert C. Martin's Clean Architecture when writing, placing, reviewing, or refactoring application code — the dependency rule, layer responsibilities, use-case boundaries, ports and adapters, and keeping frameworks, databases, and UI as replaceable details. Use when adding a feature to a layered codebase, deciding which layer new code belongs in, designing module or package structure, introducing an interface for an external dependency, reviewing a diff for boundary violations, or breaking up a god service. Do not use for throwaway scripts, one-file prototypes, config-only edits, or codebases that have deliberately chosen a different architectural style.
---

# Clean Architecture

**Read [`references/clean-architecture.md`](references/clean-architecture.md) in full now, and follow it as binding policy for this task.** Do not act on a summary of it.

It is the complete rulebook: the Dependency Rule, required layer responsibilities, code generation rules, architecture heuristics, component and boundary rules, naming, testing, forbidden patterns, refactoring rules, and the review checklist to run before finalizing any change.

`MUST` is binding, `SHOULD` is a strong default, `MUST NOT` is forbidden.

If constraints force an architectural compromise, **confirm with the user and get their explicit approval first** — state the violation, its cost, and the cleaner alternative, then wait.

**Source:** verbatim copy of [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books/blob/main/clean-architecture/clean-architecture.md) (MIT), with one local addition: the approval requirement above, added to "When Tradeoffs Are Necessary". Refresh with `./update-sources.sh`.
