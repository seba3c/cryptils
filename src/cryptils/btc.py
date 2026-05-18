from __future__ import annotations

from decimal import Decimal

from .core import CryptoAmount


class BTC(CryptoAmount):
    _symbol = "BTC"
    _decimals = 8

    def __init__(self, value: str | int | Decimal) -> None:
        super().__init__(value)
        self._value = self._value.quantize(Decimal("0.00000001"))

    def to_sats(self) -> Sats:
        return Sats(int(self._value * 10**8))


class Sats(CryptoAmount):
    _symbol = "sats"
    _decimals = 0

    def __init__(self, value: str | int | Decimal) -> None:
        super().__init__(int(Decimal(value)))

    def to_btc(self) -> BTC:
        return BTC(self._value / 10**8)
