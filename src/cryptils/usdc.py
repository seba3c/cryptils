from __future__ import annotations

from ._core import CryptoAmount


class USDC(CryptoAmount):
    _name = "USD Coin"
    _symbol = "USDC"
    _decimals = 6
