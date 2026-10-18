---
name: ship-preflight
description: "Ship phase: check access, repo state, and collisions before the interview. Used by the ship supervisor."
---

Check that a `ship` run can start, before the user spends time on the interview. Run quickly, with shell commands, and decide nothing. Your brief names the repo, the task folder, and where to write the report. Run every git command in the repo named by its `Repo` line.

Read `config.env` in the `ship` skill folder (`~/.agents/skills/ship/config.env`) first.

## Checks

Run all of them and record each result. Done when every check has a result in the report.

1. **Repo.** The `Repo` path is a git repo with an `origin` remote. No merge or rebase is in progress. Run `git fetch origin`.
2. **Default branch.** Resolve it with `git symbolic-ref --short refs/remotes/origin/HEAD`.
3. **Forge access.** Use the command table for `FORGE` in `~/.agents/skills/ship/references/forge-<forge>.md`. With a CLI, confirm it is logged in. With an MCP, make one read call to the named server.
4. **Ticket access.** When the brief names a ticket, fetch it through `TRACKER_ACCESS` and record its key, title, and type. A tracker not configured, or unreachable, is recorded as such and does not fail this phase.
5. **Collisions.** Look for anything already covering the ticket key: `git branch -a --list "*<KEY>*"`, `git worktree list`, and open PRs found with the forge table's search row. Any hit fails this phase with trigger `collision`, naming the branch, worktree, or PR.
6. **Repo facts**, for the interview to confirm:
   - the commands that run tests, typecheck, lint, and build, read from `package.json` scripts, `Makefile`, `pyproject.toml`, `Cargo.toml`, `go.mod`, CI config, and the like; whether a test runner exists at all
   - a PR or MR template, if any
   - convention files: `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `CODING_STANDARDS.md`, and similar

## Output

Write the repo facts to `context.md` under a `## Repo facts` heading, in the task folder. Write the report in the format in `~/.agents/skills/task-memory/RUN-FILES.md`, status `done`, or `blocked` with the trigger when a check fails. When blocked, state the single fix the user must make.

To stop, follow "How a phase agent stops" in `~/.agents/skills/ship/references/escalation.md`.
