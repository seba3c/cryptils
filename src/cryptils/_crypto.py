from __future__ import annotations

from typing import Any

from ._core import CurrencyAmount


class CryptoAmount(CurrencyAmount):
    def __init__(self, value: Any) -> None:
        if type(self) is CryptoAmount:
            raise TypeError("CryptoAmount is an abstract class and cannot be instantiated")
        super().__init__(value)


class BTCAmount(CryptoAmount):
    _name = "Bitcoin"
    _code = "BTC"
    _decimals = 8


class ETHAmount(CryptoAmount):
    _name = "Ethereum"
    _code = "ETH"
    _decimals = 18


class USDCAmount(CryptoAmount):
    _name = "USD Coin"
    _code = "USDC"
    _decimals = 6


class USDTAmount(CryptoAmount):
    _name = "Tether"
    _code = "USDT"
    _decimals = 6
