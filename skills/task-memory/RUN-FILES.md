# Run files

Extra files a task folder gains when an orchestrator such as `ship` drives the task. Plain tasks never need them. The three core files (`summary.md`, `plan.md`, `log.md`) keep their meaning and stay the first thing any agent reads.

## Layout

```
<root>/<repo>/<task>/
  summary.md    # core
  plan.md       # core
  log.md        # core
  design.md     # optional: a confirmed design the task builds against
  spec.md       # what to build: goal, acceptance criteria, scope, logistics
  context.md    # material pulled in: ticket, comments, docs, what failed to load
  noticed.md    # one "Noticed:" line per out-of-scope finding
  blocked.md    # present only while the run is stopped
  reports/      # one file per phase attempt: <phase>-<n>.md
  artifacts/    # raw command output: <name>.out and <name>.exit
```

Create each file or folder only when something needs it.

## spec.md

```markdown
# Spec: <task title>

## Goal
One to three sentences.

## Acceptance criteria
- [ ] A criterion that can be checked from a shell or by reading code. One behaviour per line.

## Out of scope
- Things agreed not to touch.

## Logistics
- **Target branch:** main
- **Branch:** <name>
- **Ticket:** <key and url> or none
- **Verify commands:** the commands that prove the work
- **Off limits:** paths or systems not to change

## Decisions
- <decision made with the user>: <why>.
```

## context.md

```markdown
# Context

## Repo facts
- Commands: how to run tests, typecheck, lint, build; whether a test runner exists.
- PR or MR template: path, or none.
- Convention files: paths.

## Pulled
- <source>: <what it gave, one line>

## Failed to pull
- <source>: <error>. Or "none".
```

## reports/<phase>-<n>.md

Every phase writes one report per attempt, in this shape, so a supervisor can read status without reading work.

```markdown
# <Phase> report <n>

- **Status:** done | failed | blocked
- **Trigger:** <one trigger name from blocked.md below, only when Status is blocked>
- **Tier:** cheap | standard | strong
- **Updated:** YYYY-MM-DD

## Summary
One paragraph: what was done and what the result is.

## Artifacts
- <path>: what it holds

## Blockers
- What is needed to continue, or "none".
```

## artifacts/

Raw output of any gate or check, written by the command and never retyped by an agent:

```bash
<command> > artifacts/<name>.out 2>&1; echo $? > artifacts/<name>.exit
```

A check passed when its `.exit` file holds `0`. Read the `.exit` file, not the agent's report, to decide pass or fail.

## blocked.md

Written when a run stops for a person. Delete it when the run resumes.

```markdown
# Blocked: <one line>

- **Phase:** <phase and position, such as build, task 3 of 5>
- **Trigger:** ambiguity | retry cap | security | credentials | destructive step | scope growth | subagent failure | collision | ci failure
- **Rule hit:** <the cap or rule, with its value, such as "per-task attempts: 3">
- **Since:** YYYY-MM-DD

## What happened
Plain account of the stop.

## What was tried
- Each attempt, in one line.

## What is needed from you
The one question or action that unblocks the run.

## How to resume
The exact command or sentence to continue.
```

When writing it: set `summary.md` Status to `blocked`, point **Next step** at this file, and tell the user in chat the phase, the rule hit, and the path.
