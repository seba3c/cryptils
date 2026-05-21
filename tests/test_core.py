import pytest

from cryptils._core import CurrencyAmount
from cryptils._crypto import CryptoAmount
from cryptils._fiat import FiatAmount


def test_crypto_amount_cannot_be_instantiated():
    with pytest.raises(TypeError, match="CryptoAmount is an abstract class"):
        CryptoAmount("1")


def test_currency_amount_cannot_be_instantiated():
    with pytest.raises(TypeError, match="CurrencyAmount is an abstract class"):
        CurrencyAmount("1")


def test_fiat_amount_cannot_be_instantiated():
    with pytest.raises(TypeError, match="FiatAmount is an abstract class"):
        FiatAmount("1")
