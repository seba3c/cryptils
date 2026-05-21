from decimal import Decimal

import pytest

from cryptils import BTCAmount, USDTAmount


def test_usdt_name():
    assert USDTAmount(0).name == "Tether"


def test_usdt_code():
    assert USDTAmount(0).code == "USDT"


def test_usdt_new_instance():
    assert USDTAmount("1.5") == USDTAmount(1.5)
    assert USDTAmount("1") == USDTAmount(1)
    assert USDTAmount("1.5") == USDTAmount(Decimal("1.5"))


def test_usdt_precision():
    assert USDTAmount("1.0000011") == USDTAmount("1.000001")
    assert USDTAmount("1.0000014") == USDTAmount("1.000001")
    assert USDTAmount("1.00000149") == USDTAmount("1.000001")
    assert USDTAmount("1.0000015") == USDTAmount("1.000002")
    assert USDTAmount("1.0000019") == USDTAmount("1.000002")
    assert USDTAmount("1.00000199") == USDTAmount("1.000002")


def test_usdt_str():
    assert str(USDTAmount("1.5")) == "1.500000"


def test_usdt_repr():
    assert repr(USDTAmount("1.5")) == "USDT(1.500000)"


def test_usdt_hash():
    assert hash(USDTAmount("1.5")) == hash(USDTAmount("1.5"))
    assert hash(USDTAmount("1.5")) == hash(USDTAmount("1.50"))
    assert hash(USDTAmount("1.5")) == hash(USDTAmount(1.5))
    assert hash(USDTAmount("1.5")) != hash(USDTAmount("1.0"))


def test_usdt_to_string():
    assert USDTAmount("1.5").to_string() == "USDT 1.500000"


def test_usdt_to_decimal():
    assert USDTAmount("1.5").to_decimal() == Decimal("1.50000")


def test_usdt_to_float():
    assert USDTAmount("1.5").to_float() == 1.50000


def test_usdt_addition_same_class():
    assert USDTAmount("0.5") + USDTAmount("0.5") == USDTAmount("1.0")


def test_usdt_addition_with_int():
    assert USDTAmount("0.5") + 1 == USDTAmount("1.5")


def test_usdt_addition_with_decimal():
    assert USDTAmount("0.5") + Decimal("0.5") == USDTAmount("1.0")


def test_usdt_addition_with_float():
    assert USDTAmount("0.5") + 0.5 == USDTAmount("1.0")


def test_usdt_addition_with_str_raises():
    with pytest.raises(TypeError):
        USDTAmount("0.5") + "0.5"


def test_usdt_reverse_addition_with_int():
    assert 1 + USDTAmount("0.5") == USDTAmount("1.5")


def test_usdt_subtraction_same_class():
    assert USDTAmount("1.5") - USDTAmount("0.5") == USDTAmount("1.0")


def test_usdt_subtraction_with_int():
    assert USDTAmount("1.5") - 1 == USDTAmount("0.5")


def test_usdt_subtraction_with_decimal():
    assert USDTAmount("1.5") - Decimal("0.5") == USDTAmount("1.0")


def test_usdt_subtraction_with_float():
    assert USDTAmount("1.5") - 0.5 == USDTAmount("1.0")


def test_usdt_subtraction_with_str_raises():
    with pytest.raises(TypeError):
        USDTAmount("1.5") - "0.5"


def test_usdt_reverse_subtraction_with_int():
    assert 2 - USDTAmount("0.5") == USDTAmount("1.5")


def test_usdt_multiplication_with_int():
    assert USDTAmount("1") * 2 == USDTAmount("2")


def test_usdt_multiplication_with_decimal():
    assert USDTAmount("1") * Decimal("2") == USDTAmount("2")


def test_usdt_multiplication_with_float():
    assert USDTAmount("1") * 2.0 == USDTAmount("2")


def test_usdt_multiplication_with_str_raises():
    with pytest.raises(TypeError):
        USDTAmount("1") * "2"


def test_usdt_reverse_multiplication_with_int():
    assert 2 * USDTAmount("1") == USDTAmount("2")


def test_usdt_multiplication_same_class_raises():
    with pytest.raises(TypeError):
        USDTAmount("1") * USDTAmount("2")


def test_usdt_division_with_int():
    assert USDTAmount("2") / 2 == USDTAmount("1")


def test_usdt_division_with_decimal():
    assert USDTAmount("2") / Decimal("2") == USDTAmount("1")


def test_usdt_division_with_float():
    assert USDTAmount("2") / 2.0 == USDTAmount("1")


def test_usdt_division_with_str_raises():
    with pytest.raises(TypeError):
        USDTAmount("2") / "2"


def test_usdt_reverse_division_with_int():
    assert 2 / USDTAmount("2") == USDTAmount("1")


def test_usdt_division_same_class_raises():
    with pytest.raises(TypeError):
        USDTAmount("2") / USDTAmount("1")


def test_usdt_equality_with_int():
    assert USDTAmount("1") == 1
    assert (USDTAmount("1") == 2) is False


