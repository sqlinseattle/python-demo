import sys

from get_btc_price import get_btc_price_usd


def test():
    price = get_btc_price_usd()
    if price is None:
        print("Skipped: no network/failed to fetch BTC price.")
        return 0

    assert isinstance(price, float) or isinstance(price, int)
    assert price > 0
    print(f"OK: BTC price is ${price}")
    return 0


if __name__ == "__main__":
    sys.exit(test())
