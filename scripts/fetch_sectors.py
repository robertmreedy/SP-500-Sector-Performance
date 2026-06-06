import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

SECTORS = {
    "XLK": "Technology",
    "XLF": "Financials",
    "XLV": "Healthcare",
    "XLE": "Energy",
    "XLI": "Industrials",
    "XLY": "Consumer Discretionary",
    "XLP": "Consumer Staples",
    "XLRE": "Real Estate",
    "XLB": "Materials",
    "XLU": "Utilities",
    "XLC": "Communication Services"
}

# Pull 1 year of data to support 30/90/180-day windows
end = datetime.today()
start = end - timedelta(days=365)

tickers = list(SECTORS.keys())
raw = yf.download(tickers, start=start, end=end, auto_adjust=True)["Close"]

# Normalize each ticker to 100 at the earliest available date
normalized = (raw / raw.iloc[0]) * 100

# Reshape to long format for Observable/D3
long_df = normalized.reset_index().melt(id_vars="Date", var_name="ticker", value_name="indexed_value")
long_df["sector"] = long_df["ticker"].map(SECTORS)
long_df["Date"] = long_df["Date"].dt.strftime("%Y-%m-%d")
long_df = long_df.dropna()
long_df = long_df.sort_values(["Date", "ticker"])

os.makedirs("data", exist_ok=True)
long_df.to_csv("data/sectors.csv", index=False)
print(f"Done — {len(long_df)} rows written to data/sectors.csv")
