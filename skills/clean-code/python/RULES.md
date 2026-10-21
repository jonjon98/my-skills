# Python rules

These extend `../SKILL.md`. The core hard rules apply in full.

## Baseline

- Follow PEP 8 for layout and naming: `snake_case` for functions and variables, `PascalCase` for classes, lines under 100 characters.
- Add type hints to every public function and method. Let the hints carry the parameter and return contract, so a docstring is needed only for behaviour the hints cannot express.

## Explicit over compact

- Prefer a plain `for` loop with a named result over a nested comprehension.

  ```python
  active_users = [user for user in users if user.is_active]
  ```

  is fine. This is not:

  ```python
  names = [item.name for group in groups for item in group.items if item.enabled and item.name]
  ```

  Write the second as named steps:

  ```python
  enabled_items = [item for group in groups for item in group.items if item.enabled]
  names = [item.name for item in enabled_items if item.name]
  ```

- Avoid `lambda` inside `map`, `filter`, or `sorted` when a named function reads better.
- Avoid chained conditional expressions. Use `if` statements with names.
- Avoid assignment expressions (`:=`) inside comprehensions or calls.
- Do not stack decorators, context managers, and comprehensions on one line.

## Phases in code

A function that validates, finds, branches, and collects should read in that order:

```python
def load_dependencies(node_id: str, graph: Graph) -> list[Node]:
    validate_node_id(node_id)
    node = find_first_node(graph, node_id)

    if node.is_single:
        return collect_single_dependencies(node, graph)
    return collect_multi_dependencies(node, graph)
```

The branch sits in one place. Each helper holds its own detail.
