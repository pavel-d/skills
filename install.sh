#!/usr/bin/env bash
#
# Symlink the skills in this repository into an agent's skill directory.
#
# Claude Code users can instead install this repo as a plugin (see README.md);
# this script is for Codex and for Claude Code without the plugin system.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$REPO_DIR/skills"

usage() {
    cat <<EOF
Usage: $(basename "$0") <target> [project-dir]

Targets:
  codex-user        \$HOME/.agents/skills                  (all Codex sessions)
  codex-project     <project-dir>/.agents/skills           (one repository)
  claude-user       \$HOME/.claude/skills                  (all Claude Code sessions)
  claude-project    <project-dir>/.claude/skills           (one repository)
  opencode-user     \$HOME/.config/opencode/skills         (all opencode sessions)
  opencode-project  <project-dir>/.opencode/skills         (one repository)

project-dir defaults to the current directory and is only used by the
*-project targets.

Each skill is symlinked, so a "git pull" in this repository updates every
install.
EOF
}

if [ $# -lt 1 ]; then
    usage >&2
    exit 2
fi

target="$1"
project_dir="${2:-$PWD}"

case "$target" in
    codex-user)     dest="$HOME/.agents/skills" ;;
    codex-project)  dest="$project_dir/.agents/skills" ;;
    claude-user)    dest="$HOME/.claude/skills" ;;
    claude-project) dest="$project_dir/.claude/skills" ;;
    opencode-user)    dest="$HOME/.config/opencode/skills" ;;
    opencode-project) dest="$project_dir/.opencode/skills" ;;
    -h|--help)      usage; exit 0 ;;
    *)
        echo "error: unknown target '$target'" >&2
        usage >&2
        exit 2
        ;;
esac

if [ ! -d "$SOURCE_DIR" ]; then
    echo "error: no skills directory at $SOURCE_DIR" >&2
    exit 1
fi

mkdir -p "$dest"

installed=0
for skill_dir in "$SOURCE_DIR"/*/; do
    skill_name="$(basename "$skill_dir")"

    if [ ! -f "$skill_dir/SKILL.md" ]; then
        echo "error: $skill_name has no SKILL.md" >&2
        exit 1
    fi

    link="$dest/$skill_name"
    source_path="${skill_dir%/}"

    if [ -L "$link" ]; then
        current="$(readlink "$link")"
        if [ "$current" != "$source_path" ]; then
            echo "error: $link already links to $current" >&2
            echo "       remove it first, or install to a different target" >&2
            exit 1
        fi
    elif [ -e "$link" ]; then
        echo "error: $link already exists and is not a symlink" >&2
        exit 1
    else
        ln -s "$source_path" "$link"
    fi

    echo "  $skill_name -> $link"
    installed=$((installed + 1))
done

if [ "$installed" -eq 0 ]; then
    echo "error: no skills found in $SOURCE_DIR" >&2
    exit 1
fi

echo "Installed $installed skill(s) into $dest"
