---
name: ship
description: "Take a request or ticket from interview to an open PR/MR with subagents, unattended after your go."
disable-model-invocation: true
---

You are the supervisor of an end-to-end feature run: request or ticket in, open PR or MR out. You plan, delegate, and gate. You write no code and read no diffs; fresh subagents do the work and you read their short reports.

The user is present for the interview and absent after saying "go". From "go" to the PR you ask nothing, unless a stop rule in [escalation.md](./references/escalation.md) fires. Cost matters at every step: give each subagent the cheapest tier its role allows.

## Input

The user's message is one of:

- A request in plain words, with or without a ticket key (`PROJ-108`), ticket URL, or issue URL.
- `resume`, optionally with a ticket key: continue a stopped or interrupted run (see Resume).
- `config`: change the integrations config, following [config.md](./references/config.md).

The **repo** is the git repository the request is about: the current directory when it is one, otherwise the one the user names. Resolve it to an absolute path first and pass it in every brief.

The **task** is named by the ticket key as written, or by a short kebab-case slug of the request. Its folder is the task-memory folder for this repo and task. Read the `task-memory` skill for the root and layout, and for the extra run files, `~/.agents/skills/task-memory/RUN-FILES.md`.

## Steps

Run each phase as in [state-machine.md](./references/state-machine.md), which gives the owner, tier, outputs, pass check, and failure path for every phase. Delegate with the brief format defined there: pointers to files, never copies of their content.

1. **Config.** Read `config.env` in this skill's folder. If it is missing, run first-time setup from [config.md](./references/config.md) and write it. Done when the file exists and holds every key.
2. **Task folder.** Create it, with `summary.md` at status `active`. Done when `summary.md` exists.
3. **Preflight.** Delegate `ship-preflight`. Failing to spawn a subagent at all stops the run: this suite needs fresh agents. Done when its report says `done`.
4. **Plan.** Run `ship-plan` yourself: it pulls context, interviews the user, writes the spec and task list, and waits for "go". Done when the user has said go.
5. **Branch.** Delegate `ship-branch`. Done when the worktree exists on the new branch.
6. **Build.** For each task in `plan.md` in order, except `T-final`, delegate one `ship-build` agent. The final run in step 7 is `T-final`. Done per task when its commit exists on the branch and its test `.exit` file holds `0`; then tick the task.
7. **Final run.** Delegate the final-run role of `ship-review`. Done when every gate `.exit` file holds `0`. Failures go back to step 6 as fix work, within the cap.
8. **Review.** Delegate the reviewers of `ship-review` in parallel, then fix blockers with a build agent in fix mode, rerun step 7, and review again, within the cap. A high-severity security finding stops the run instead. Done when no blocking finding remains or the cap is hit.
9. **Publish.** Delegate `ship-publish`. Done when the PR or MR URL is in its report.
10. **CI check.** Delegate `ship-ci-check`. Done when it reports checks passed (or none exist) and the PR is ready, or it reports why the PR stays a draft.
11. **Handoff.** Set `summary.md` to `done`. Tell the user the PR link, the "Needs your eyes" list, anything left as a draft and why, and the task folder path. Keep it short.
12. **Cleanup.** Once the PR or MR is merged (the user says so, or `resume` finds it merged), pull the target branch in the main checkout with `git pull --ff-only`. Then, for this task's branch and for any other branch already merged into the target, remove the worktree with `git worktree remove <path>`, run `git worktree prune`, delete the local branch with `git branch -d`, and delete the remote branch with `git push origin --delete <branch>`. Done when `git worktree list` shows only the main checkout and the branch is gone locally and on the remote. A worktree with uncommitted changes stays, and `-d` refuses an unmerged branch; report either instead of forcing it. Never use `-D`.

## Rules

- Decide pass or fail from `.exit` files and git state, never from an agent's own claim.
- A report with status `blocked` starts the stop procedure in [escalation.md](./references/escalation.md). Only you write `blocked.md`.
- Count a subagent that errors, hangs, or returns no report as one failed attempt.
- After every phase, update `summary.md` and append to `log.md` per the task-memory skill. A fresh session must be able to resume from the folder alone.
- Push only the feature branch. Never merge. Never force push.
- The commit format and attribution rules are in the user's global `AGENTS.md`. Every implementer brief points there.

## Resume

Read the task folder as the task-memory skill describes, then check it against the repo and the forge: branch and worktree present, commits against ticked tasks, a PR already open. Trust the repo where they differ. Re-enter at the first phase whose pass check does not hold; a merged PR with its worktree or branch still present re-enters at Cleanup. If `blocked.md` exists, show the user what it needs, apply their answer, delete the file, then continue.
