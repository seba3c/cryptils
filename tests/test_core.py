import pytest

from cryptils.core import CryptoAmount


def test_crypto_amount_cannot_be_instantiated():
    with pytest.raises(TypeError, match="CryptoAmount is an abstract class"):
        CryptoAmount("1")
