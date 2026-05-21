import pytest

from cryptils import (
    AUDAmount,
    CADAmount,
    CHFAmount,
    CNYAmount,
    EURAmount,
    GBPAmount,
    HKDAmount,
    JPYAmount,
    NZDAmount,
    USDAmount,
)


@pytest.mark.parametrize(
    ("amount_class", "name", "code", "decimals"),
    [
        (USDAmount, "US Dollar", "USD", 2),
        (EURAmount, "Euro", "EUR", 2),
        (JPYAmount, "Yen", "JPY", 0),
        (GBPAmount, "Pound Sterling", "GBP", 2),
        (CNYAmount, "Yuan", "CNY", 2),
        (AUDAmount, "Australian Dollar", "AUD", 2),
        (CADAmount, "Canadian Dollar", "CAD", 2),
        (CHFAmount, "Swiss Franc", "CHF", 2),
        (HKDAmount, "Hong Kong Dollar", "HKD", 2),
        (NZDAmount, "New Zealand Dollar", "NZD", 2),
    ],
)
def test_fiat_name_code_decimals(amount_class, name, code, decimals):
    instance = amount_class(0)
    assert instance.name == name
    assert instance.code == code
    assert instance.decimals == decimals


def test_usd_str():
    assert str(USDAmount("1.5")) == "1.50"
    assert str(USDAmount("1")) == "1.00"


def test_jpy_str():
    assert str(JPYAmount("150")) == "150"
    assert str(JPYAmount("150.5")) == "151"
    assert str(JPYAmount("149.4")) == "149"


def test_usd_to_string():
    assert USDAmount("1.5").to_string() == "USD 1.50"


def test_jpy_to_string():
    assert JPYAmount("150").to_string() == "JPY 150"


def test_usd_precision():
    assert USDAmount("1.004") == USDAmount("1.00")
    assert USDAmount("1.005") == USDAmount("1.01")


def test_jpy_precision():
    assert JPYAmount("1.4") == JPYAmount("1")
    assert JPYAmount("1.5") == JPYAmount("2")


def test_usd_addition():
    assert USDAmount("0.5") + USDAmount("0.5") == USDAmount("1.00")
    assert USDAmount("0.5") + 1 == USDAmount("1.50")
    assert 1 + USDAmount("0.5") == USDAmount("1.50")


def test_jpy_addition():
    assert JPYAmount("100") + JPYAmount("50") == JPYAmount("150")
    assert JPYAmount("100") + 50 == JPYAmount("150")


def test_usd_cross_class_arithmetic():
    with pytest.raises(TypeError):
        USDAmount("1") + EURAmount("1")
    with pytest.raises(TypeError):
        USDAmount("1") - EURAmount("1")


def test_usd_equality_with_same_class():
    assert USDAmount("1.50") == USDAmount("1.5")
    assert USDAmount("1.50") != USDAmount("2.00")


def test_jpy_equality_with_same_class():
    assert JPYAmount("150") == JPYAmount("150")
    assert JPYAmount("150") != JPYAmount("151")


def test_usd_comparison():
    assert USDAmount("1") < USDAmount("2")
    assert USDAmount("2") > USDAmount("1")
    assert USDAmount("1") <= USDAmount("1")
    assert USDAmount("1") >= USDAmount("1")


def test_jpy_comparison():
    assert JPYAmount("100") < JPYAmount("200")
    assert JPYAmount("200") > JPYAmount("100")
    assert JPYAmount("100") <= JPYAmount("100")
    assert JPYAmount("100") >= JPYAmount("100")


def test_usd_repr():
    assert repr(USDAmount("1.5")) == "USD(1.50)"


def test_jpy_repr():
    assert repr(JPYAmount("150")) == "JPY(150)"


def test_usd_hash():
    assert hash(USDAmount("1.50")) == hash(USDAmount("1.5"))


def test_jpy_hash():
    assert hash(JPYAmount("150")) == hash(JPYAmount("150"))
