---
name: ship-review
description: "Ship phase: run all gates and acceptance checks, or review the diff as one lens. Used by the ship supervisor."
---

Two roles share this skill. Your brief names one, the task folder, the worktree, the attempt, and where to write the report. Read only the file for your role.

- **final-run**: run every gate and acceptance check and save the raw output. Read [FINAL-RUN.md](./FINAL-RUN.md). You edit nothing.
- **reviewer**, with a lens of `spec`, `quality`, or `security`: read the diff and report findings. Read [REVIEWERS.md](./REVIEWERS.md). You edit nothing.

Neither role fixes anything. Fixes go to a build agent in fix mode.
