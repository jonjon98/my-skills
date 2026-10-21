# TypeScript and JavaScript rules

These extend `../SKILL.md`. The core hard rules apply in full. This file covers TypeScript and JavaScript. Where a project is plain JavaScript, the same rules apply with the type annotations left out. React and Vite have their own files: `../react/RULES.md` and `../vite/RULES.md`.

## Baseline

- Turn on `strict` in `tsconfig.json`. Do not weaken it to make an error go away.
- Use `const` by default. Use `let` only when the value is reassigned, and never `var`.
- Use ES modules (`import` and `export`). Name each export for what it is.
- Prefer named exports over default exports, so every import reads the same name the module defines.
- Give exported functions an explicit return type, so the contract is readable without opening the body.

## Types

- Do not use `any`. Use `unknown` for input you have not checked yet, then narrow it with a named guard function.
- Model data with `type` or `interface` names that describe the domain, such as `Invoice` or `CartLine`, not `Data` or `Obj`.
- Use a discriminated union for values with variants, and branch on the tag in one `switch`:

  ```ts
  type Payment =
    | { kind: "card"; last4: string }
    | { kind: "bank"; iban: string };

  function describePayment(payment: Payment): string {
    switch (payment.kind) {
      case "card":
        return `Card ending ${payment.last4}`;
      case "bank":
        return `Bank account ${payment.iban}`;
    }
  }
  ```

- Avoid type assertions (`as`) except at a boundary you can check. Parse external data with a validator instead.

## Explicit over compact

- Name each intermediate value instead of chaining array methods on one line:

  ```ts
  const enabledItems = items.filter((item) => item.enabled);
  const names = enabledItems.map((item) => item.name);
  ```

  Avoid chains of three or more calls, and nested callbacks.

- Avoid nested ternaries. Use an `if` with a named result, or a lookup object.
- Avoid immediately invoked functions and clever destructuring inside parameters when a named step reads better.

## Comments

- Keep the comment rules from the core skill. TypeScript types and names carry the contract, so JSDoc is needed only for behaviour the types cannot express.
