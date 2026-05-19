from __future__ import annotations

from .core import CryptoAmount


class BTC(CryptoAmount):
    _name = "Bitcoin"
    _symbol = "BTC"
    _decimals = 8
