# Java rules

These extend `../SKILL.md`. The core hard rules apply in full. The Java conventions below follow the Google Java Style Guide, with the Clean Code book's advice on small, named steps.

## Baseline

- Format every changed file with the project's formatter (Spotless, google-java-format, or the IDE setting the repo uses). Never hand-format against it.
- Give classes and methods names that state their job, such as `InvoiceTotalCalculator` and `calculateTotal`. Avoid `Manager`, `Helper`, and `Util` as names for classes that hold logic.
- One top-level class per file, named after the file.
- Mark fields `final` unless they change. Mark local variables `final` when the code is clearer with it.

## Types and data

- Model plain data as a `record`, when the project's Java version supports it.
- Do not return `null` from a method. Return `Optional<T>` when absence is expected, or throw a named exception when it is an error.
- Do not use `Optional` for fields or parameters. Use it only as a return type.
- Use an enum for a fixed set of values, not string constants.

## Explicit over compact

- Name each step as a local variable. Avoid long stream chains. Three operations is the limit before you split the code into named steps:

  ```java
  List<Item> enabledItems = items.stream()
      .filter(Item::isEnabled)
      .toList();
  List<String> names = enabledItems.stream()
      .map(Item::name)
      .toList();
  ```

- Return early for invalid input and for the simplest case, so the main path stays at one level.
- Avoid nested ternaries. Use an `if` with a named variable.
- Never catch an exception and ignore it. Handle it, rethrow it with context, or log it once with the reason.
- Avoid `static` methods that hide dependencies. Pass dependencies in, so the code reads what it needs.

## Phases in code

A method that validates, finds, branches, and collects should read in that order:

```java
List<Node> loadDependencies(String nodeId, Graph graph) {
    validateNodeId(nodeId);
    Node node = findFirstNode(graph, nodeId);

    if (node.isSingle()) {
        return collectSingleDependencies(node, graph);
    }
    return collectMultiDependencies(node, graph);
}
```

The branch sits in one place. Each helper holds its own detail.

## Comments

- Keep the core comment rules. Public API classes and methods may carry Javadoc only when the name and types cannot express the contract.
