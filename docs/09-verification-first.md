# Verification First

Prefer deterministic checks before model opinions.

Useful checks:

- path existence and expected sections
- `git diff --check`
- added-line secret scan
- wikilink validation
- CSV parse/width checks
- JSON/YAML schema checks
- tests/linters for code
- source URL/provenance checks
- hash rechecks
- remote HEAD verification after push

Never write “verified” unless a check actually ran or a caveat explicitly says what was not verified.
