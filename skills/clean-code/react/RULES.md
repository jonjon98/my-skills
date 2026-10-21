# React rules

These extend `../SKILL.md` and `../typescript/RULES.md`. Apply the TypeScript rules to all React code.

## Components

- Write function components only. One exported component per file, named the same as the file.
- Type props with a named `type` or `interface`, such as `UserCardProps`, and destructure them in the signature.
- Keep JSX to layout. Move every condition into a named variable above the `return`:

  ```tsx
  export function InvoiceStatus({ invoice }: InvoiceStatusProps) {
    const isOverdue = invoice.dueDate < today();
    const label = isOverdue ? "Overdue" : "Open";

    return <span className={isOverdue ? "text-red" : "text-grey"}>{label}</span>;
  }
  ```

- Return early for loading and error states, so the main render path stays at one level.
- Name each event handler for what it does, such as `handleSubmit`, and define it above the `return`.

## Hooks

- Keep hook calls at the top of the component, in the same order every render. Follow the rules of hooks without exception.
- Do not use `useEffect` to compute data from props or state. Compute it during render, or with `useMemo` only when a measured cost justifies it.
- Do not use `useEffect` to respond to a user action. Put the work in the event handler that the action triggers.
- Use `useEffect` only to sync with something outside React: a subscription, a timer, a DOM API, or a network request. Every effect cleans up what it starts and lists every value it reads in its dependency array.
- If an effect seems needed, first check whether the work belongs in an event handler, during render, or in a data-fetching library. Pick that first.
