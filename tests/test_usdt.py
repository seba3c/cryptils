from decimal import Decimal

import pytest

from cryptils import BTC, USDT


def test_usdt_name():
    assert USDT._name == "Tether"


def test_usdt_symbol():
    assert USDT._symbol == "USDT"


def test_usdt_precision():
    assert USDT("1.0000011") == USDT("1.000001")
    assert USDT("1.0000014") == USDT("1.000001")
    assert USDT("1.00000149") == USDT("1.000001")
    assert USDT("1.0000015") == USDT("1.000002")
    assert USDT("1.0000019") == USDT("1.000002")
    assert USDT("1.00000199") == USDT("1.000002")


def test_usdt_str():
    assert str(USDT("1.5")) == "1.500000"


def test_usdt_repr():
    assert repr(USDT("1.5")) == "USDT(1.500000 USDT)"


def test_usdt_hash():
    assert hash(USDT("1.5")) == hash(USDT("1.5"))
    assert hash(USDT("1.5")) == hash(USDT("1.50"))
    assert hash(USDT("1.5")) == hash(USDT(1.5))
    assert hash(USDT("1.5")) != hash(USDT("1.0"))


def test_usdt_to_string():
    assert USDT("1.5").to_string() == "1.500000 USDT"


def test_usdt_as_decimal():
    assert USDT("1.5").as_decimal() == Decimal("1.50000")


def test_usdt_addition_same_class():
    assert USDT("0.5") + USDT("0.5") == USDT("1.0")


def test_usdt_addition_with_int():
    assert USDT("0.5") + 1 == USDT("1.5")


def test_usdt_addition_with_decimal():
    assert USDT("0.5") + Decimal("0.5") == USDT("1.0")


def test_usdt_addition_with_float():
    assert USDT("0.5") + 0.5 == USDT("1.0")


def test_usdt_addition_with_str():
    assert USDT("0.5") + "0.5" == USDT("1.0")


def test_usdt_reverse_addition_with_int():
    assert 1 + USDT("0.5") == USDT("1.5")


def test_usdt_subtraction_same_class():
    assert USDT("1.5") - USDT("0.5") == USDT("1.0")


def test_usdt_subtraction_with_int():
    assert USDT("1.5") - 1 == USDT("0.5")


def test_usdt_subtraction_with_decimal():
    assert USDT("1.5") - Decimal("0.5") == USDT("1.0")


def test_usdt_subtraction_with_float():
    assert USDT("1.5") - 0.5 == USDT("1.0")


def test_usdt_subtraction_with_str():
    assert USDT("1.5") - "0.5" == USDT("1.0")


def test_usdt_reverse_subtraction_with_int():
    assert 2 - USDT("0.5") == USDT("1.5")


def test_usdt_multiplication_with_int():
    assert USDT("1") * 2 == USDT("2")


def test_usdt_multiplication_with_decimal():
    assert USDT("1") * Decimal("2") == USDT("2")


def test_usdt_multiplication_with_float():
    assert USDT("1") * 2.0 == USDT("2")


def test_usdt_multiplication_with_str():
    assert USDT("1") * "2" == USDT("2")


def test_usdt_reverse_multiplication_with_int():
    assert 2 * USDT("1") == USDT("2")


def test_usdt_multiplication_same_class_raises():
    with pytest.raises(TypeError):
        USDT("1") * USDT("2")


def test_usdt_division_with_int():
    assert USDT("2") / 2 == USDT("1")


def test_usdt_division_with_decimal():
    assert USDT("2") / Decimal("2") == USDT("1")


def test_usdt_division_with_float():
    assert USDT("2") / 2.0 == USDT("1")


def test_usdt_division_with_str():
    assert USDT("2") / "2" == USDT("1")


def test_usdt_reverse_division_with_int():
    assert 2 / USDT("2") == USDT("1")


def test_usdt_division_same_class_raises():
    with pytest.raises(TypeError):
        USDT("2") / USDT("1")


def test_usdt_equality_with_int():
    assert USDT("1") == 1
    assert (USDT("1") == 2) is False


def test_usdt_equality_with_decimal():
    assert USDT("1.5") == Decimal("1.5")
    assert (USDT("1.5") == Decimal("2.5")) is False


