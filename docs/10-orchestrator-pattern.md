# Orchestrator Pattern

Use the lightest adequate mode:

```text
direct tools -> deterministic script -> specialist worker -> reviewer -> scheduled loop
```

Rules:

- Source of truth first.
- Deterministic checks beat LLM opinions.
- Workers return handles: paths, diffs, test output, URLs, IDs, or no-change reports.
- Orchestrator verifies side-effect claims.
- Cull/defer/no-op are valid outcomes.
- Final integration decides accept, patch, defer, ask, or stop.
