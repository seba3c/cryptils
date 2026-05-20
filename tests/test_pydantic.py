from decimal import Decimal

import pytest
from pydantic import BaseModel, ValidationError

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
    assert "Expected str, int, float, Decimal or BTC, got ETH" in str(exc_info.value)

    with pytest.raises(ValidationError) as exc_info:
        _create_wallet(balances={"eth": BTC("1.5")})
    assert "Expected str, int, float, Decimal or ETH, got BTC" in str(exc_info.value)


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
    schema = WalletBalanceDetail.model_json_schema()
    for field, c_name, c_code in [
        ("btc", "Bitcoin", "BTC"),
        ("eth", "Ethereum", "ETH"),
        ("usdc", "USD Coin", "USDC"),
        ("usdt", "Tether", "USDT"),
    ]:
        prop = schema["properties"][field]
        assert prop["title"] == f"{c_code} amount"
        assert prop["description"] == f"{c_name} amount as a string, int or float"
