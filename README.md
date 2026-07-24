# ai-skills

Reusable engineering skills for coding agents, in a format both **Claude Code** and **Codex** read
natively, and installable in Claude Code as a plugin.

Every skill is a directory containing a `SKILL.md` with `name` and `description` frontmatter — the
common denominator across agents — plus `references/` for material loaded only when a task needs it.

## Skills

| Skill | What it does |
| --- | --- |
| [`architecture-review`](skills/architecture-review/SKILL.md) | Reviews a diff, branch, or module against both rulebooks below and reports violations with locations, cited rules, consequences, and concrete fixes. |
| [`clean-architecture`](skills/clean-architecture/SKILL.md) | Robert C. Martin's Clean Architecture: the dependency rule, layer responsibilities, ports and adapters, forbidden patterns, review checklist. |
| [`domain-driven-design`](skills/domain-driven-design/SKILL.md) | Eric Evans' Domain-Driven Design: ubiquitous language, bounded contexts, aggregates, repositories, factories, specifications, anti-corruption layers. |

The two rulebook skills are **verbatim downloads** of the upstream documents (see
[Sources](#sources)), wrapped in a `SKILL.md` that tells the agent to read them in full. They are
not summarized — a summary would silently drop binding rules.

## The reviewer

`architecture-review` is the reviewer: it reads both rulebooks in full, then reviews against *their*
checklists rather than a paraphrase. It reports each finding with a file:line, the specific rule
violated, the concrete consequence, and a fix — and it will not accept an architectural compromise
without your explicit approval.

In Claude Code it is also packaged as a subagent, [`architecture-reviewer`](agents/architecture-reviewer.md),
which delegates to the same skill:

```
@ai-skills:architecture-reviewer review the current branch
```

In Codex, invoke the skill directly:

```
$architecture-review review the current branch
```

## Install

### Claude Code (plugin)

```
/plugin marketplace add pavel-d/skills
/plugin install ai-skills@ai-skills
/reload-plugins
```

To try it from a local checkout, point the marketplace at the directory instead:

```
/plugin marketplace add /path/to/skills
/plugin install ai-skills@ai-skills
```

Plugin components are namespaced — invoke explicitly with `/ai-skills:architecture-review` or
`@ai-skills:architecture-reviewer`, or let Claude load them automatically when a task matches.

### Claude Code (without the plugin system)

```sh
./install.sh claude-user                     # ~/.claude/skills, all sessions
./install.sh claude-project ~/code/my-app    # one repository
```

### Codex

```sh
./install.sh codex-user                      # ~/.agents/skills, all sessions
./install.sh codex-project ~/code/my-app     # one repository
```

Codex discovers skills in `.agents/skills` (walking from the working directory up to the repo root)
and in `$HOME/.agents/skills`. Type `$` in the CLI to invoke one explicitly, or let Codex match it
implicitly against the description. Codex has no subagent format, so the reviewer is used as a skill
there.

### Any other agent

Point the agent at [`AGENTS.md`](AGENTS.md), which indexes every skill with its trigger conditions,
or copy the skill directory into whatever location that agent reads.

`install.sh` creates symlinks, so `git pull` in this repository updates every install.

## Sources

The rulebooks come from [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books)
(MIT) and distill *Clean Architecture* by Robert C. Martin and *Domain-Driven Design* by Eric Evans.

Refresh them with:

```sh
./update-sources.sh
```

The script re-downloads each document and re-applies this repository's local modifications, failing
loudly if an upstream anchor has moved rather than silently dropping a change. Local modifications:

- **clean-architecture** — "When Tradeoffs Are Necessary" requires explicit user approval before an
  architectural compromise stands.
- **domain-driven-design** — none; byte-identical to upstream.

## Adding a skill

```
skills/<skill-name>/
├── SKILL.md            # required — frontmatter + operative policy
├── references/         # optional — detail loaded on demand
└── scripts/            # optional — executable helpers
```

Authoring rules are in [`AGENTS.md`](AGENTS.md). In short: `name` must match the directory, the
`description` must say when the skill applies *and* when it does not, and vendored external material
is downloaded verbatim and registered in `update-sources.sh` — never rewritten by hand.

## License

[MIT](LICENSE) — see the file for upstream attribution.
