---
name: domain-driven-design
description: Apply Eric Evans' Domain-Driven Design when modeling a business domain — ubiquitous language, bounded contexts, entities vs value objects, aggregate boundaries, repositories, factories, specifications, and anti-corruption layers. Use when naming domain concepts, deciding whether something is an entity or a value object, drawing aggregate or transaction boundaries, integrating with another system's model, replacing primitives that carry business meaning, extracting rules from repeated conditionals, or reviewing code for a passive/anemic domain model. Do not use for CRUD-only supporting subdomains, technical infrastructure with no business rules, or codebases where the domain is genuinely trivial.
---

# Domain-Driven Design

**Read [`references/domain-driven-design.md`](references/domain-driven-design.md) in full now, and follow it as binding policy for this task.** Do not act on a summary of it.

It is the complete rulebook: knowledge crunching and deep models, ubiquitous language, bounded contexts and context mapping, strategic design and distillation, large-scale structure, the building blocks (entities, value objects, aggregates, domain services, repositories, factories, specifications), supple design, translation at boundaries, testing rules, forbidden patterns, refactoring rules, and the review checklist to run before finalizing any change.

`MUST` is binding, `SHOULD` is a strong default, `MUST NOT` is forbidden.

Note its Primary Directive: when uncertain, prefer the option that makes the domain model clearer — and simplify aggressively outside the core domain rather than applying every pattern everywhere.

**Source:** verbatim copy of [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books/blob/main/domain-driven-design/domain-driven-design.md) (MIT), unmodified. Refresh with `./update-sources.sh`.
