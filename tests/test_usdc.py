from decimal import Decimal

import pytest

from cryptils import BTCAmount, USDCAmount


def test_usdc_name():
    assert USDCAmount(0).name == "USD Coin"


def test_usdc_code():
    assert USDCAmount(0).code == "USDC"


def test_usdc_new_instance():
    assert USDCAmount("1.5") == USDCAmount(1.5)
    assert USDCAmount("1") == USDCAmount(1)
    assert USDCAmount("1.5") == USDCAmount(Decimal("1.5"))


def test_usdc_precision():
    assert USDCAmount("1.0000011") == USDCAmount("1.000001")
    assert USDCAmount("1.0000014") == USDCAmount("1.000001")
    assert USDCAmount("1.00000149") == USDCAmount("1.000001")
    assert USDCAmount("1.0000015") == USDCAmount("1.000002")
    assert USDCAmount("1.0000019") == USDCAmount("1.000002")
    assert USDCAmount("1.00000199") == USDCAmount("1.000002")


def test_usdc_str():
    assert str(USDCAmount("1.5")) == "1.500000"


def test_usdc_repr():
    assert repr(USDCAmount("1.5")) == "USDC(1.500000)"


def test_usdc_hash():
    assert hash(USDCAmount("1.5")) == hash(USDCAmount("1.5"))
    assert hash(USDCAmount("1.5")) == hash(USDCAmount("1.50"))
    assert hash(USDCAmount("1.5")) == hash(USDCAmount(1.5))
    assert hash(USDCAmount("1.5")) != hash(USDCAmount("1.0"))


def test_usdc_to_string():
    assert USDCAmount("1.5").to_string() == "USDC 1.500000"


def test_usdc_to_decimal():
    assert USDCAmount("1.5").to_decimal() == Decimal("1.50000")


def test_usdc_to_float():
    assert USDCAmount("1.5").to_float() == 1.50000


def test_usdc_addition_same_class():
    assert USDCAmount("0.5") + USDCAmount("0.5") == USDCAmount("1.0")


def test_usdc_addition_with_int():
    assert USDCAmount("0.5") + 1 == USDCAmount("1.5")


def test_usdc_addition_with_decimal():
    assert USDCAmount("0.5") + Decimal("0.5") == USDCAmount("1.0")


def test_usdc_addition_with_float():
    assert USDCAmount("0.5") + 0.5 == USDCAmount("1.0")


def test_usdc_addition_with_str_raises():
    with pytest.raises(TypeError):
        USDCAmount("0.5") + "0.5"


def test_usdc_reverse_addition_with_int():
    assert 1 + USDCAmount("0.5") == USDCAmount("1.5")


def test_usdc_subtraction_same_class():
    assert USDCAmount("1.5") - USDCAmount("0.5") == USDCAmount("1.0")


def test_usdc_subtraction_with_int():
    assert USDCAmount("1.5") - 1 == USDCAmount("0.5")


def test_usdc_subtraction_with_decimal():
    assert USDCAmount("1.5") - Decimal("0.5") == USDCAmount("1.0")


def test_usdc_subtraction_with_float():
    assert USDCAmount("1.5") - 0.5 == USDCAmount("1.0")


def test_usdc_subtraction_with_str_raises():
    with pytest.raises(TypeError):
        USDCAmount("1.5") - "0.5"


def test_usdc_reverse_subtraction_with_int():
    assert 2 - USDCAmount("0.5") == USDCAmount("1.5")


def test_usdc_multiplication_with_int():
    assert USDCAmount("1") * 2 == USDCAmount("2")


def test_usdc_multiplication_with_decimal():
    assert USDCAmount("1") * Decimal("2") == USDCAmount("2")


def test_usdc_multiplication_with_float():
    assert USDCAmount("1") * 2.0 == USDCAmount("2")


def test_usdc_multiplication_with_str_raises():
    with pytest.raises(TypeError):
        USDCAmount("1") * "2"


def test_usdc_reverse_multiplication_with_int():
    assert 2 * USDCAmount("1") == USDCAmount("2")


def test_usdc_multiplication_same_class_raises():
    with pytest.raises(TypeError):
        USDCAmount("1") * USDCAmount("2")


def test_usdc_division_with_int():
    assert USDCAmount("2") / 2 == USDCAmount("1")


def test_usdc_division_with_decimal():
    assert USDCAmount("2") / Decimal("2") == USDCAmount("1")


def test_usdc_division_with_float():
    assert USDCAmount("2") / 2.0 == USDCAmount("1")


def test_usdc_division_with_str_raises():
    with pytest.raises(TypeError):
        USDCAmount("2") / "2"


def test_usdc_reverse_division_with_int():
    assert 2 / USDCAmount("2") == USDCAmount("1")


def test_usdc_division_same_class_raises():
    with pytest.raises(TypeError):
        USDCAmount("2") / USDCAmount("1")


def test_usdc_equality_with_int():
    assert USDCAmount("1") == 1
    assert (USDCAmount("1") == 2) is False


