"""Print current Bitcoin price to console.

Usage:
    python print_btc.py
"""

from get_btc_price import get_btc_price_usd


def main() -> None:
    price = get_btc_price_usd()
    if price is None:
        print("Failed to fetch Bitcoin price.")
    else:
        print(f"Bitcoin price (USD): ${price}")


if __name__ == "__main__":
    main()
