---
name: ship-plan
description: "Ship phase: pull context, interview the user on the gaps, write the spec and task list, wait for go. Run by the ship supervisor itself."
---

Turn a request into a spec and a task list that agents can build without you. You run this in the main session, because the user answers here. The user is present for this phase and absent after it.

Your brief, or the `ship` supervisor, gives the task folder. Read `config.env` in the `ship` skill folder (`~/.agents/skills/ship/config.env`).

## 1. Pull context

When no ticket was given and `TRACKER`, `DOCS_SOURCE` and `CHAT_SOURCE` are all `none`, skip the agent: add `- nothing configured to pull` under "Pulled" in `context.md` and go on. Otherwise delegate to one fresh cheap-tier agent, with a brief that points at [CONTEXT-PULL.md](./CONTEXT-PULL.md) and the task folder. It writes `context.md`. Do the interview prep while it runs. Done when `context.md` lists what was pulled and what failed.

## 2. Interview

Call the `grilling` skill (`~/.agents/skills/grilling/SKILL.md`; read and follow it if you cannot call skills by name) on the request and `context.md`. These rules sit on top of it:

- Look facts up yourself, in the code and in `context.md`. Put only decisions to the user.
- Skip any question the ticket, docs, or chat already answers. Record what you inferred and from where, so the user can correct it in step 4.
- Report anything in `context.md` under "Failed to pull" in the first round, so the user can supply it.
- Settle each of these, by inference where the sources give it and by question where they do not: acceptance criteria that can be checked from a shell or by reading code, what is out of scope, what is off limits, the task type (feat, fix, chore, docs, test, build), the target branch, the commands that verify the work, and the ticket to link.

Done when the frontier is empty: every decision settled or inferred with its source.

## 3. Write the spec and the task list

Write `spec.md` in the format in `~/.agents/skills/task-memory/RUN-FILES.md`. Add the task type to its Logistics.

Write `plan.md` as the task list, one line per task:

```
- [ ] T1: <title> | criteria: A1, A2 | files: <expected files, a rough list>
```

Rules for the list:

- Each task is a thin vertical slice that is checkable on its own and fits one fresh agent context.
- Do any prefactoring first.
- Every acceptance criterion appears under at least one task.
- The last task is always `T-final: acceptance`. The final-run role of `ship-review` performs it, never a build agent. No code change belongs in it.

Done when every criterion is covered by a task.

## 4. Summarise and wait for go

Post a short summary to the user: the goal, the acceptance criteria, the task titles, the logistics, and every inferred item with its source. Say that after "go" you will ask nothing unless something stops the run. Wait for the user to say go. Apply any correction they give to `spec.md` and `plan.md`, and ask again.

Done when the user has said go. Log it in `log.md`.
