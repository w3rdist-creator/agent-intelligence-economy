# Agent Intelligence Economy

A portable Obsidian + agent operating system for turning raw inputs into verified, reusable, token-efficient operational knowledge.

Most agent memory systems fail by confusing accumulation with intelligence. This kit teaches an agent to metabolize inputs: preserve sources, extract reusable procedures, verify claims, score loops, revise beliefs, and compress lessons into skills. Obsidian is the cold knowledge base; skills are executable compressed intelligence; ledgers are accountability; tokens are attention capital; recurring loops must earn the right to continue.

## Core loop

```text
CAPTURE -> ROUTE -> EXTRACT -> VERIFY -> SCORE -> PROMOTE / KILL -> COMPRESS -> LEARN
```

A useful output is not merely a generated note, report, branch, or idea. A useful output has a durable handle, enough provenance to revisit, verification results where possible, and a disposition: promoted, merged, killed, deferred, returned for rework, blocked, or superseded.

## What this repo gives you

- A starter Obsidian vault shape for clippings, sources, synthesis, ledgers, reports, and promotion candidates.
- Hermes-style skills for clipping harvest, skill optimization, token efficiency, verification, loop scoring, and bounded agent labs.
- Templates for source notes, canonical claims, mechanisms, belief revision, prediction ledgers, task packets, and two-layer reports.
- Small Python scripts for hash logging, clipping batch sweeps, compact verification, wikilink checking, loop scoreboard rendering, and belief-revision summaries.
- Doctrine documents explaining authority boundaries, context layering, tokenomics, truth-seeking, anti-bloat, and anti-patterns.

## Quick start

1. Copy `starter-vault/` into your Obsidian vault or use it as a reference.
2. Put raw web clips, PDFs, pasted notes, or exports in `Clippings/` or `Sources/`.
3. Run a clipping sweep:

```bash
python3 scripts/clipping_batch_sweep.py starter-vault/Clippings starter-vault/Ledgers/clippings_processing_log.csv starter-vault/Reports
```

4. Review the generated report. Promote only reusable procedures into skills/runbooks.
5. Track recurring automations in `starter-vault/Ledgers/loop_scoreboard.csv` and kill or tune loops that do not change decisions or artifacts.

## The four budgets

- Context budget: what enters the active prompt.
- Retrieval budget: what gets searched or loaded.
- Reasoning budget: which tasks deserve stronger models, tools, or review.
- Review budget: how much human/agent attention the output creates afterward.

A cheap report that creates 2,000 tokens of review debt is more expensive than an expensive pass that ships a verified artifact.

## Authority boundaries

- Obsidian/Git: durable truth and recovery.
- Raw clippings: source ore, not canon.
- Skills: compressed procedures that change future agent behavior.
- Memory: stable user/environment facts only.
- Scripts and ledgers: deterministic state and verification.
- Chat/Discord/Slack: cockpit and workbench, not source of truth.
- Sandbox vaults: pressure-test ideas; explicit promotion is required.
- Agents/workers: execute and review; they do not self-certify final truth.



## Install the skills into Hermes

This repository keeps skills in plain Hermes-style `SKILL.md` folders. A friend can use them in three ways:

### Option A — inspect/use as references

```bash
git clone https://github.com/<owner>/agent-intelligence-economy.git
cd agent-intelligence-economy
```

Read `docs/`, copy `starter-vault/`, and paste/adapt templates as needed.

### Option B — copy selected skills into a Hermes profile

```bash
PASTE HERE: HERMES_HOME_PATH
# Example: export HERMES_HOME=~/.hermes
mkdir -p "$HERMES_HOME/skills/agent-intelligence-economy"
cp -R skills/* "$HERMES_HOME/skills/agent-intelligence-economy/"
hermes skills list | grep -i intelligence || true
```

### Option C — install individual skill directories manually

Copy one folder from `skills/<name>/` into your Hermes skills directory, then start a fresh Hermes session and ask it to load that skill.

## Minimum viable workflow

1. Put source material in `starter-vault/Clippings/`.
2. Run `python3 scripts/clipping_batch_sweep.py ...`.
3. Review the report and classify each item.
4. Patch or create only reusable skills/runbooks.
5. Log rejected edits and already-absorbed items.
6. Score recurring loops weekly.
7. Promote only claims that survive objection/falsifier gates.

## Public launch note

This is an engine kit, not a private brain dump. It intentionally avoids personal project data, private financial details, raw chats, secrets, and local machine paths.

## Safety and privacy

This repo is sanitized. It does not include private vault contents, credentials, live trading logic, personal finance data, raw chats, or private project specifics. Treat market/trading examples as paper/research-only calibration patterns unless separately authorized with real risk controls.
