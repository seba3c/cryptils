from __future__ import annotations

from typing import Any


class PydanticMixin:
    """Mixin providing Pydantic v2 validation and serialization support.

    Uses lazy imports so that Pydantic remains an optional dependency.
    """

    @classmethod
    def _pydantic_validate(cls, value: Any, /) -> Any:
        from ._core import CryptoAmount

        if isinstance(value, cls):
            return value
        if isinstance(value, CryptoAmount):
            raise ValueError(f"Expected {cls.__name__}, got {type(value).__name__}")
        if isinstance(value, (str, int, float)):
            return cls(value)
        from decimal import Decimal

        if isinstance(value, Decimal):
            return cls(value)
        raise ValueError(
            f"Expected str, int, float, Decimal or {cls.__name__}, got {type(value).__name__}"
        )

    def _pydantic_serialize(self, /) -> str:
        return f"{self._value:.{self._decimals}f}"

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler: Any) -> Any:
        from pydantic_core import core_schema

        return core_schema.no_info_after_validator_function(
            cls._pydantic_validate,
            core_schema.any_schema(),
            serialization=core_schema.plain_serializer_function_ser_schema(
                cls._pydantic_serialize,
            ),
        )

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: Any, handler: Any) -> Any:
        json_schema = handler(core_schema)
        json_schema["type"] = "string"
        json_schema["description"] = f"{cls._name} amount as a string"
        return json_schema
