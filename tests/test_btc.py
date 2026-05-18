from cryptils import BTC, Sats


def test_btc_str():
    assert str(BTC("1.5")) == "1.50000000 BTC"


def test_btc_to_sats():
    assert BTC("1.0").to_sats() == Sats(100_000_000)


def test_sats_to_btc():
    assert Sats(50_000_000).to_btc() == BTC("0.5")


def test_btc_addition():
    assert BTC("0.5") + BTC("0.5") == BTC("1.0")
