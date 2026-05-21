from decimal import Decimal

import pytest

from cryptils import ETH, BTCAmount


def test_eth_name():
    assert ETH(0).name == "Ethereum"


def test_eth_code():
    assert ETH(0).code == "ETH"


def test_eth_new_instance():
    assert ETH("1.5") == ETH(1.5)
    assert ETH("1") == ETH(1)
    assert ETH("1.5") == ETH(Decimal("1.5"))


def test_eth_precision():
    assert ETH("1.0000000000000000011") == ETH("1.000000000000000001")
    assert ETH("1.0000000000000000014") == ETH("1.000000000000000001")
    assert ETH("1.00000000000000000149") == ETH("1.000000000000000001")
    assert ETH("1.0000000000000000015") == ETH("1.000000000000000002")
    assert ETH("1.0000000000000000019") == ETH("1.000000000000000002")
    assert ETH("1.00000000000000000199") == ETH("1.000000000000000002")


def test_eth_str():
    assert str(ETH("1.5")) == "1.500000000000000000"


def test_eth_repr():
    assert repr(ETH("1.5")) == "ETH(1.500000000000000000)"


def test_eth_hash():
    assert hash(ETH("1.5")) == hash(ETH("1.5"))
    assert hash(ETH("1.5")) == hash(ETH("1.50"))
    assert hash(ETH("1.5")) == hash(ETH(1.5))
    assert hash(ETH("1.5")) != hash(ETH("1.0"))


def test_eth_to_string():
    assert ETH("1.5").to_string() == "ETH 1.500000000000000000"


def test_eth_to_decimal():
    assert ETH("1.5").to_decimal() == Decimal("1.50000000000000000")


def test_eth_to_float():
    assert ETH("1.5").to_float() == 1.50000000000000000


def test_eth_addition_same_class():
    assert ETH("0.5") + ETH("0.5") == ETH("1.0")


def test_eth_addition_with_int():
    assert ETH("0.5") + 1 == ETH("1.5")


def test_eth_addition_with_decimal():
    assert ETH("0.5") + Decimal("0.5") == ETH("1.0")


def test_eth_addition_with_float():
    assert ETH("0.5") + 0.5 == ETH("1.0")


def test_eth_addition_with_str_raises():
    with pytest.raises(TypeError):
        ETH("0.5") + "0.5"


def test_eth_reverse_addition_with_int():
    assert 1 + ETH("0.5") == ETH("1.5")


def test_eth_subtraction_same_class():
    assert ETH("1.5") - ETH("0.5") == ETH("1.0")


def test_eth_subtraction_with_int():
    assert ETH("1.5") - 1 == ETH("0.5")


def test_eth_subtraction_with_decimal():
    assert ETH("1.5") - Decimal("0.5") == ETH("1.0")


def test_eth_subtraction_with_float():
    assert ETH("1.5") - 0.5 == ETH("1.0")


def test_eth_subtraction_with_str_raises():
    with pytest.raises(TypeError):
        ETH("1.5") - "0.5"


def test_eth_reverse_subtraction_with_int():
    assert 2 - ETH("0.5") == ETH("1.5")


def test_eth_multiplication_with_int():
    assert ETH("1") * 2 == ETH("2")


def test_eth_multiplication_with_decimal():
    assert ETH("1") * Decimal("2") == ETH("2")


def test_eth_multiplication_with_float():
    assert ETH("1") * 2.0 == ETH("2")


def test_eth_multiplication_with_str_raises():
    with pytest.raises(TypeError):
        ETH("1") * "2"


def test_eth_reverse_multiplication_with_int():
    assert 2 * ETH("1") == ETH("2")


def test_eth_multiplication_same_class_raises():
    with pytest.raises(TypeError):
        ETH("1") * ETH("2")


def test_eth_division_with_int():
    assert ETH("2") / 2 == ETH("1")


def test_eth_division_with_decimal():
    assert ETH("2") / Decimal("2") == ETH("1")


def test_eth_division_with_float():
    assert ETH("2") / 2.0 == ETH("1")


def test_eth_division_with_str_raises():
    with pytest.raises(TypeError):
        ETH("2") / "2"


def test_eth_reverse_division_with_int():
    assert 2 / ETH("2") == ETH("1")


def test_eth_division_same_class_raises():
    with pytest.raises(TypeError):
        ETH("2") / ETH("1")


