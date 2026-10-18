# Config

`config.env` sits in this skill's folder and is git-ignored. It holds this machine's integrations and the run caps. `config.env.example` beside it lists every key with its default. It never holds a secret: access is by a logged-in CLI or a configured MCP server.

## First-time setup

When `config.env` is missing:

1. Detect what you can: the host of `git remote get-url origin`, whether `gh` or `glab` is installed and logged in, and which MCP servers the harness lists for tickets, docs, and chat.
2. Ask the user for the rest in one message, one line per group, offering the detected value as the default:
   - forge and how to reach it: CLI first, MCP second
   - ticket tracker, how to reach it, and which key prefixes belong to it
   - docs source, and chat source, each possibly none
   - the real model name for each of the three tiers, cheap, standard and strong
3. Write `config.env` from `config.env.example`. Leave unknown values empty and say which. Also copy `~/.agents/skills/ship-branch/config.env.example` to `config.env` there when it is missing, because a subagent cannot ask the user for it later.
4. If the user cannot answer something yet, write the key empty. A source with an empty value is skipped, and the context pull reports it as not configured.

## Editing later

The user may say "set X to Y", "add the docs source", and the like, to any agent. Edit `config.env` in place, keep the other lines, and confirm the changed line.

## Keys

See `config.env.example`. A caps key overrides the default caps in `state-machine.md`.
