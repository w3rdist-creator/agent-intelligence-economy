# Example: Clipping to Skill

## Raw clipping claim

A blog post says teams improve agent reliability by keeping small procedural playbooks and updating them after failures.

## Extraction

Reusable procedure: after a failed or difficult run, patch the nearest existing skill with the smallest instruction that would prevent the failure next time.

## Candidate patch

Target: `bounded-skill-optimization`

Patch: “Prefer patching an existing umbrella skill over creating a narrow new skill when the lesson applies to an existing task class.”

## Decision

Accepted. This changes future behavior and avoids skill sprawl.
