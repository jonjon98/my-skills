#!/usr/bin/env bash
# Symlink every skill in ./skills into the global skill directories.
#   ~/.agents/skills/<name> -> <this repo>/skills/<name>
#   ~/.claude/skills/<name> -> ../../.agents/skills/<name>
# Safe to re-run. Existing real folders are left alone.
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
agents="$HOME/.agents/skills"
claude="$HOME/.claude/skills"
mkdir -p "$agents" "$claude"

link() { # link <target> <path>
  if [ -e "$2" ] && [ ! -L "$2" ]; then
    echo "skip  $2 (real folder exists, remove it first)"
    return
  fi
  ln -sfn "$1" "$2"
  echo "link  $2 -> $1"
}

for dir in "$repo"/skills/*/; do
  name="$(basename "$dir")"
  link "$repo/skills/$name" "$agents/$name"
  link "../../.agents/skills/$name" "$claude/$name"
done

# task-memory: choose where task progress is stored (written to the skill's config.env).
# Set TASK_MEMORY_DIR to skip the prompt. An existing config.env is kept.
cfg="$repo/skills/task-memory/config.env"
if [ ! -f "$cfg" ]; then
  dir="${TASK_MEMORY_DIR:-}"
  if [ -z "$dir" ]; then
    read -r -p "Where should task-memory store tasks? [~/task-memory] " dir
    dir="${dir:-$HOME/task-memory}"
  fi
  dir="${dir/#\~/$HOME}"
  case "$dir" in /*) ;; *) echo "error: path must be absolute: $dir" >&2; exit 1 ;; esac
  mkdir -p "$dir"
  echo "TASK_MEMORY_DIR=$dir" > "$cfg"
  echo "wrote $cfg"
else
  echo "keep  $cfg ($(cat "$cfg"))"
fi
