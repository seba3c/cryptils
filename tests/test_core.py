import pytest

from cryptils._core import CurrencyAmount
from cryptils._crypto import CryptoAmount


def test_crypto_amount_cannot_be_instantiated():
    with pytest.raises(TypeError, match="CryptoAmount is an abstract class"):
        CryptoAmount("1")


def test_currency_amount_cannot_be_instantiated():
    with pytest.raises(TypeError, match="CurrencyAmount is an abstract class"):
        CurrencyAmount("1")
