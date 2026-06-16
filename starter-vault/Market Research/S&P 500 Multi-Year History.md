---
type: market-history
status: seed
source: Yahoo Finance chart API ^GSPC
retrieved: 2026-06-16
instrument: S&P 500 Index
symbol: ^GSPC
price_basis: index close, not total return
---
# S&P 500 Multi-Year History

This is a sanitized public starter note derived from daily S&P 500 index closes via the Yahoo Finance chart API. It is included so the market research layer is not blank.

## Data files

- `Data/sp500_annual_history.csv` — annual close-to-close returns, year high/low, and within-year drawdown from year high.
- `Data/sp500_decade_summary.csv` — decade-level compound/annualized summaries.

## Coverage

- First year in snapshot: 1927 ending 1927-12-30 at 17.6600.
- Latest year in snapshot: 2026 through 2026-06-12 at 7431.4600.
- Best close-to-close year in this snapshot: 1954 at 45.02%.
- Worst close-to-close year in this snapshot: 1931 at -47.07%.

## How to use this history

Use the data to ask better questions:

- What regime was the market in: inflation shock, war, productivity boom, valuation reset, credit crisis, policy rescue, platform/network expansion, AI capex cycle?
- Was a drawdown valuation-driven, earnings-driven, liquidity-driven, policy-driven, or exogenous shock-driven?
- Did the index recover through earnings growth, multiple expansion, inflation, policy support, or sector rotation?
- What would have falsified the bullish or bearish thesis at the time?

## Guardrails

- This is not total-return data; dividends are excluded.
- Yahoo Finance data can revise. Re-run the fetch script if precision matters.
- Historical analogies are hypotheses, not forecasts.
- Do not turn this into live-trading advice.

## Next source upgrades

- Add total-return index data from a licensed/public source if available.
- Add CPI-adjusted real returns.
- Add earnings, valuation, rates, recession, and drawdown regime overlays.
- Add primary-source or source-of-record citations for major market events.
