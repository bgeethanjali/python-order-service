"""Pricing helpers (legacy Python 3.8 style)."""
from typing import List, Optional


def apply_discount(amount, percent=None):
    # type: (float, Optional[float]) -> float
    if percent is None:
        return amount
    return amount - (amount * (percent / 100.0))


def format_line(sku, qty, price):
    # type: (str, int, float) -> str
    return "%s x%d @ %.2f" % (sku, qty, price)


def sku_list(items):
    # type: (List[dict]) -> List[str]
    return [i["sku"] for i in items]
