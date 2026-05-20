from __future__ import annotations

from abc import ABCMeta
from decimal import Decimal
from typing import Any, ClassVar, TypeAlias

from ._pydantic import PydanticMixin

_arithmetic_comparison_compatible: TypeAlias = Decimal | int | float
_instance_compatible: TypeAlias = _arithmetic_comparison_compatible | str


class CryptoAmount(PydanticMixin, metaclass=ABCMeta):  # noqa: B024
    _name: ClassVar[str] = ""
    _code: ClassVar[str] = ""
    _decimals: ClassVar[int] = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def code(self) -> str:
        return self._code

    def __init__(self, value: _instance_compatible) -> None:
        if type(self) is CryptoAmount:
            raise TypeError("CryptoAmount is an abstract class and cannot be instantiated directly")
        if type(value) is self.__class__:
            self._value = self._to_decimal(value.as_decimal())
        else:
            self._value = self._to_decimal(value)

    def _to_decimal(self, value: _arithmetic_comparison_compatible) -> Decimal:
        return Decimal(value).quantize(Decimal(10) ** -self._decimals)

    def to_decimal(self) -> Decimal:
        return self._value

    def to_string(self) -> str:
        return f"{self._code} {self._value}"

    def to_float(self) -> float:
        return float(self._value)

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_decimal()})"

    def _is_compatible(self, other: Any) -> bool:
        return isinstance(other, _arithmetic_comparison_compatible)

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
