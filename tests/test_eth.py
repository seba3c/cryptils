from decimal import Decimal

import pytest

from cryptils import BTCAmount, ETHAmount


def test_eth_name():
    assert ETHAmount(0).name == "Ethereum"


def test_eth_code():
    assert ETHAmount(0).code == "ETH"


def test_eth_new_instance():
    assert ETHAmount("1.5") == ETHAmount(1.5)
    assert ETHAmount("1") == ETHAmount(1)
    assert ETHAmount("1.5") == ETHAmount(Decimal("1.5"))


def test_eth_precision():
    assert ETHAmount("1.0000000000000000011") == ETHAmount("1.000000000000000001")
    assert ETHAmount("1.0000000000000000014") == ETHAmount("1.000000000000000001")
    assert ETHAmount("1.00000000000000000149") == ETHAmount("1.000000000000000001")
    assert ETHAmount("1.0000000000000000015") == ETHAmount("1.000000000000000002")
    assert ETHAmount("1.0000000000000000019") == ETHAmount("1.000000000000000002")
    assert ETHAmount("1.00000000000000000199") == ETHAmount("1.000000000000000002")


def test_eth_str():
    assert str(ETHAmount("1.5")) == "1.500000000000000000"


def test_eth_repr():
    assert repr(ETHAmount("1.5")) == "ETH(1.500000000000000000)"


def test_eth_hash():
    assert hash(ETHAmount("1.5")) == hash(ETHAmount("1.5"))
    assert hash(ETHAmount("1.5")) == hash(ETHAmount("1.50"))
    assert hash(ETHAmount("1.5")) == hash(ETHAmount(1.5))
    assert hash(ETHAmount("1.5")) != hash(ETHAmount("1.0"))


def test_eth_to_string():
    assert ETHAmount("1.5").to_string() == "ETH 1.500000000000000000"


def test_eth_to_decimal():
    assert ETHAmount("1.5").to_decimal() == Decimal("1.50000000000000000")


def test_eth_to_float():
    assert ETHAmount("1.5").to_float() == 1.50000000000000000


def test_eth_addition_same_class():
    assert ETHAmount("0.5") + ETHAmount("0.5") == ETHAmount("1.0")


def test_eth_addition_with_int():
    assert ETHAmount("0.5") + 1 == ETHAmount("1.5")


def test_eth_addition_with_decimal():
    assert ETHAmount("0.5") + Decimal("0.5") == ETHAmount("1.0")


def test_eth_addition_with_float():
    assert ETHAmount("0.5") + 0.5 == ETHAmount("1.0")


def test_eth_addition_with_str_raises():
    with pytest.raises(TypeError):
        ETHAmount("0.5") + "0.5"


def test_eth_reverse_addition_with_int():
    assert 1 + ETHAmount("0.5") == ETHAmount("1.5")


def test_eth_subtraction_same_class():
    assert ETHAmount("1.5") - ETHAmount("0.5") == ETHAmount("1.0")


def test_eth_subtraction_with_int():
    assert ETHAmount("1.5") - 1 == ETHAmount("0.5")


def test_eth_subtraction_with_decimal():
    assert ETHAmount("1.5") - Decimal("0.5") == ETHAmount("1.0")


def test_eth_subtraction_with_float():
    assert ETHAmount("1.5") - 0.5 == ETHAmount("1.0")


def test_eth_subtraction_with_str_raises():
    with pytest.raises(TypeError):
        ETHAmount("1.5") - "0.5"


def test_eth_reverse_subtraction_with_int():
    assert 2 - ETHAmount("0.5") == ETHAmount("1.5")


def test_eth_multiplication_with_int():
    assert ETHAmount("1") * 2 == ETHAmount("2")


def test_eth_multiplication_with_decimal():
    assert ETHAmount("1") * Decimal("2") == ETHAmount("2")


def test_eth_multiplication_with_float():
    assert ETHAmount("1") * 2.0 == ETHAmount("2")


def test_eth_multiplication_with_str_raises():
    with pytest.raises(TypeError):
        ETHAmount("1") * "2"


def test_eth_reverse_multiplication_with_int():
    assert 2 * ETHAmount("1") == ETHAmount("2")


def test_eth_multiplication_same_class_raises():
    with pytest.raises(TypeError):
        ETHAmount("1") * ETHAmount("2")


def test_eth_division_with_int():
    assert ETHAmount("2") / 2 == ETHAmount("1")


def test_eth_division_with_decimal():
    assert ETHAmount("2") / Decimal("2") == ETHAmount("1")


def test_eth_division_with_float():
    assert ETHAmount("2") / 2.0 == ETHAmount("1")


def test_eth_division_with_str_raises():
    with pytest.raises(TypeError):
        ETHAmount("2") / "2"


def test_eth_reverse_division_with_int():
    assert 2 / ETHAmount("2") == ETHAmount("1")


def test_eth_division_same_class_raises():
    with pytest.raises(TypeError):
        ETHAmount("2") / ETHAmount("1")