def test_eth_equality_with_int():
    assert ETH("1") == 1
    assert (ETH("1") == 2) is False


def test_eth_equality_with_decimal():
    assert ETH("1.5") == Decimal("1.5")
    assert (ETH("1.5") == Decimal("2.5")) is False


def test_eth_equality_with_float():
    assert ETH("1.5") == 1.5
    assert (ETH("1.5") == 2.5) is False


def test_eth_equality_with_str():
    assert (ETH("1.5") == "1.5") is False
    assert (ETH("1.5") == "2.5") is False


def test_eth_equality_with_same_class():
    assert ETH("1.5") == ETH("1.5")
    assert (ETH("1.5") == ETH("2.5")) is False


def test_eth_equality_with_different_class():
    assert (ETH("1.5") == BTCAmount("1.5")) is False
    assert (BTCAmount("1.5") == ETH("1.5")) is False


def test_eth_inequality_with_int():
    assert ETH("1") != 2
    assert (ETH("1") != 1) is False


def test_eth_less_than_with_int():
    assert ETH("1") < 2
    assert not ETH("1") < 1


def test_eth_less_than_with_decimal():
    assert ETH("1") < Decimal("2")
    assert not ETH("1") < Decimal("1")


def test_eth_less_than_with_float():
    assert ETH("1") < 2.0
    assert not ETH("1") < 1.0


def test_eth_less_than_with_str_raises():
    with pytest.raises(TypeError):
        assert ETH("1") < "2"


def test_eth_less_than_with_same_class():
    assert ETH("1") < ETH("2")
    assert not ETH("1") < ETH("1")


def test_eth_less_than_or_equal_with_int():
    assert ETH("1") <= 1
    assert ETH("1") <= 2
    assert not ETH("2") <= 1


def test_eth_greater_than_with_int():
    assert ETH("2") > 1
    assert not ETH("1") > 1


def test_eth_greater_than_with_decimal():
    assert ETH("2") > Decimal("1")
    assert not ETH("1") > Decimal("1")


def test_eth_greater_than_with_float():
    assert ETH("2") > 1.0
    assert not ETH("1") > 1.0


def test_eth_greater_than_with_str_raises():
    with pytest.raises(TypeError):
        assert ETH("2") > "1"


def test_eth_greater_than_with_same_class():
    assert ETH("2") > ETH("1")
    assert not ETH("1") > ETH("1")


def test_eth_greater_than_or_equal_with_int():
    assert ETH("1") >= 1
    assert ETH("2") >= 1
    assert not ETH("1") >= 2


def test_eth_comparison_with_zero():
    assert ETH("0") == 0
    assert ETH("0") == Decimal("0")
    assert ETH("0") == 0.0
    assert ETH("0") == ETH("0")
    assert ETH("1") > 0
    assert ETH("-1") < 0
    assert ETH("0") >= 0
    assert ETH("0") <= 0


def test_eth_add_incompatible_type():
    with pytest.raises(TypeError):
        ETH("1") + None


def test_eth_sub_incompatible_type():
    with pytest.raises(TypeError):
        ETH("1") - None


def test_eth_rsub_incompatible_type():
    with pytest.raises(TypeError):
        None - ETH("1")


def test_eth_mul_incompatible_type():
    with pytest.raises(TypeError):
        ETH("1") * None


def test_eth_truediv_incompatible_type():
    with pytest.raises(TypeError):
        ETH("1") / None


def test_eth_rtruediv_incompatible_type():
    with pytest.raises(TypeError):
        None / ETH("1")


def test_eth_lt_incompatible_type():
    with pytest.raises(TypeError):
        assert ETH("1") < None


def test_eth_le_incompatible_type():
    with pytest.raises(TypeError):
        assert ETH("1") <= None


def test_eth_gt_incompatible_type():
    with pytest.raises(TypeError):
        assert ETH("1") > None


def test_eth_ge_incompatible_type():
    with pytest.raises(TypeError):
        assert ETH("1") >= None


def test_eth_comparison_with_negative():
    assert ETH("-1") == -1
    assert ETH("-1.5") == Decimal("-1.5")
    assert ETH("-1.5") == -1.5
    assert ETH("-1.5") == ETH("-1.5")
    assert ETH("-1") < 0
    assert ETH("-1") < ETH("0")
    assert ETH("-2") <= -1
    assert ETH("-1") >= -2
    assert ETH("-1") > -2
