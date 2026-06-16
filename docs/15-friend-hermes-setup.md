# Friend Hermes Setup

Use this when another Hermes user wants to try the kit.

## Clone

```bash
git clone https://github.com/<owner>/agent-intelligence-economy.git
cd agent-intelligence-economy
```

## Try the starter vault

```bash
cp -R starter-vault ~/Agent-Intelligence-Economy-Vault
```

Open that folder in Obsidian. Add a few Markdown clippings to `Clippings/`, then run:

```bash
python3 scripts/clipping_batch_sweep.py   ~/Agent-Intelligence-Economy-Vault/Clippings   ~/Agent-Intelligence-Economy-Vault/Ledgers/clippings_processing_log.csv   ~/Agent-Intelligence-Economy-Vault/Reports
```

## Install skills

Set the profile home explicitly so you do not copy into the wrong Hermes profile.

```bash
PASTE HERE: HERMES_HOME_PATH
# Example: export HERMES_HOME="$HOME/.hermes"
mkdir -p "$HERMES_HOME/skills/agent-intelligence-economy"
cp -R skills/* "$HERMES_HOME/skills/agent-intelligence-economy/"
```

Then start a fresh Hermes session and ask:

```text
Load the clippings-skill-harvester skill and process my Obsidian Clippings folder using the capture-to-output protocol.
```

## Recommended first three skills

1. `clippings-skill-harvester` — metabolize raw inputs.
2. `bounded-skill-optimization` — convert run evidence into skill patches.
3. `loop-scoreboard` — keep automations honest.

## Safety rails

- Do not point the sweep at private journals until you understand the report output.
- Do not turn every clipping into memory or a skill.
- Do not publish generated reports without reviewing source excerpts.
- Do not use market examples as trading advice.
