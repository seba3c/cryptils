from __future__ import annotations

from decimal import Decimal
from typing import ClassVar


class CryptoAmount:
    _symbol: ClassVar[str] = ""
    _decimals: ClassVar[int] = 0

    def __init__(self, value: str | int | Decimal) -> None:
        self._value = Decimal(value)

    @property
    def value(self) -> Decimal:
        return self._value

    def __str__(self) -> str:
        return f"{self._value:.{self._decimals}f} {self._symbol}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({str(self._value)})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._value == other._value

    def __hash__(self) -> int:
        return hash((self.__class__, self._value))

    def __add__(self, other: CryptoAmount) -> CryptoAmount:
        if not isinstance(other, self.__class__):
            raise TypeError(f"Cannot add {type(other).__name__} to {type(self).__name__}")
        return self.__class__(self._value + other._value)

    def __sub__(self, other: CryptoAmount) -> CryptoAmount:
        if not isinstance(other, self.__class__):
            raise TypeError(f"Cannot subtract {type(other).__name__} from {type(self).__name__}")
        return self.__class__(self._value - other._value)
