from __future__ import annotations

from abc import ABCMeta
from decimal import Decimal
from typing import Any, ClassVar, TypeAlias

_number_or_str: TypeAlias = Decimal | int | float | str


class CryptoAmount(metaclass=ABCMeta):  # noqa: B024
    _name: ClassVar[str] = ""
    _symbol: ClassVar[str] = ""
    _decimals: ClassVar[int] = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def symbol(self) -> str:
        return self._symbol

    def __init__(self, value: _number_or_str) -> None:
        self._value = self._to_decimal(value)

    def _to_decimal(self, value: _number_or_str) -> Decimal:
        return Decimal(value).quantize(Decimal(10) ** -self._decimals)

    def as_decimal(self) -> Decimal:
        return self._value

    def to_string(self):
        return f"{self._value:.{self._decimals}f} {self._symbol}"

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_string()})"

    def _is_compatible(self, other: Any) -> bool:
        return isinstance(other, _number_or_str)

    def _compare(self, other: Any) -> Decimal:
        if isinstance(other, self.__class__):
            return other._value
        if self._is_compatible(other):
            return self._to_decimal(other)
        return NotImplemented

    def __eq__(self, other: Any) -> bool:
        other_value = self._compare(other)
        if other_value is NotImplemented:
            return NotImplemented
        return self._value == other_value

    def __lt__(self, other: Any) -> bool:
        other_value = self._compare(other)
        if other_value is NotImplemented:
            return NotImplemented
        return self._value < other_value

    def __le__(self, other: Any) -> bool:
        other_value = self._compare(other)
        if other_value is NotImplemented:
            return NotImplemented
        return self._value <= other_value

    def __gt__(self, other: Any) -> bool:
        other_value = self._compare(other)
        if other_value is NotImplemented:
            return NotImplemented
        return self._value > other_value

    def __ge__(self, other: Any) -> bool:
        other_value = self._compare(other)
        if other_value is NotImplemented:
            return NotImplemented
        return self._value >= other_value

    def __hash__(self) -> int:
        return hash((self.__class__, self._value))

    def __add__(self, other: Any) -> CryptoAmount:
        if isinstance(other, self.__class__):
            return self.__class__(self._value + other._value)
        if self._is_compatible(other):
            return self.__class__(self._value + self._to_decimal(other))
        return NotImplemented

    def __radd__(self, other: Any) -> CryptoAmount:
        return self.__add__(other)

    def __sub__(self, other: Any) -> CryptoAmount:
        if isinstance(other, self.__class__):
            return self.__class__(self._value - other._value)
        if self._is_compatible(other):
            return self.__class__(self._value - self._to_decimal(other))
        return NotImplemented

    def __rsub__(self, other: Any) -> CryptoAmount:
        if self._is_compatible(other):
            return self.__class__(self._to_decimal(other) - self._value)
        return NotImplemented

    def __mul__(self, other: Any) -> CryptoAmount:
        if isinstance(other, self.__class__):
            raise TypeError(f"Cannot multiply two {type(self).__name__} instances")
        if self._is_compatible(other):
            return self.__class__(self._value * self._to_decimal(other))
        return NotImplemented

    def __rmul__(self, other: Any) -> CryptoAmount:
        return self.__mul__(other)

    def __truediv__(self, other: Any) -> CryptoAmount:
        if isinstance(other, self.__class__):
            raise TypeError(f"Cannot divide two {type(self).__name__} instances")
        if self._is_compatible(other):
            return self.__class__(self._value / self._to_decimal(other))
        return NotImplemented

    def __rtruediv__(self, other: Any) -> CryptoAmount:
        if self._is_compatible(other):
            return self.__class__(self._to_decimal(other) / self._value)
        return NotImplemented
