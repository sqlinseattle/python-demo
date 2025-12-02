"""
Simple Bitcoin price fetcher.
Uses CoinGecko public API to get current BTC price in USD.
"""
from typing import Optional

import requests

COINGECKO_SIMPLE_PRICE = (
    "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
)


def get_btc_price_usd() -> Optional[float]:
    """Return the current Bitcoin price in USD rounded to 2 decimal places.

    Returns None on failure.
    """
    try:
        resp = requests.get(COINGECKO_SIMPLE_PRICE, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        # Expected shape: {"bitcoin": {"usd": 12345.67}}
        price = data.get("bitcoin", {}).get("usd")
        if price is None:
            return None
        return round(float(price), 2)
    except Exception:
        return None
