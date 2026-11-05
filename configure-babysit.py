#!/usr/bin/env python3
"""Install the shared babysit activation rule without replacing other guidance."""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil

BEGIN = "<!-- pavel-d/skills:babysit:start -->"
END = "<!-- pavel-d/skills:babysit:end -->"
INSTRUCTION_PATHS = {
    "codex": Path(".codex/AGENTS.md"),
    "claude": Path(".claude/CLAUDE.md"),
    "opencode": Path(".config/opencode/AGENTS.md"),
}


def with_policy(content: str, policy: str) -> str:
    """Replace only our managed block; reject ambiguous or damaged markers."""
    block = f"{BEGIN}\n\n{policy.rstrip()}\n\n{END}"
    if BEGIN not in content and END not in content:
        separator = "\n\n" if content and not content.endswith("\n") else "\n"
        return f"{content}{separator if content else ''}{block}\n"
    if content.count(BEGIN) != 1 or content.count(END) != 1:
        raise ValueError("expected exactly one pair of babysit markers")
    start = content.index(BEGIN)
    finish = content.index(END)
    if finish < start:
        raise ValueError("babysit markers are reversed")
    return content[:start] + block + content[finish + len(END) :]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("agents", nargs="+", choices=INSTRUCTION_PATHS)
    parser.add_argument("--home", type=Path, default=Path.home())
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    home = args.home.expanduser().resolve()
    policy = (Path(__file__).parent / "instructions/babysit.md").read_text()
    if "codex" in args.agents:
        override = home / ".codex/AGENTS.override.md"
        if override.exists() and override.read_text().strip():
            parser.error(f"{override} shadows AGENTS.md; reconcile it first")
    updates = []
    for agent in dict.fromkeys(args.agents):
        path = home / INSTRUCTION_PATHS[agent]
        before = path.read_text() if path.exists() else ""
        try:
            after = with_policy(before, policy)
        except ValueError as error:
            parser.error(f"{path}: {error}")
        updates.append((path, before, after))
    if args.check:
        outdated = [str(path) for path, before, after in updates if before != after]
        if outdated:
            parser.error(
                "babysit activation missing or outdated: " + ", ".join(outdated)
            )
        print("Babysit activation is current for: " + ", ".join(args.agents))
        return
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    for path, before, after in updates:
        if before == after:
            print(f"Already current: {path}")
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            backup = path.with_name(f"{path.name}.pre-babysit-{timestamp}")
            shutil.copy2(path, backup)
            print(f"Backup: {backup}")
        path.write_text(after)
        print(f"Configured: {path}")


if __name__ == "__main__":
    main()
