from decimal import Decimal

import pytest

from cryptils import ETH, BTCAmount


def test_btc_name():
    assert BTCAmount(0).name == "Bitcoin"


def test_btc_code():
    assert BTCAmount(0).code == "BTC"


def test_btc_new_instance():
    assert BTCAmount("1.5") == BTCAmount(1.5)
    assert BTCAmount("1") == BTCAmount(1)
    assert BTCAmount("1.5") == BTCAmount(Decimal("1.5"))
    assert BTCAmount("1.50000000") == BTCAmount(BTCAmount("1.500000001"))


def test_btc_precision():
    assert BTCAmount("1.000000011") == BTCAmount("1.00000001")
    assert BTCAmount("1.000000014") == BTCAmount("1.00000001")
    assert BTCAmount("1.0000000149") == BTCAmount("1.00000001")
    assert BTCAmount("1.000000015") == BTCAmount("1.00000002")
    assert BTCAmount("1.000000019") == BTCAmount("1.00000002")
    assert BTCAmount("1.0000000199") == BTCAmount("1.00000002")


def test_btc_str():
    assert str(BTCAmount("1.5")) == "1.50000000"


def test_btc_repr():
    assert repr(BTCAmount("1.5")) == "BTC(1.50000000)"


def test_btc_hash():
    assert hash(BTCAmount("1.5")) == hash(BTCAmount("1.5"))
    assert hash(BTCAmount("1.5")) == hash(BTCAmount("1.50"))
    assert hash(BTCAmount("1.5")) == hash(BTCAmount(1.5))
    assert hash(BTCAmount("1.5")) != hash(BTCAmount("1.0"))


def test_btc_to_string():
    assert BTCAmount("1.5").to_string() == "BTC 1.50000000"


def test_btc_to_decimal():
    assert BTCAmount("1.5").to_decimal() == Decimal("1.5000000")


def test_btc_to_float():
    assert BTCAmount("1.5").to_float() == 1.5000000


def test_btc_addition_same_class():
    assert BTCAmount("0.5") + BTCAmount("0.5") == BTCAmount("1.0")


def test_btc_addition_with_int():
    assert BTCAmount("0.5") + 1 == BTCAmount("1.5")


def test_btc_addition_with_decimal():
    assert BTCAmount("0.5") + Decimal("0.5") == BTCAmount("1.0")


def test_btc_addition_with_float():
    assert BTCAmount("0.5") + 0.5 == BTCAmount("1.0")


def test_btc_addition_with_str():
    with pytest.raises(TypeError):
        assert BTCAmount("0.5") + "0.5"


def test_btc_reverse_addition_with_int():
    assert 1 + BTCAmount("0.5") == BTCAmount("1.5")


def test_btc_subtraction_same_class():
    assert BTCAmount("1.5") - BTCAmount("0.5") == BTCAmount("1.0")


def test_btc_subtraction_with_int():
    assert BTCAmount("1.5") - 1 == BTCAmount("0.5")


def test_btc_subtraction_with_decimal():
    assert BTCAmount("1.5") - Decimal("0.5") == BTCAmount("1.0")


def test_btc_subtraction_with_float():
    assert BTCAmount("1.5") - 0.5 == BTCAmount("1.0")


def test_btc_subtraction_with_str_raises():
    with pytest.raises(TypeError):
        BTCAmount("1.5") - "0.5"


def test_btc_reverse_subtraction_with_int():
    assert 2 - BTCAmount("0.5") == BTCAmount("1.5")


def test_btc_multiplication_with_int():
    assert BTCAmount("1") * 2 == BTCAmount("2")


def test_btc_multiplication_with_decimal():
    assert BTCAmount("1") * Decimal("2") == BTCAmount("2")


def test_btc_multiplication_with_float():
    assert BTCAmount("1") * 2.0 == BTCAmount("2")


def test_btc_multiplication_with_str_raises():
    with pytest.raises(TypeError):
        assert BTCAmount("1") * "2"


def test_btc_reverse_multiplication_with_int():
    assert 2 * BTCAmount("1") == BTCAmount("2")


def test_btc_multiplication_same_class_raises():
    with pytest.raises(TypeError):
        BTCAmount("1") * BTCAmount("2")


def test_btc_division_with_int():
    assert BTCAmount("2") / 2 == BTCAmount("1")


def test_btc_division_with_decimal():
    assert BTCAmount("2") / Decimal("2") == BTCAmount("1")


def test_btc_division_with_float():
    assert BTCAmount("2") / 2.0 == BTCAmount("1")


def test_btc_division_with_str_raises():
    with pytest.raises(TypeError):
        assert BTCAmount("2") / "2"


def test_btc_reverse_division_with_int():
    assert 2 / BTCAmount("2") == BTCAmount("1")


def test_btc_division_same_class_raises():
    with pytest.raises(TypeError):
        BTCAmount("2") / BTCAmount("1")


