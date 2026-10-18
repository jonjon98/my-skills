---
name: task-memory
description: Persist and resume task progress in a configured task-memory folder. Use when the user says "remember this", "task memory", "save progress", or "read from task memory", or when starting or resuming work on a ticket or task that may already have saved progress.
---

Task memory is a progress file for a task, kept outside the repo so it survives across sessions, agents, and worktrees. A fresh agent reading it should pick up the task cold, without the original conversation.

## Root

The root folder comes from `config.env` in this skill's folder (the base directory shown when the skill loads), a single line:

```
TASK_MEMORY_DIR=/absolute/path
```

Resolve the root before any read or write:

```bash
sed -n 's/^TASK_MEMORY_DIR=//p' "<skill base directory>/config.env"
```

If `config.env` is missing or the value is empty, ask the user for the root, write it to `config.env`, then continue. Below, `<root>` means this value.

## Layout

```
<root>/
  <repo>/
    <task>/
      summary.md   # read first: goal, status, current state, next step
      plan.md      # ordered checklist of steps
      log.md       # append-only, dated progress entries
```

An orchestrator that drives a task adds optional files (spec, context, reports, artifacts, and a blocked report). Read [RUN-FILES.md](./RUN-FILES.md) when a task folder holds them or when writing for such a run.

- **`<repo>`**: the repository name, taken from the main checkout so every worktree shares it:
  ```bash
  basename "$(dirname "$(git rev-parse --path-format=absolute --git-common-dir)")"
  ```
  Outside a git repo, use the basename of the working directory.
- **`<task>`**: a short kebab-case slug, or the name the user gives. When the task comes from a ticket, prefix the ticket ID as written: `ENG-123-fix-login-redirect`.
- Create any missing directory with `mkdir -p`.
- Write to the resolved absolute path, never relative to the working directory. After writing, confirm the file exists at that path.

## Reading

Read when the user asks, and on your own when starting or resuming work that may have memory: a ticket ID is mentioned, the current branch looks like a task, or the user says "continue" or "pick up where we left off".

1. List `<root>/<repo>/`. Match the task by ticket ID, then branch name (recorded in each `summary.md`), then slug. If several could match, ask which.
2. Read `summary.md`, then `plan.md`. Read `log.md` only for history behind a decision.
3. Check the recorded state against the repo (branch, recent commits, files named in the summary). Memory can go stale. Trust the repo where they disagree, and say what changed.
4. Tell the user in two or three lines what you found and the next step, then continue.

Done when you have reported the task's status and next step, or confirmed no memory exists for it.

## Writing

Create memory for a new task only when the user asks. Once a task has memory, keep it current yourself: update after each finished plan step, when a decision is made, and before ending a session that moved the task forward.

1. Resolve the task directory as above, creating it if missing.
2. Rewrite `summary.md` in place so it shows the present state, not history.
3. Update `plan.md`: tick finished steps, add or reorder steps as the plan changes.
4. Append one entry to `log.md` with today's date.

Done when a fresh agent reading only `summary.md` and `plan.md` would know what is done, what is next, and why.

Write the name of an env var or credential, never its value. Write absolute dates (`2026-10-16`), not "yesterday".

## File formats

### summary.md

```markdown
# <Task title>

- **Ticket:** ENG-123 (<url>) or none
- **Repo:** <repo>
- **Branch:** <branch> or none
- **Status:** active | blocked | done
- **Updated:** YYYY-MM-DD

## Goal
What "done" means for this task, in one to three sentences.

## Current state
Where things stand right now: what works, what is half-built, which files are in play.

## Next step
The single next concrete action.

## Decisions
- <decision>: <why>. Keep the reason; it is what a later agent cannot recover.

## Gotchas
- Traps hit along the way, non-obvious constraints, open questions.
```

### plan.md

```markdown
# Plan: <Task title>

- [x] Step already done
- [ ] Next step
- [ ] Later step
```

### log.md

Newest entry at the bottom. Each entry is a dated heading and a few bullets of what changed.

```markdown
## 2026-10-16
- Added the redirect guard in `auth/callback.ts`; tests pass.
- Decided to keep the legacy cookie for one release (see summary).
```

When the task is finished, set **Status** to `done` and leave the directory in place as a record. When a run stops for a person, set **Status** to `blocked` and write `blocked.md` as described in RUN-FILES.md.
