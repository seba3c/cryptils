from __future__ import annotations

from .core import CryptoAmount


class ETH(CryptoAmount):
    _name = "Tether"
    _symbol = "USDT"
    _decimals = 6
