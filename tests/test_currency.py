from cryptils import Currency


def test_currency_comparison():
    assert Currency.BTC == Currency.BTC
    assert Currency.BTC != Currency.ETH
    assert Currency.BTC == "BTC"
    assert Currency.BTC == "BTC"