def test_btc_equality_with_int():
    assert BTCAmount("1") == 1
    assert (BTCAmount("1") == 2) is False


def test_btc_equality_with_decimal():
    assert BTCAmount("1.5") == Decimal("1.5")
    assert (BTCAmount("1.5") == Decimal("2.5")) is False


def test_btc_equality_with_float():
    assert BTCAmount("1.5") == 1.5
    assert (BTCAmount("1.5") == 2.5) is False


def test_btc_equality_with_str():
    assert (BTCAmount("1.5") == "1.5") is False


def test_btc_equality_with_same_class():
    assert BTCAmount("1.5") == BTCAmount("1.5")
    assert (BTCAmount("1.5") == BTCAmount("2.5")) is False


def test_btc_equality_with_different_class():
    assert (BTCAmount("1.5") == ETH("1.5")) is False
    assert (ETH("1.5") == BTCAmount("1.5")) is False


def test_btc_inequality_with_int():
    assert BTCAmount("1") != 2
    assert (BTCAmount("1") != 1) is False


def test_btc_less_than_with_int():
    assert BTCAmount("1") < 2
    assert not BTCAmount("1") < 1


def test_btc_less_than_with_decimal():
    assert BTCAmount("1") < Decimal("2")
    assert not BTCAmount("1") < Decimal("1")


def test_btc_less_than_with_float():
    assert BTCAmount("1") < 2.0
    assert not BTCAmount("1") < 1.0


def test_btc_less_than_with_str_raises():
    with pytest.raises(TypeError):
        assert BTCAmount("1") < "2"


def test_btc_less_than_with_same_class():
    assert BTCAmount("1") < BTCAmount("2")
    assert not BTCAmount("1") < BTCAmount("1")


def test_btc_less_than_or_equal_with_int():
    assert BTCAmount("1") <= 1
    assert BTCAmount("1") <= 2
    assert not BTCAmount("2") <= 1


def test_btc_greater_than_with_int():
    assert BTCAmount("2") > 1
    assert not BTCAmount("1") > 1


def test_btc_greater_than_with_decimal():
    assert BTCAmount("2") > Decimal("1")
    assert not BTCAmount("1") > Decimal("1")


def test_btc_greater_than_with_float():
    assert BTCAmount("2") > 1.0
    assert not BTCAmount("1") > 1.0


def test_btc_greater_than_with_str_raises():
    with pytest.raises(TypeError):
        assert BTCAmount("2") > "1"


def test_btc_greater_than_with_same_class():
    assert BTCAmount("2") > BTCAmount("1")
    assert not BTCAmount("1") > BTCAmount("1")


def test_btc_greater_than_or_equal_with_int():
    assert BTCAmount("1") >= 1
    assert BTCAmount("2") >= 1
    assert not BTCAmount("1") >= 2


def test_btc_comparison_with_zero():
    assert BTCAmount("0") == 0
    assert BTCAmount("0") == Decimal("0")
    assert BTCAmount("0") == 0.0
    assert BTCAmount("0") == BTCAmount("0")
    assert BTCAmount("1") > 0
    assert BTCAmount("-1") < 0
    assert BTCAmount("0") >= 0
    assert BTCAmount("0") <= 0


def test_btc_add_incompatible_type():
    with pytest.raises(TypeError):
        BTCAmount("1") + None


def test_btc_sub_incompatible_type():
    with pytest.raises(TypeError):
        BTCAmount("1") - None


def test_btc_rsub_incompatible_type():
    with pytest.raises(TypeError):
        None - BTCAmount("1")


def test_btc_mul_incompatible_type():
    with pytest.raises(TypeError):
        BTCAmount("1") * None


def test_btc_truediv_incompatible_type():
    with pytest.raises(TypeError):
        BTCAmount("1") / None


def test_btc_rtruediv_incompatible_type():
    with pytest.raises(TypeError):
        None / BTCAmount("1")


def test_btc_lt_incompatible_type():
    with pytest.raises(TypeError):
        assert BTCAmount("1") < None


def test_btc_le_incompatible_type():
    with pytest.raises(TypeError):
        assert BTCAmount("1") <= None


def test_btc_gt_incompatible_type():
    with pytest.raises(TypeError):
        assert BTCAmount("1") > None


def test_btc_ge_incompatible_type():
    with pytest.raises(TypeError):
        assert BTCAmount("1") >= None


def test_btc_comparison_with_negative():
    assert BTCAmount("-1") == -1
    assert BTCAmount("-1.5") == Decimal("-1.5")
    assert BTCAmount("-1.5") == -1.5
    assert BTCAmount("-1.5") == BTCAmount("-1.5")
    assert BTCAmount("-1") < 0
    assert BTCAmount("-1") < BTCAmount("0")
    assert BTCAmount("-2") <= -1
    assert BTCAmount("-1") >= -2
    assert BTCAmount("-1") > -2
