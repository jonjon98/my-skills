#!/usr/bin/env bash
# Install or remove throwaway config.env files for the ship eval sandboxes.
#   config.sh on   write test configs, only where no config.env exists yet
#   config.sh off  remove only the configs this script wrote
set -euo pipefail
ship="$HOME/.agents/skills/ship"
case "${1:-}" in
  on)
    for d in "$ship"; do
      if [ -e "$d/config.env" ]; then echo "keep  $d/config.env (not ours)"; continue; fi
      cp "$d/config.env.example" "$d/config.env"
      touch "$d/.eval-config"
      echo "wrote $d/config.env"
    done
    if [ -e "$ship/.eval-config" ]; then
      sed -i '' -e 's/^FORGE=.*/FORGE=github/' -e 's/^FORGE_ACCESS=.*/FORGE_ACCESS=cli/' \
        -e 's/^CI_GRACE_SECONDS=.*/CI_GRACE_SECONDS=5/' -e 's/^CI_WAIT_MINUTES=.*/CI_WAIT_MINUTES=1/' "$ship/config.env"
    fi ;;
  off)
    for d in "$ship"; do
      if [ -e "$d/.eval-config" ]; then rm -f "$d/config.env" "$d/.eval-config"; echo "removed $d/config.env"; fi
    done ;;
  *) echo "usage: config.sh on|off" >&2; exit 2 ;;
esac
