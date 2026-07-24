#!/usr/bin/env bash
#
# Re-download the upstream rulebooks that back the skills in this repository.
#
# Reference files are kept verbatim from upstream so they can be refreshed
# without merge work. Local modifications are listed below and re-applied here;
# each skill's SKILL.md records the same list.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UPSTREAM="https://raw.githubusercontent.com/ciembor/agent-rules-books/main"

download() {
    local remote_path="$1"
    local local_path="$REPO_DIR/$2"

    if [ ! -d "$(dirname "$local_path")" ]; then
        echo "error: no directory for $local_path" >&2
        exit 1
    fi

    curl -sSfL -o "$local_path" "$UPSTREAM/$remote_path"
    echo "  $remote_path -> $2"
}

# Insert a line immediately after an anchor line, failing if the anchor is
# missing (upstream changed) or the line is already present.
insert_after() {
    local file="$REPO_DIR/$1"
    local anchor="$2"
    local line="$3"

    if grep -qF -- "$line" "$file"; then
        echo "error: $1 already contains the local modification" >&2
        exit 1
    fi

    if ! grep -qF -- "$anchor" "$file"; then
        echo "error: anchor not found in $1: $anchor" >&2
        echo "       upstream changed; re-apply the local modification by hand" >&2
        exit 1
    fi

    awk -v anchor="$anchor" -v line="$line" '
        { print }
        index($0, anchor) && !done { print line; done = 1 }
    ' "$file" > "$file.tmp"

    mv "$file.tmp" "$file"
    echo "  patched $1"
}

echo "Downloading upstream rulebooks:"
download "clean-architecture/clean-architecture.md" \
    "skills/clean-architecture/references/clean-architecture.md"
download "domain-driven-design/domain-driven-design.md" \
    "skills/domain-driven-design/references/domain-driven-design.md"

echo "Applying local modifications:"
insert_after "skills/clean-architecture/references/clean-architecture.md" \
    "If constraints force a compromise:" \
    "- **CONFIRM WITH THE USER AND GET THEIR EXPLICIT APPROVAL FIRST!**"

echo "Done."
