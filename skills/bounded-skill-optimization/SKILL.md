---
name: bounded-skill-optimization
description: Improve agent skills and runbooks through evidence-backed, bounded, validated patches.
version: 0.1.0
---

# Bounded Skill Optimization


Trigger after difficult sessions, repeated failures, useful source harvests, cron reviews, or stale skill behavior.

Loop:
observed run evidence -> recurring success/failure pattern -> localized candidate edit -> validation gate -> accepted patch or rejected-edit record -> later review.

Acceptance criteria:
- grounded in observed evidence;
- reusable across future runs;
- smaller than the problem it prevents;
- belongs in this artifact;
- not a stale one-off fact;
- does not loosen safety or privacy boundaries.
