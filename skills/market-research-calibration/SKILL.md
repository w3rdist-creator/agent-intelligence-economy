---
name: market-research-calibration
description: Use public market-history data for research-only calibration, regime analysis, thesis review, and non-trade learning without live execution.
version: 0.1.0
---

# Market Research Calibration

Use when analyzing market history, market regimes, index drawdowns, or paper-only thesis reviews.

## Rules

1. Read source-of-record data first, not narrative memory.
2. Separate index price history from total-return history.
3. Treat analogies as hypotheses, not forecasts.
4. Include a falsifier and non-trade option for every thesis.
5. Prefer paper/calibration outputs over execution outputs.
6. No live trading, broker actions, wallet actions, or copy-trading.

## Starter data

The starter vault includes annual S&P 500 index history under:

`starter-vault/Market Research/Data/sp500_annual_history.csv`

Use it for base rates, drawdown questions, and regime prompts. Upgrade it with total-return, CPI, rates, earnings, and recession overlays before making stronger claims.
