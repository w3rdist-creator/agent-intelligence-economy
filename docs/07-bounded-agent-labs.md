# Bounded Agent Labs

Useful autonomy needs a lab, not a vibe.

```text
program contract -> allowed mutation surface -> fixed budget -> objective score -> keep/discard/revert -> logged lesson -> next run
```

Rules:

- One mutation surface per run.
- Agent cannot edit its own evaluator.
- Fixed budget and stop condition.
- Objective score or explicit human review rubric.
- Crash/null/discard are valid outcomes.
- Complexity must justify itself.
