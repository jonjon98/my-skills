# Sources

Where each rule set comes from. This file is for people reading the repo. No rules file links to it, so the agent does not load it during a run.

## Core (`SKILL.md`)

- *Clean Code*, Robert C. Martin: small functions, one level of abstraction, descriptive names, comments as a last resort.
- *The Pragmatic Programmer*, Andrew Hunt and David Thomas: DRY, orthogonality, and fixing broken windows.

## Python (`python/RULES.md`)

- [PEP 8, Style Guide for Python Code](https://peps.python.org/pep-0008/): layout, naming, and line length.

## Go (`go/RULES.md`)

- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments): error handling, naming, and doc comments on exported names.

## TypeScript and JavaScript (`typescript/RULES.md`)

- [TSConfig reference: strict](https://www.typescriptlang.org/tsconfig/strict.html): the `strict` flag and what it enables.

## React (`react/RULES.md`)

- [You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect): when `useEffect` is needed, and when to compute values in render or in event handlers.

## Vite (`vite/RULES.md`)

- [Env Variables and Modes](https://vite.dev/guide/env-and-mode): the `VITE_` prefix, and which variables reach the browser.

## Java (`java/RULES.md`)

- [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html): naming, formatting, and Javadoc.

## Spring Boot (`spring-boot/RULES.md`)

- [Spring Boot Configuration Binding](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-Configuration-Binding): constructor binding and `@ConfigurationProperties`.

## Terraform (`terraform/RULES.md`)

- [HashiCorp Terraform style guide](https://developer.hashicorp.com/terraform/language/v1.12.x/style): formatting, layout, and file names.
- [HashiCorp refactoring with moved blocks](https://developer.hashicorp.com/terraform/language/v1.7.x/modules/develop/refactoring): `moved` and `removed` blocks.
- [Gruntwork Terraform style guide](https://docs.gruntwork.io/guides/style/terraform-style-guide): the 120-column limit, snake_case labels, and concrete object types. Its folder layout and per-section comments are not used, because they conflict with the core comment rule.
- [Terraform skill by Anton Babenko](https://tessl.io/registry/skills/github/antonbabenko/terraform-skill/terraform-skill--terraform-skill): `count` versus `for_each`, and naming.
- [Terraform skill by bkircher](https://tessl.io/registry/skills/github/bkircher/skills/terraform): `nullable`, and `optional()` object fields.
