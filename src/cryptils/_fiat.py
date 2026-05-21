from __future__ import annotations

from typing import Any

from ._core import CurrencyAmount
from ._currency import Currency


class FiatAmount(CurrencyAmount):
    def __init__(self, value: Any) -> None:
        if type(self) is FiatAmount:
            raise TypeError("FiatAmount is an abstract class and cannot be instantiated")
        super().__init__(value)


class USDAmount(FiatAmount):
    _currency = Currency.USD


class EURAmount(FiatAmount):
    _currency = Currency.EUR


class JPYAmount(FiatAmount):
    _currency = Currency.JPY


class GBPAmount(FiatAmount):
    _currency = Currency.GBP


class CNYAmount(FiatAmount):
    _currency = Currency.CNY


class AUDAmount(FiatAmount):
    _currency = Currency.AUD


class CADAmount(FiatAmount):
    _currency = Currency.CAD


class CHFAmount(FiatAmount):
    _currency = Currency.CHF


class HKDAmount(FiatAmount):
    _currency = Currency.HKD


class NZDAmount(FiatAmount):
    _currency = Currency.NZD
