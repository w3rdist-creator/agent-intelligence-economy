# Example: Bounded Agent Lab Run

Objective: improve clipping classification accuracy.

Allowed mutation surface: `classifier_rules.md` only.

Evaluator: 30 held-out clipping examples with expected disposition labels.

Budget: 3 attempts or 30 minutes.

Score: exact label accuracy plus penalty for over-promoting to skill.

Result: keep if score improves by at least 5 percentage points without increasing false promotions.
