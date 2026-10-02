# AGENTS.md

This repository is a collection of reusable skills for coding agents. Every skill lives in
`skills/<skill-name>/SKILL.md` with YAML frontmatter (`name`, `description`) — the format read by
both Claude Code and Codex.

## Available skills

| Skill | Read when |
| --- | --- |
| [`architecture-review`](skills/architecture-review/SKILL.md) | Reviewing a diff, branch, or module against the Clean Architecture and DDD rulebooks. Loads both rulebooks and reports violations. |
| [`clean-architecture`](skills/clean-architecture/SKILL.md) | Writing, placing, reviewing, or refactoring code in a layered codebase: dependency direction, use-case boundaries, ports and adapters, keeping frameworks/DB/UI replaceable. |
| [`domain-driven-design`](skills/domain-driven-design/SKILL.md) | Modeling a business domain: ubiquitous language, bounded contexts, entities vs value objects, aggregate boundaries, repositories, factories, specifications, anti-corruption layers. |
| [`pentest-dispatch`](skills/pentest-dispatch/SKILL.md) | Coordinating an authorized, scope-locked penetration test across parallel subagents (recon → fan-out → synthesis). Requires written authorization and a locked `scope.json`; enforces no-DoS/SE/PII/out-of-scope guardrails. |

An agent that does not auto-discover skills should read the relevant `SKILL.md` in full before
starting work that matches its trigger conditions, and treat it as binding policy for that task.

## How the rulebook skills are built

`clean-architecture` and `domain-driven-design` wrap upstream rulebooks from
[`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) (MIT). The reference
file under each skill is a **verbatim download** of the upstream document, and `SKILL.md` is a thin
wrapper that tells the agent to read it in full. Nothing is summarized or paraphrased — a summary
would silently drop binding rules.

Re-download with `./update-sources.sh`. That script also re-applies the repository's local
modifications and fails loudly if an upstream anchor has moved, so a modification is never silently
lost. Current local modifications:

- `clean-architecture`: "When Tradeoffs Are Necessary" requires explicit user approval before an
  architectural compromise stands.

## Authoring rules for this repo

A skill directory contains:

```
skills/<skill-name>/
├── SKILL.md            # required — frontmatter + the operative policy
├── references/         # optional — deep material loaded only when needed
└── scripts/            # optional — executable helpers
```

- Frontmatter carries exactly two fields: `name` (kebab-case, matching the directory name) and
  `description`. Both Claude Code and Codex require these; extra fields are not portable.
- The `description` must state both when the skill applies and when it does not. It is the only
  thing an agent sees before deciding to load the skill, so front-load the trigger words.
- Keep `SKILL.md` operative and scannable. Move exhaustive detail into `references/` and link to it
  by relative path, so the full text is loaded only when a question needs it.
- Write rules an agent can act on. Prefer `MUST`/`MUST NOT` over prose about principles.
- Skills must not depend on a specific language, framework, or agent runtime.
- When vendoring external material, download it verbatim rather than rewriting it, record the source
  and license in `SKILL.md`, and add it to `update-sources.sh` with any local modifications.

## Subagents

`agents/architecture-reviewer.md` is a Claude Code subagent that delegates to the
`architecture-review` skill. The skill holds the review procedure so that the agent and Codex — which
has no equivalent subagent format — cannot drift apart. Keep the procedure in the skill; keep the
agent thin.
