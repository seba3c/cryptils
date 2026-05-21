from __future__ import annotations

from typing import Any

from ._core import CurrencyAmount
from ._currency import Currency


class CryptoAmount(CurrencyAmount):
    def __init__(self, value: Any) -> None:
        if type(self) is CryptoAmount:
            raise TypeError("CryptoAmount is an abstract class and cannot be instantiated")
        super().__init__(value)


class BTCAmount(CryptoAmount):
    _currency = Currency.BTC


class ETHAmount(CryptoAmount):
    _currency = Currency.ETH


class USDCAmount(CryptoAmount):
    _currency = Currency.USDC


class USDTAmount(CryptoAmount):
    _currency = Currency.USDT
