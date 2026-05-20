from decimal import Decimal

import pytest
from pydantic import BaseModel, ValidationError  # noqa: E402

from cryptils import BTC, ETH, USDC, USDT


class WalletBalanceDetail(BaseModel):
    btc: BTC
    eth: ETH
    usdc: USDC
    usdt: USDT


class WalletBalance(BaseModel):
    timestamp: int
    wallet_id: str
    balances: WalletBalanceDetail


def _create_wallet(**kwargs):
    defaults = {
        "timestamp": 1234567890,
        "wallet_id": "wallet-1",
        "balances": {
            "btc": "1.5",
            "eth": "2.0",
            "usdc": "100",
            "usdt": "50.5",
        },
    }
    if "balances" in kwargs:
        defaults["balances"].update(kwargs.pop("balances"))
    defaults.update(kwargs)
    return WalletBalance(**defaults)


@pytest.mark.parametrize(
    "field, value, expected",
    [
        ("btc", "1.5", BTC("1.5")),
        ("btc", 1, BTC("1")),
        ("btc", 1.5, BTC("1.5")),
        ("btc", Decimal("1.5"), BTC("1.5")),
        ("btc", BTC("1.5"), BTC("1.5")),
        ("eth", "2.0", ETH("2.0")),
        ("eth", 2, ETH("2")),
        ("eth", Decimal("2.0"), ETH("2.0")),
        ("usdc", "100", USDC("100")),
        ("usdc", 100, USDC("100")),
        ("usdt", "50.5", USDT("50.5")),
        ("usdt", 50.5, USDT("50.5")),
    ],
)
def test_valid_inputs(field, value, expected):
    wallet = _create_wallet(balances={field: value})
    assert getattr(wallet.balances, field) == expected


def test_invalid_cross_currency():
    with pytest.raises(ValidationError) as exc_info:
        _create_wallet(balances={"btc": ETH("1.5")})
    assert "Expected BTC, got ETH" in str(exc_info.value)

    with pytest.raises(ValidationError) as exc_info:
        _create_wallet(balances={"eth": BTC("1.5")})
    assert "Expected ETH, got BTC" in str(exc_info.value)


@pytest.mark.parametrize(
    "field, value",
    [
        ("btc", []),
        ("btc", {}),
        ("btc", None),
        ("eth", []),
        ("usdc", None),
        ("usdt", {}),
    ],
)
def test_invalid_types(field, value):
    with pytest.raises(ValidationError) as exc_info:
        _create_wallet(balances={field: value})
    assert "Expected str, int, float, Decimal" in str(exc_info.value)


def test_serialization():
    wallet = _create_wallet()
    assert wallet.model_dump_json() == (
        '{"timestamp":1234567890,"wallet_id":"wallet-1",'
        '"balances":{"btc":"1.50000000","eth":"2.000000000000000000",'
        '"usdc":"100.000000","usdt":"50.500000"}}'
    )


def test_json_schema():
    schema = WalletBalance.model_json_schema()
    assert schema["properties"]["timestamp"]["type"] == "integer"
    assert schema["properties"]["wallet_id"]["type"] == "string"
    balances_ref = schema["properties"]["balances"]["$ref"]
    detail_key = balances_ref.split("/")[-1]
    balances_schema = schema["$defs"][detail_key]
    assert balances_schema["type"] == "object"
    for field, currency_name in [
        ("btc", "Bitcoin"),
        ("eth", "Ethereum"),
        ("usdc", "USD Coin"),
        ("usdt", "Tether"),
    ]:
        prop = balances_schema["properties"][field]
        assert prop["type"] == "string"
        assert f"{currency_name} amount as a string" in prop["description"]
