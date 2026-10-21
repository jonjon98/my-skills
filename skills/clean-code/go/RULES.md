# Go rules

These extend `../SKILL.md`. The core hard rules apply in full. The Go conventions below follow Effective Go and the Go Code Review Comments guide.

## Baseline

- Run `gofmt` on every changed file. Never hand-format against it.
- Name by role, not by type: `users`, not `userList`. Use short names only for short scopes, such as a loop index or a receiver.
- Keep exported names clear without the package name in them. Write `user.New`, not `user.NewUser`, when the package is `user`.
- Give every exported identifier a doc comment that starts with its name. This is the one comment convention Go expects, because tooling reads it.

## Explicit over compact

- Handle errors as named steps. Check each error where it occurs and return early, so the happy path stays at the left margin:

  ```go
  config, err := loadConfig(path)
  if err != nil {
      return fmt.Errorf("load config %s: %w", path, err)
  }
  ```

- Wrap errors with `%w` and a short description of the step that failed.
- Do not `else` after a `return`. The return already ends the branch.
- Avoid long method chains and nested function literals. Name the intermediate value instead.
- Avoid named return values except in very short functions, where they document a result the signature cannot otherwise show.
- Avoid `init()` for real work. Put setup in a named function that the caller invokes.

## Phases in code

A function that validates, finds, branches, and collects should read in that order:

```go
func LoadDependencies(nodeID string, graph Graph) ([]Node, error) {
    if err := validateNodeID(nodeID); err != nil {
        return nil, err
    }
    node, err := findFirstNode(graph, nodeID)
    if err != nil {
        return nil, err
    }

    if node.IsSingle() {
        return collectSingleDependencies(node, graph)
    }
    return collectMultiDependencies(node, graph)
}
```

The branch sits in one place. Each helper holds its own detail.
