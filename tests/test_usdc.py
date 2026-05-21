from decimal import Decimal

import pytest

from cryptils import USDC, BTCAmount


def test_usdc_name():
    assert USDC(0).name == "USD Coin"


def test_usdc_code():
    assert USDC(0).code == "USDC"


def test_usdc_new_instance():
    assert USDC("1.5") == USDC(1.5)
    assert USDC("1") == USDC(1)
    assert USDC("1.5") == USDC(Decimal("1.5"))


def test_usdc_precision():
    assert USDC("1.0000011") == USDC("1.000001")
    assert USDC("1.0000014") == USDC("1.000001")
    assert USDC("1.00000149") == USDC("1.000001")
    assert USDC("1.0000015") == USDC("1.000002")
    assert USDC("1.0000019") == USDC("1.000002")
    assert USDC("1.00000199") == USDC("1.000002")


def test_usdc_str():
    assert str(USDC("1.5")) == "1.500000"


def test_usdc_repr():
    assert repr(USDC("1.5")) == "USDC(1.500000)"


def test_usdc_hash():
    assert hash(USDC("1.5")) == hash(USDC("1.5"))
    assert hash(USDC("1.5")) == hash(USDC("1.50"))
    assert hash(USDC("1.5")) == hash(USDC(1.5))
    assert hash(USDC("1.5")) != hash(USDC("1.0"))


def test_usdc_to_string():
    assert USDC("1.5").to_string() == "USDC 1.500000"


def test_usdc_to_decimal():
    assert USDC("1.5").to_decimal() == Decimal("1.50000")


def test_usdc_to_float():
    assert USDC("1.5").to_float() == 1.50000


def test_usdc_addition_same_class():
    assert USDC("0.5") + USDC("0.5") == USDC("1.0")


def test_usdc_addition_with_int():
    assert USDC("0.5") + 1 == USDC("1.5")


def test_usdc_addition_with_decimal():
    assert USDC("0.5") + Decimal("0.5") == USDC("1.0")


def test_usdc_addition_with_float():
    assert USDC("0.5") + 0.5 == USDC("1.0")


def test_usdc_addition_with_str_raises():
    with pytest.raises(TypeError):
        USDC("0.5") + "0.5"


def test_usdc_reverse_addition_with_int():
    assert 1 + USDC("0.5") == USDC("1.5")


def test_usdc_subtraction_same_class():
    assert USDC("1.5") - USDC("0.5") == USDC("1.0")


def test_usdc_subtraction_with_int():
    assert USDC("1.5") - 1 == USDC("0.5")


def test_usdc_subtraction_with_decimal():
    assert USDC("1.5") - Decimal("0.5") == USDC("1.0")


def test_usdc_subtraction_with_float():
    assert USDC("1.5") - 0.5 == USDC("1.0")


def test_usdc_subtraction_with_str_raises():
    with pytest.raises(TypeError):
        USDC("1.5") - "0.5"


def test_usdc_reverse_subtraction_with_int():
    assert 2 - USDC("0.5") == USDC("1.5")


def test_usdc_multiplication_with_int():
    assert USDC("1") * 2 == USDC("2")


def test_usdc_multiplication_with_decimal():
    assert USDC("1") * Decimal("2") == USDC("2")


def test_usdc_multiplication_with_float():
    assert USDC("1") * 2.0 == USDC("2")


def test_usdc_multiplication_with_str_raises():
    with pytest.raises(TypeError):
        USDC("1") * "2"


def test_usdc_reverse_multiplication_with_int():
    assert 2 * USDC("1") == USDC("2")


def test_usdc_multiplication_same_class_raises():
    with pytest.raises(TypeError):
        USDC("1") * USDC("2")


def test_usdc_division_with_int():
    assert USDC("2") / 2 == USDC("1")


def test_usdc_division_with_decimal():
    assert USDC("2") / Decimal("2") == USDC("1")


def test_usdc_division_with_float():
    assert USDC("2") / 2.0 == USDC("1")


def test_usdc_division_with_str_raises():
    with pytest.raises(TypeError):
        USDC("2") / "2"


def test_usdc_reverse_division_with_int():
    assert 2 / USDC("2") == USDC("1")


def test_usdc_division_same_class_raises():
    with pytest.raises(TypeError):
        USDC("2") / USDC("1")


def test_usdc_equality_with_int():
    assert USDC("1") == 1
    assert (USDC("1") == 2) is False


