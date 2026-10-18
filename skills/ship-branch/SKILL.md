---
name: ship-branch
description: "Create a named feature branch in its own git worktree from the target branch. Used by the ship supervisor, or when asked to start a branch."
---

Create the feature branch and its worktree. Your brief names the repo, the task folder, and where to write the report. Run git in the repo named by its `Repo` line. A standalone request names the ticket or task directly.

Read `config.env` in this skill's folder, `~/.agents/skills/ship-branch/config.env`. If it is missing, copy `config.env.example` beside it, ask the user for any value they want changed, and write it.

## Name the branch

Template, from config: `BRANCH_TEMPLATE`, default `{username}/{type}/{ticket}-{slug}`.

- **username**: `BRANCH_USERNAME`, or when empty the login of the forge account: see the "Your username" row of `~/.agents/skills/ship/references/forge-<forge>.md`.
- **type**: one of `feat`, `fix`, `chore`, `docs`, `test`, `build`, taken from the task type in `spec.md`. When the spec has none, infer it from the ticket type using `TYPE_MAP` in config. Refactors and cleanup are `chore`. Ask only when the ticket and spec give nothing.
- **ticket**: the key as written. With no ticket, drop `{ticket}-` from the template.
- **slug**: the ticket title or agreed task name, lowercased, ASCII, words joined by hyphens, cut to `BRANCH_SLUG_MAX` characters at a word boundary.

Example: `your-username/feat/PROJ-108-add-login-endpoint`.

## Create it

1. Read the target branch from `spec.md` logistics. Default to the repo's default branch.
2. Stop with trigger `collision` if the branch or its worktree path already exists.
3. Run `git fetch origin <target>`, then `git worktree add --no-track -b <branch> <worktree-path> origin/<target>`. The worktree path is `WORKTREE_DIR` from config joined with the branch name, hyphens replacing slashes. When `WORKTREE_DIR` is empty use `../<repo>.worktrees`.
4. In the worktree, confirm `git branch --show-current` prints the branch.

Done when step 4 confirms. Write the branch and worktree path into `spec.md` logistics and into `summary.md`, then write the report in the format in `~/.agents/skills/task-memory/RUN-FILES.md`.

To stop, follow "How a phase agent stops" in `~/.agents/skills/ship/references/escalation.md`.
