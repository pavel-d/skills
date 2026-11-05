# ai-skills

Reusable engineering skills for coding agents, in a format both **Claude Code** and **Codex** read
natively, and installable in Claude Code and Codex (CLI and desktop) as a plugin.

Every skill is a directory containing a `SKILL.md` with `name` and `description` frontmatter — the
common denominator across agents — plus `references/` for material loaded only when a task needs it.

## Skills

| Skill                                                                  | What it does                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`babysit-the-change-or-pr`](skills/babysit-the-change-or-pr/SKILL.md) | Carries code changes and PRs through the authorized stage: local validation, review, CI, merge, publication, automatic deployment, and live verification.                                                                                            |
| [`architecture-review`](skills/architecture-review/SKILL.md)           | Reviews a diff, branch, or module against both rulebooks below and reports violations with locations, cited rules, consequences, and concrete fixes.                                                                                                 |
| [`clean-architecture`](skills/clean-architecture/SKILL.md)             | Robert C. Martin's Clean Architecture: the dependency rule, layer responsibilities, ports and adapters, forbidden patterns, review checklist.                                                                                                        |
| [`domain-driven-design`](skills/domain-driven-design/SKILL.md)         | Eric Evans' Domain-Driven Design: ubiquitous language, bounded contexts, aggregates, repositories, factories, specifications, anti-corruption layers.                                                                                                |
| [`pentest-dispatch`](skills/pentest-dispatch/SKILL.md)                 | Orchestrates an authorized penetration test across parallel subagents — scope-locked recon, API/auth mapping, web/API/cloud/auth/business-logic testing, and synthesis — with always-on guardrails (no DoS, SE, PII exfil, or out-of-scope probing). |

The two rulebook skills are **verbatim downloads** of the upstream documents (see
[Sources](#sources)), wrapped in a `SKILL.md` that tells the agent to read them in full. They are
not summarized — a summary would silently drop binding rules.

## The reviewer

`architecture-review` is the reviewer: it reads both rulebooks in full, then reviews against _their_
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
/plugin install ai-skills@pavel-d
/reload-plugins
```

To try it from a local checkout, point the marketplace at the directory instead:

```
/plugin marketplace add /path/to/skills
/plugin install ai-skills@pavel-d
```

Plugin components are namespaced — invoke explicitly with `/ai-skills:architecture-review` or
`@ai-skills:architecture-reviewer`, or let Claude load them automatically when a task matches.

### Claude Code (without the plugin system)

```sh
./install.sh claude-user                     # ~/.claude/skills, all sessions
./install.sh claude-project ~/code/my-app    # one repository
```

### Codex CLI and desktop (plugin)

Register the Git-backed marketplace and install the plugin at user scope:

```sh
codex plugin marketplace add pavel-d/skills --ref main
codex plugin add ai-skills@pavel-d
```

The same user configuration is used by Codex CLI and Codex in the ChatGPT desktop app.
Start a new session after installation; restart the desktop app if its plugin list is stale.
The marketplace appears as **Pavel's Skills**. Invoke the skill explicitly as
`$ai-skills:babysit-the-change-or-pr`, or let Codex select it for a matching task.

Update from the central repository:

```sh
codex plugin marketplace upgrade pavel-d
codex plugin add ai-skills@pavel-d
```

For Claude Code, use `claude plugin marketplace update pavel-d` followed by
`claude plugin update ai-skills@pavel-d`. Reload plugins or start a new session afterward.
Updates are fetched by each machine's plugin manager; this repository does not push changes
into already-running sessions or other machines automatically.

### Codex (without the plugin system)

```sh
./install.sh codex-user                      # ~/.agents/skills, all sessions
./install.sh codex-project ~/code/my-app     # one repository
```

Codex discovers skills in `.agents/skills` (walking from the working directory up to the repo root)
and in `$HOME/.agents/skills`. Type `$` in the CLI to invoke one explicitly, or let Codex match it
implicitly against the description. Codex has no subagent format, so the reviewer is used as a skill
there.

### opencode

```sh
./install.sh opencode-user                   # ~/.config/opencode/skills, all sessions
./install.sh opencode-project ~/code/my-app  # one repository
```

opencode discovers skills in `.opencode/skills` (walking from the working directory up to the repo
root) and in `~/.config/opencode/skills`. It also reads the `.claude/skills` and `.agents/skills`
locations, so a `claude-*` or `codex-*` install is picked up too; the `opencode-*` targets install
to opencode's own directories.

### Any other agent

Point the agent at [`AGENTS.md`](AGENTS.md), which indexes every skill with its trigger conditions,
or copy the skill directory into whatever location that agent reads.

`install.sh` creates symlinks, so `git pull` in this repository updates every install.

### Apply babysit in every agent session

Plugin installation makes the skill available. To require its use for code-change and PR tasks
in every repository, install the user-level activation rule on each machine:

```sh
python3 configure-babysit.py codex claude opencode
python3 configure-babysit.py --check codex claude opencode
```

Install the skill first: use the plugin for Codex and Claude Code, and
`./install.sh opencode-user` for OpenCode. Avoid installing both symlinks and the plugin in the
same harness, since that exposes duplicate copies of skills.

The configurator updates a marked block in `~/.codex/AGENTS.md`, `~/.claude/CLAUDE.md`, and
`~/.config/opencode/AGENTS.md`. It preserves other instructions, backs up changed existing files,
and rejects malformed managed blocks or a Codex global override that would hide the rule.
It targets the standard home locations; with a custom `CODEX_HOME` or `XDG_CONFIG_HOME`, adapt
the instruction destination before using it. Use `--home /path/to/home` to stage or inspect an
installation. No credentials or service configuration are changed.

The rule loads the installed skill; its workflow remains centrally maintained in
[`skills/babysit-the-change-or-pr/SKILL.md`](skills/babysit-the-change-or-pr/SKILL.md).
The activation text lives in [`instructions/babysit.md`](instructions/babysit.md); rerun the
configurator after changing that text. Read-only tasks do not invoke babysit. A local-fix request
finishes at validated local changes, and a delivery request continues only through its authorized
stages. Global activation grants no extra permission to push, merge, deploy, or restart services.

When migrating a custom skill, first verify the plugin's installed copy, then move the custom
directory to a backup outside all skill discovery directories. Start a new session and verify
that the plugin copy is the one discovered. Existing sessions keep their previously loaded
instructions until refreshed or restarted.

## Development checks

The formatting commands use pinned Prettier and Ruff versions through `npx` and `uvx`.
They cover the plugin and babysit integration files; upstream rulebooks remain verbatim.

```sh
make format
make format-check
make test
```

## Sources

The rulebooks come from [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books)
(MIT) and distill _Clean Architecture_ by Robert C. Martin and _Domain-Driven Design_ by Eric Evans.

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
`description` must say when the skill applies _and_ when it does not, and vendored external material
is downloaded verbatim and registered in `update-sources.sh` — never rewritten by hand.

## License

[MIT](LICENSE) — see the file for upstream attribution.