def test_usdc_equality_with_decimal():
    assert USDCAmount("1.5") == Decimal("1.5")
    assert (USDCAmount("1.5") == Decimal("2.5")) is False


def test_usdc_equality_with_float():
    assert USDCAmount("1.5") == 1.5
    assert (USDCAmount("1.5") == 2.5) is False


def test_usdc_equality_with_str():
    assert (USDCAmount("1.5") == "1.5") is False
    assert (USDCAmount("1.5") == "2.5") is False


def test_usdc_equality_with_same_class():
    assert USDCAmount("1.5") == USDCAmount("1.5")
    assert (USDCAmount("1.5") == USDCAmount("2.5")) is False


def test_usdc_equality_with_different_class():
    assert (USDCAmount("1.5") == BTCAmount("1.5")) is False
    assert (BTCAmount("1.5") == USDCAmount("1.5")) is False


def test_usdc_inequality_with_int():
    assert USDCAmount("1") != 2
    assert (USDCAmount("1") != 1) is False


def test_usdc_less_than_with_int():
    assert USDCAmount("1") < 2
    assert not USDCAmount("1") < 1


def test_usdc_less_than_with_decimal():
    assert USDCAmount("1") < Decimal("2")
    assert not USDCAmount("1") < Decimal("1")


def test_usdc_less_than_with_float():
    assert USDCAmount("1") < 2.0
    assert not USDCAmount("1") < 1.0


def test_usdc_less_than_with_str_raises():
    with pytest.raises(TypeError):
        assert USDCAmount("1") < "2"


def test_usdc_less_than_with_same_class():
    assert USDCAmount("1") < USDCAmount("2")
    assert not USDCAmount("1") < USDCAmount("1")


def test_usdc_less_than_or_equal_with_int():
    assert USDCAmount("1") <= 1
    assert USDCAmount("1") <= 2
    assert not USDCAmount("2") <= 1


def test_usdc_greater_than_with_int():
    assert USDCAmount("2") > 1
    assert not USDCAmount("1") > 1


def test_usdc_greater_than_with_decimal():
    assert USDCAmount("2") > Decimal("1")
    assert not USDCAmount("1") > Decimal("1")


def test_usdc_greater_than_with_float():
    assert USDCAmount("2") > 1.0
    assert not USDCAmount("1") > 1.0


def test_usdc_greater_than_with_str_raises():
    with pytest.raises(TypeError):
        assert USDCAmount("2") > "1"


def test_usdc_greater_than_with_same_class():
    assert USDCAmount("2") > USDCAmount("1")
    assert not USDCAmount("1") > USDCAmount("1")


def test_usdc_greater_than_or_equal_with_int():
    assert USDCAmount("1") >= 1
    assert USDCAmount("2") >= 1
    assert not USDCAmount("1") >= 2


def test_usdc_comparison_with_zero():
    assert USDCAmount("0") == 0
    assert USDCAmount("0") == Decimal("0")
    assert USDCAmount("0") == 0.0
    assert USDCAmount("0") == USDCAmount("0")
    assert USDCAmount("1") > 0
    assert USDCAmount("-1") < 0
    assert USDCAmount("0") >= 0
    assert USDCAmount("0") <= 0


def test_usdc_add_incompatible_type():
    with pytest.raises(TypeError):
        USDCAmount("1") + None


def test_usdc_sub_incompatible_type():
    with pytest.raises(TypeError):
        USDCAmount("1") - None


def test_usdc_rsub_incompatible_type():
    with pytest.raises(TypeError):
        None - USDCAmount("1")


def test_usdc_mul_incompatible_type():
    with pytest.raises(TypeError):
        USDCAmount("1") * None


def test_usdc_truediv_incompatible_type():
    with pytest.raises(TypeError):
        USDCAmount("1") / None


def test_usdc_rtruediv_incompatible_type():
    with pytest.raises(TypeError):
        None / USDCAmount("1")


def test_usdc_lt_incompatible_type():
    with pytest.raises(TypeError):
        assert USDCAmount("1") < None


def test_usdc_le_incompatible_type():
    with pytest.raises(TypeError):
        assert USDCAmount("1") <= None


def test_usdc_gt_incompatible_type():
    with pytest.raises(TypeError):
        assert USDCAmount("1") > None


def test_usdc_ge_incompatible_type():
    with pytest.raises(TypeError):
        assert USDCAmount("1") >= None


def test_usdc_comparison_with_negative():
    assert USDCAmount("-1") == -1
    assert USDCAmount("-1.5") == Decimal("-1.5")
    assert USDCAmount("-1.5") == -1.5
    assert USDCAmount("-1.5") == USDCAmount("-1.5")
    assert USDCAmount("-1") < 0
    assert USDCAmount("-1") < USDCAmount("0")
    assert USDCAmount("-2") <= -1
    assert USDCAmount("-1") >= -2
    assert USDCAmount("-1") > -2
