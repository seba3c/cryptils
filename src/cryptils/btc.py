from __future__ import annotations

from ._core import CryptoAmount


class BTC(CryptoAmount):
    _name = "Bitcoin"
    _code = "BTC"
    _decimals = 8
