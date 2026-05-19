from __future__ import annotations

from .core import CryptoAmount


class USDC(CryptoAmount):
    _name = "USD Coin"
    _symbol = "USDC"
    _decimals = 6