def test_usdc_equality_with_decimal():
    assert USDC("1.5") == Decimal("1.5")
    assert (USDC("1.5") == Decimal("2.5")) is False


def test_usdc_equality_with_float():
    assert USDC("1.5") == 1.5
    assert (USDC("1.5") == 2.5) is False


def test_usdc_equality_with_str():
    assert (USDC("1.5") == "1.5") is False
    assert (USDC("1.5") == "2.5") is False


def test_usdc_equality_with_same_class():
    assert USDC("1.5") == USDC("1.5")
    assert (USDC("1.5") == USDC("2.5")) is False


def test_usdc_equality_with_different_class():
    assert (USDC("1.5") == BTCAmount("1.5")) is False
    assert (BTCAmount("1.5") == USDC("1.5")) is False


def test_usdc_inequality_with_int():
    assert USDC("1") != 2
    assert (USDC("1") != 1) is False


def test_usdc_less_than_with_int():
    assert USDC("1") < 2
    assert not USDC("1") < 1


def test_usdc_less_than_with_decimal():
    assert USDC("1") < Decimal("2")
    assert not USDC("1") < Decimal("1")


def test_usdc_less_than_with_float():
    assert USDC("1") < 2.0
    assert not USDC("1") < 1.0


def test_usdc_less_than_with_str_raises():
    with pytest.raises(TypeError):
        assert USDC("1") < "2"


def test_usdc_less_than_with_same_class():
    assert USDC("1") < USDC("2")
    assert not USDC("1") < USDC("1")


def test_usdc_less_than_or_equal_with_int():
    assert USDC("1") <= 1
    assert USDC("1") <= 2
    assert not USDC("2") <= 1


def test_usdc_greater_than_with_int():
    assert USDC("2") > 1
    assert not USDC("1") > 1


def test_usdc_greater_than_with_decimal():
    assert USDC("2") > Decimal("1")
    assert not USDC("1") > Decimal("1")


def test_usdc_greater_than_with_float():
    assert USDC("2") > 1.0
    assert not USDC("1") > 1.0


def test_usdc_greater_than_with_str_raises():
    with pytest.raises(TypeError):
        assert USDC("2") > "1"


def test_usdc_greater_than_with_same_class():
    assert USDC("2") > USDC("1")
    assert not USDC("1") > USDC("1")


def test_usdc_greater_than_or_equal_with_int():
    assert USDC("1") >= 1
    assert USDC("2") >= 1
    assert not USDC("1") >= 2


def test_usdc_comparison_with_zero():
    assert USDC("0") == 0
    assert USDC("0") == Decimal("0")
    assert USDC("0") == 0.0
    assert USDC("0") == USDC("0")
    assert USDC("1") > 0
    assert USDC("-1") < 0
    assert USDC("0") >= 0
    assert USDC("0") <= 0


def test_usdc_add_incompatible_type():
    with pytest.raises(TypeError):
        USDC("1") + None


def test_usdc_sub_incompatible_type():
    with pytest.raises(TypeError):
        USDC("1") - None


def test_usdc_rsub_incompatible_type():
    with pytest.raises(TypeError):
        None - USDC("1")


def test_usdc_mul_incompatible_type():
    with pytest.raises(TypeError):
        USDC("1") * None


def test_usdc_truediv_incompatible_type():
    with pytest.raises(TypeError):
        USDC("1") / None


def test_usdc_rtruediv_incompatible_type():
    with pytest.raises(TypeError):
        None / USDC("1")


def test_usdc_lt_incompatible_type():
    with pytest.raises(TypeError):
        assert USDC("1") < None


def test_usdc_le_incompatible_type():
    with pytest.raises(TypeError):
        assert USDC("1") <= None


def test_usdc_gt_incompatible_type():
    with pytest.raises(TypeError):
        assert USDC("1") > None


def test_usdc_ge_incompatible_type():
    with pytest.raises(TypeError):
        assert USDC("1") >= None


def test_usdc_comparison_with_negative():
    assert USDC("-1") == -1
    assert USDC("-1.5") == Decimal("-1.5")
    assert USDC("-1.5") == -1.5
    assert USDC("-1.5") == USDC("-1.5")
    assert USDC("-1") < 0
    assert USDC("-1") < USDC("0")
    assert USDC("-2") <= -1
    assert USDC("-1") >= -2
    assert USDC("-1") > -2