def test_eth_equality_with_int():
    assert ETHAmount("1") == 1
    assert (ETHAmount("1") == 2) is False


def test_eth_equality_with_decimal():
    assert ETHAmount("1.5") == Decimal("1.5")
    assert (ETHAmount("1.5") == Decimal("2.5")) is False


def test_eth_equality_with_float():
    assert ETHAmount("1.5") == 1.5
    assert (ETHAmount("1.5") == 2.5) is False


def test_eth_equality_with_str():
    assert (ETHAmount("1.5") == "1.5") is False
    assert (ETHAmount("1.5") == "2.5") is False


def test_eth_equality_with_same_class():
    assert ETHAmount("1.5") == ETHAmount("1.5")
    assert (ETHAmount("1.5") == ETHAmount("2.5")) is False


def test_eth_equality_with_different_class():
    assert (ETHAmount("1.5") == BTCAmount("1.5")) is False
    assert (BTCAmount("1.5") == ETHAmount("1.5")) is False


def test_eth_inequality_with_int():
    assert ETHAmount("1") != 2
    assert (ETHAmount("1") != 1) is False


def test_eth_less_than_with_int():
    assert ETHAmount("1") < 2
    assert not ETHAmount("1") < 1


def test_eth_less_than_with_decimal():
    assert ETHAmount("1") < Decimal("2")
    assert not ETHAmount("1") < Decimal("1")


def test_eth_less_than_with_float():
    assert ETHAmount("1") < 2.0
    assert not ETHAmount("1") < 1.0


def test_eth_less_than_with_str_raises():
    with pytest.raises(TypeError):
        assert ETHAmount("1") < "2"


def test_eth_less_than_with_same_class():
    assert ETHAmount("1") < ETHAmount("2")
    assert not ETHAmount("1") < ETHAmount("1")


def test_eth_less_than_or_equal_with_int():
    assert ETHAmount("1") <= 1
    assert ETHAmount("1") <= 2
    assert not ETHAmount("2") <= 1


def test_eth_greater_than_with_int():
    assert ETHAmount("2") > 1
    assert not ETHAmount("1") > 1


def test_eth_greater_than_with_decimal():
    assert ETHAmount("2") > Decimal("1")
    assert not ETHAmount("1") > Decimal("1")


def test_eth_greater_than_with_float():
    assert ETHAmount("2") > 1.0
    assert not ETHAmount("1") > 1.0


def test_eth_greater_than_with_str_raises():
    with pytest.raises(TypeError):
        assert ETHAmount("2") > "1"


def test_eth_greater_than_with_same_class():
    assert ETHAmount("2") > ETHAmount("1")
    assert not ETHAmount("1") > ETHAmount("1")


def test_eth_greater_than_or_equal_with_int():
    assert ETHAmount("1") >= 1
    assert ETHAmount("2") >= 1
    assert not ETHAmount("1") >= 2


def test_eth_comparison_with_zero():
    assert ETHAmount("0") == 0
    assert ETHAmount("0") == Decimal("0")
    assert ETHAmount("0") == 0.0
    assert ETHAmount("0") == ETHAmount("0")
    assert ETHAmount("1") > 0
    assert ETHAmount("-1") < 0
    assert ETHAmount("0") >= 0
    assert ETHAmount("0") <= 0


def test_eth_add_incompatible_type():
    with pytest.raises(TypeError):
        ETHAmount("1") + None


def test_eth_sub_incompatible_type():
    with pytest.raises(TypeError):
        ETHAmount("1") - None


def test_eth_rsub_incompatible_type():
    with pytest.raises(TypeError):
        None - ETHAmount("1")


def test_eth_mul_incompatible_type():
    with pytest.raises(TypeError):
        ETHAmount("1") * None


def test_eth_truediv_incompatible_type():
    with pytest.raises(TypeError):
        ETHAmount("1") / None


def test_eth_rtruediv_incompatible_type():
    with pytest.raises(TypeError):
        None / ETHAmount("1")


def test_eth_lt_incompatible_type():
    with pytest.raises(TypeError):
        assert ETHAmount("1") < None


def test_eth_le_incompatible_type():
    with pytest.raises(TypeError):
        assert ETHAmount("1") <= None


def test_eth_gt_incompatible_type():
    with pytest.raises(TypeError):
        assert ETHAmount("1") > None


def test_eth_ge_incompatible_type():
    with pytest.raises(TypeError):
        assert ETHAmount("1") >= None


def test_eth_comparison_with_negative():
    assert ETHAmount("-1") == -1
    assert ETHAmount("-1.5") == Decimal("-1.5")
    assert ETHAmount("-1.5") == -1.5
    assert ETHAmount("-1.5") == ETHAmount("-1.5")
    assert ETHAmount("-1") < 0
    assert ETHAmount("-1") < ETHAmount("0")
    assert ETHAmount("-2") <= -1
    assert ETHAmount("-1") >= -2
    assert ETHAmount("-1") > -2
