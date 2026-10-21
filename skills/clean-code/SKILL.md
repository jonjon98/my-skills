---
name: clean-code
description: Clean, readable code standards for writing, changing, or reviewing code in any language. Use when writing new code, editing existing code, reviewing a diff, or when the user asks about clean code, coding standards, or good practice.
---

Write code as a story a reader can follow from top to bottom. Names and structure carry the meaning, so comments are the exception.

## Hard rules

These always apply.

1. **Explicit over clever.** Name every step with a value or function that says what it means. Code should read like a story, not a puzzle.
2. **One level of complexity per function.** Every line in a function works at the same level. Branch in one place only, with at most one level of conditional nesting.
3. **Functions read as ordered phases.** For example: validate, locate, branch by kind, collect. Each phase is one named step, so the function reads like its outline.
4. **Comments only for what code cannot say.** Keep a comment only for a public contract the signature cannot express, a non-obvious constraint, a deprecation notice, or a link to an external bug or spec behind a workaround. Otherwise rename or restructure.
5. **Known bugs are not comments.** Fix a known bug, or raise a ticket for it. Never leave a note describing a known bug in the code.

## Soft rules

Apply these with judgement. Break one only when readability or maintainability clearly wins.

- **Avoid nested `if`s.** Pull the inner condition into a named variable or function, or return early. Nesting clusters code and hides its shape.
- **Keep expressions simple.** An expression holds at most one comprehension or call chain and two operations. Split anything denser into named steps.
- **Do not expand simple code.** A one-line return stays one line. Do not wrap it in a function just to name it.
- **Name for the reader.** A name says what a value means, not how it is computed. A longer clear name beats a short cryptic one.
- **Keep functions readable at a glance.** If a function needs scrolling to follow, split it along its phases.
- **Say each thing once (DRY).** Every piece of knowledge has one authoritative place. When the same rule appears twice, move it into one named function or constant. Do not merge two similar-looking pieces that change for different reasons, because the merge couples them.
- **Keep parts independent (orthogonal).** Each module does one job and changes for one reason. A module uses another only through its public interface, never through its internal details. Changing a payment provider should not require changes to the invoice total logic.

## Breaking a soft rule

State the reason in one line in your reply to the user. If a pull request is open, also add a line comment on that line in the PR with the same reason, so the reviewer can accept or reject it. Do not add a code comment for it.

## Working method

- Read the repo's own conventions first. Where its standards file (such as `CODING_STANDARDS.md` or `CONTRIBUTING.md`) conflicts with this skill, the repo wins.
- Match the surrounding style where the repo is consistent, unless that style breaks a hard rule.
- Before you finish, reread every changed function as a story. Fix any unnamed step or any function that mixes levels.

## Language rules

Load the matching file for language-specific rules:

- Python: `python/RULES.md`
- Go: `go/RULES.md`
- TypeScript and JavaScript: `typescript/RULES.md`
- React: `react/RULES.md`
- Vite: `vite/RULES.md`
- Java: `java/RULES.md`
- Spring Boot: `spring-boot/RULES.md`
