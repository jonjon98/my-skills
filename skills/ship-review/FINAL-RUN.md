# Final run

You are a fresh agent running the checks the build agents claimed pass. Trust nothing they reported. You are cheap and mechanical: run commands, save output, report exit codes.

Work only inside the worktree, on the branch in `spec.md`.

## Start clean

Before running anything, move every existing `artifacts/gate-*` and `artifacts/accept-*` file into `artifacts/final-run-<n-1>/`, where `n` is your attempt number. Skip this on attempt 1. Your run then starts with no `.exit` files, so a missing one means a check did not run, and an `.exit` left over from an earlier attempt can never pass this one.

## Gates

Read the verify commands in `spec.md` logistics, and the repo facts in `context.md`. Run each of these that exists: the full test suite, the typecheck, the lint, and the build. Save each with the artifacts pattern in `~/.agents/skills/task-memory/RUN-FILES.md`:

```bash
<command> > <task folder>/artifacts/gate-<name>.out 2>&1; echo $? > <task folder>/artifacts/gate-<name>.exit
```

## Acceptance checks

For each acceptance criterion in `spec.md`, run a check from the shell: run the command, call the endpoint, read the file. Save each as `artifacts/accept-<criterion>.out` and `.exit`, and a `.exit` of `0` means the criterion held.

A criterion that cannot be checked from a shell, such as visual layout, goes in the report under `## Needs your eyes`, with one line on what to look at. It does not fail the run.

## Report

Write `reports/final-run-<n>.md` in the format in `RUN-FILES.md`. In the summary, list each gate and criterion with its exit code, read from the `.exit` files. Status is `done` when every `.exit` file holds `0`, otherwise `failed`. Add the `## Needs your eyes` list.

Done when every gate and criterion has an `.exit` file or a place in the Needs your eyes list.