def test_usdt_equality_with_decimal():
    assert USDTAmount("1.5") == Decimal("1.5")
    assert (USDTAmount("1.5") == Decimal("2.5")) is False


def test_usdt_equality_with_float():
    assert USDTAmount("1.5") == 1.5
    assert (USDTAmount("1.5") == 2.5) is False


def test_usdt_equality_with_str():
    assert (USDTAmount("1.5") == "1.5") is False
    assert (USDTAmount("1.5") == "2.5") is False


def test_usdt_equality_with_same_class():
    assert USDTAmount("1.5") == USDTAmount("1.5")
    assert (USDTAmount("1.5") == USDTAmount("2.5")) is False


def test_usdt_equality_with_different_class():
    assert (USDTAmount("1.5") == BTCAmount("1.5")) is False
    assert (BTCAmount("1.5") == USDTAmount("1.5")) is False


def test_usdt_inequality_with_int():
    assert USDTAmount("1") != 2
    assert (USDTAmount("1") != 1) is False


def test_usdt_less_than_with_int():
    assert USDTAmount("1") < 2
    assert not USDTAmount("1") < 1


def test_usdt_less_than_with_decimal():
    assert USDTAmount("1") < Decimal("2")
    assert not USDTAmount("1") < Decimal("1")


def test_usdt_less_than_with_float():
    assert USDTAmount("1") < 2.0
    assert not USDTAmount("1") < 1.0


def test_usdt_less_than_with_str_raises():
    with pytest.raises(TypeError):
        assert USDTAmount("1") < "2"


def test_usdt_less_than_with_same_class():
    assert USDTAmount("1") < USDTAmount("2")
    assert not USDTAmount("1") < USDTAmount("1")


def test_usdt_less_than_or_equal_with_int():
    assert USDTAmount("1") <= 1
    assert USDTAmount("1") <= 2
    assert not USDTAmount("2") <= 1


def test_usdt_greater_than_with_int():
    assert USDTAmount("2") > 1
    assert not USDTAmount("1") > 1


def test_usdt_greater_than_with_decimal():
    assert USDTAmount("2") > Decimal("1")
    assert not USDTAmount("1") > Decimal("1")


def test_usdt_greater_than_with_float():
    assert USDTAmount("2") > 1.0
    assert not USDTAmount("1") > 1.0


def test_usdt_greater_than_with_str_raises():
    with pytest.raises(TypeError):
        assert USDTAmount("2") > "1"


def test_usdt_greater_than_with_same_class():
    assert USDTAmount("2") > USDTAmount("1")
    assert not USDTAmount("1") > USDTAmount("1")


def test_usdt_greater_than_or_equal_with_int():
    assert USDTAmount("1") >= 1
    assert USDTAmount("2") >= 1
    assert not USDTAmount("1") >= 2


def test_usdt_comparison_with_zero():
    assert USDTAmount("0") == 0
    assert USDTAmount("0") == Decimal("0")
    assert USDTAmount("0") == 0.0
    assert USDTAmount("0") == USDTAmount("0")
    assert USDTAmount("1") > 0
    assert USDTAmount("-1") < 0
    assert USDTAmount("0") >= 0
    assert USDTAmount("0") <= 0


def test_usdt_add_incompatible_type():
    with pytest.raises(TypeError):
        USDTAmount("1") + None


def test_usdt_sub_incompatible_type():
    with pytest.raises(TypeError):
        USDTAmount("1") - None


def test_usdt_rsub_incompatible_type():
    with pytest.raises(TypeError):
        None - USDTAmount("1")


def test_usdt_mul_incompatible_type():
    with pytest.raises(TypeError):
        USDTAmount("1") * None


def test_usdt_truediv_incompatible_type():
    with pytest.raises(TypeError):
        USDTAmount("1") / None


def test_usdt_rtruediv_incompatible_type():
    with pytest.raises(TypeError):
        None / USDTAmount("1")


def test_usdt_lt_incompatible_type():
    with pytest.raises(TypeError):
        assert USDTAmount("1") < None


def test_usdt_le_incompatible_type():
    with pytest.raises(TypeError):
        assert USDTAmount("1") <= None


def test_usdt_gt_incompatible_type():
    with pytest.raises(TypeError):
        assert USDTAmount("1") > None


def test_usdt_ge_incompatible_type():
    with pytest.raises(TypeError):
        assert USDTAmount("1") >= None


def test_usdt_comparison_with_negative():
    assert USDTAmount("-1") == -1
    assert USDTAmount("-1.5") == Decimal("-1.5")
    assert USDTAmount("-1.5") == -1.5
    assert USDTAmount("-1.5") == USDTAmount("-1.5")
    assert USDTAmount("-1") < 0
    assert USDTAmount("-1") < USDTAmount("0")
    assert USDTAmount("-2") <= -1
    assert USDTAmount("-1") >= -2
    assert USDTAmount("-1") > -2
