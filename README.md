## Data Pipeline

1. GitHub Actions triggers at 9AM ET on weekdays
2. `fetch_sectors.py` pulls 1 year of adjusted closing prices via `yfinance`
3. Prices are normalized to an index of 100 at the earliest available date
4. Output is written to `data/sectors.csv` in long format and committed to the repo
5. Observable fetches the raw CSV URL on load — no build step required

## CSV Schema

| Column | Description |
|--------|-------------|
| Date | Trading date (YYYY-MM-DD) |
| ticker | ETF ticker symbol |
| indexed_value | Price indexed to 100 at start of trailing year |
| sector | Full sector name |

## Observable Notebook Features

- **Line chart** — rolling indexed returns by sector with interactive time window toggle (30D / 90D / 180D / 1Y)
- **Bar chart** — total period return ranked by sector, with positive/negative color encoding
- **Correlation heatmap** — Pearson correlation matrix of daily returns across all 11 sectors
- **Monthly returns heatmap** — sector returns by calendar month, colored by magnitude
- Link: https://observablehq.com/@robertmreedy/sp-500-sector-performance

## Tech Stack

- **Python** — yfinance, pandas
- **GitHub Actions** — scheduled daily cron
- **Observable Plot** — all chart visualizations
- **D3** — data loading and parsing

## Local Development

```bash
pip install yfinance pandas
python scripts/fetch_sectors.py
```

Outputs `data/sectors.csv` locally. Commit and push to trigger the live notebook update.

## Data Source

Adjusted closing prices via [Yahoo Finance](https://finance.yahoo.com) using the `yfinance` Python library. Data is for informational and portfolio purposes only, not investment advice.
