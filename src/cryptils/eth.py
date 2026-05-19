from __future__ import annotations

from .core import CryptoAmount


class ETH(CryptoAmount):
    _name = "Ethereum"
    _symbol = "ETH"
    _decimals = 18
