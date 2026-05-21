import enum


class Currency(enum.StrEnum):
    # crypto
    BTC = "BTC", "Bitcoin", 8
    ETH = "ETH", "Ethereum", 18
    USDC = "USDC", "USD Coin", 6
    USDT = "USDT", "Tether", 6
    # fiat
    USD = "USD", "US Dollar", 2
    EUR = "EUR", "Euro", 2
    JPY = "JPY", "Yen", 0
    GBP = "GBP", "Pound Sterling", 2
    CNY = "CNY", "Yuan", 2
    AUD = "AUD", "Australian Dollar", 2
    CAD = "CAD", "Canadian Dollar", 2
    CHF = "CHF", "Swiss Franc", 2
    HKD = "HKD", "Hong Kong Dollar", 2
    NZD = "NZD", "New Zealand Dollar", 2

    def __new__(cls, code: str, name: str, decimals: int):
        obj = str.__new__(cls, code)
        obj._value_ = code
        obj._code = code
        obj._name = name
        obj._decimals = decimals
        return obj

    @property
    def code(self) -> str:
        return self._code

    @property
    def name(self) -> str:
        return self._name

    @property
    def decimals(self) -> int:
        return self._decimals
