# Market Research Starter

The starter vault includes a public research-only market layer so agents have more than blank templates when reasoning about financial history.

## Included seed data

- `starter-vault/Market Research/Data/sp500_annual_history.csv`
- `starter-vault/Market Research/Data/sp500_decade_summary.csv`
- `starter-vault/Market Research/S&P 500 Multi-Year History.md`

The S&P 500 snapshot is generated from Yahoo Finance chart API `^GSPC` daily closes. It is index-price history, not total return. Dividends are excluded.

## Why include this

Market research agents need historical base rates and regime context. Without data, they drift into narrative-only reasoning. A simple multi-year S&P 500 history lets them practice:

- regime classification;
- drawdown analysis;
- base-rate thinking;
- thesis falsification;
- separating historical analogy from forecast;
- recording non-trade conclusions.

## Guardrails

- Research-only; no live trading or broker actions.
- Historical returns are not trading signals.
- Prefer paper/calibration workflows over execution workflows.
- A market thesis should include source quality, exposure, valuation/liquidity, catalyst/timing, risk/reward, falsifier, and the option to do nothing.