def test_usdt_equality_with_float():
    assert USDT("1.5") == 1.5
    assert (USDT("1.5") == 2.5) is False


def test_usdt_equality_with_str():
    assert USDT("1.5") == "1.5"
    assert (USDT("1.5") == "2.5") is False


def test_usdt_equality_with_same_class():
    assert USDT("1.5") == USDT("1.5")
    assert (USDT("1.5") == USDT("2.5")) is False


def test_usdt_equality_with_different_class():
    assert (USDT("1.5") == BTC("1.5")) is False
    assert (BTC("1.5") == USDT("1.5")) is False


def test_usdt_inequality_with_int():
    assert USDT("1") != 2
    assert (USDT("1") != 1) is False


def test_usdt_less_than_with_int():
    assert USDT("1") < 2
    assert not USDT("1") < 1


def test_usdt_less_than_with_decimal():
    assert USDT("1") < Decimal("2")
    assert not USDT("1") < Decimal("1")


def test_usdt_less_than_with_float():
    assert USDT("1") < 2.0
    assert not USDT("1") < 1.0


def test_usdt_less_than_with_str():
    assert USDT("1") < "2"
    assert not USDT("1") < "1"


def test_usdt_less_than_with_same_class():
    assert USDT("1") < USDT("2")
    assert not USDT("1") < USDT("1")


def test_usdt_less_than_or_equal_with_int():
    assert USDT("1") <= 1
    assert USDT("1") <= 2
    assert not USDT("2") <= 1


def test_usdt_greater_than_with_int():
    assert USDT("2") > 1
    assert not USDT("1") > 1


def test_usdt_greater_than_with_decimal():
    assert USDT("2") > Decimal("1")
    assert not USDT("1") > Decimal("1")


def test_usdt_greater_than_with_float():
    assert USDT("2") > 1.0
    assert not USDT("1") > 1.0


def test_usdt_greater_than_with_str():
    assert USDT("2") > "1"
    assert not USDT("1") > "1"


def test_usdt_greater_than_with_same_class():
    assert USDT("2") > USDT("1")
    assert not USDT("1") > USDT("1")


def test_usdt_greater_than_or_equal_with_int():
    assert USDT("1") >= 1
    assert USDT("2") >= 1
    assert not USDT("1") >= 2


def test_usdt_comparison_with_zero():
    assert USDT("0") == 0
    assert USDT("0") == Decimal("0")
    assert USDT("0") == 0.0
    assert USDT("0") == "0"
    assert USDT("0") == USDT("0")
    assert USDT("1") > 0
    assert USDT("-1") < 0
    assert USDT("0") >= 0
    assert USDT("0") <= 0


def test_usdt_add_incompatible_type():
    with pytest.raises(TypeError):
        USDT("1") + None


def test_usdt_sub_incompatible_type():
    with pytest.raises(TypeError):
        USDT("1") - None


def test_usdt_rsub_incompatible_type():
    with pytest.raises(TypeError):
        None - USDT("1")


def test_usdt_mul_incompatible_type():
    with pytest.raises(TypeError):
        USDT("1") * None


def test_usdt_truediv_incompatible_type():
    with pytest.raises(TypeError):
        USDT("1") / None


def test_usdt_rtruediv_incompatible_type():
    with pytest.raises(TypeError):
        None / USDT("1")


def test_usdt_lt_incompatible_type():
    with pytest.raises(TypeError):
        assert USDT("1") < None


def test_usdt_le_incompatible_type():
    with pytest.raises(TypeError):
        assert USDT("1") <= None


def test_usdt_gt_incompatible_type():
    with pytest.raises(TypeError):
        assert USDT("1") > None


def test_usdt_ge_incompatible_type():
    with pytest.raises(TypeError):
        assert USDT("1") >= None


def test_usdt_comparison_with_negative():
    assert USDT("-1") == -1
    assert USDT("-1.5") == Decimal("-1.5")
    assert USDT("-1.5") == -1.5
    assert USDT("-1.5") == "-1.5"
    assert USDT("-1.5") == USDT("-1.5")
    assert USDT("-1") < 0
    assert USDT("-1") < USDT("0")
    assert USDT("-2") <= -1
    assert USDT("-1") >= -2
    assert USDT("-1") > -2
