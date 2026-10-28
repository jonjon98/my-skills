---
name: git-workflow
description: Git rules for committing, branching, pushing, and opening pull requests in this user's repos. Use whenever you create a commit, create a branch, push, or open a PR or MR, or when the user says commit, push, branch, or PR.
---

Follow these rules for every git action. The user is the sole author of every commit and pull request.

## Branches

- Before you commit, check the current branch. If it is the default branch (usually `main`), create a branch first, named `<type>/<short-slug>`, such as `feat/terraform-clean-code`.
- Never push to the default branch unless the user asks you to.
- Never rewrite history on a branch that has been pushed. Use a new commit to fix it.

## Commits

- Commit only when the user asks for a commit, or as part of a task they asked you to finish.
- Write each message as `<type>: <summary>`. Types: `feat`, `fix`, `chore`, `docs`, `test`, `build`.
- Add a scope when it clarifies the change: `feat(auth): add login endpoint`.
- Mark a breaking change with `!`: `feat!: drop v1 endpoints`.
- The summary is lowercase, imperative, at most 72 characters, with no trailing period.
- Add a body after a blank line when the change needs its reason explained.
- Never add `Co-Authored-By` trailers, "Generated with" lines, or any other AI attribution.

## Staging

- Stage files by name. Do not use `git add -A` or `git add .`.
- Check `git status` before committing. Confirm no secret, `config.env`, or local file is staged.
- Group related changes into one commit, and keep unrelated changes in separate commits.

## Before pushing

- Check the author email on each commit when the repo is public. Use the GitHub noreply address for public repos.
- Check the diff for secrets, tokens, and personal details, such as real email addresses or ticket keys from a private project.

## Pull requests

- Open PRs with `gh pr create`, against the default branch.
- Write the body with the `pr` skill.
- Make the PR title follow the same `<type>: <summary>` format as the commit.
