# Vite rules

These extend `../SKILL.md` and `../typescript/RULES.md`.

- Expose client environment variables only with the `VITE_` prefix, and read them through `import.meta.env` in one config module. Do not read them ad hoc across the codebase.
- Never put a secret in a `VITE_` variable. Anything with that prefix ships to the browser.
- Keep `vite.config.ts` short. Put any plugin logic in a named function in its own file.
