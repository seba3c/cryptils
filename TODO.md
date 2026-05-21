# ROADMAP

* Rename classes adding Amount postfix i.e., BTC → BTCAmount
* Add enum to represent currencies global data

````python
import enum

class Currency(enum.StrEnum):
    BTC = "BTC"
    USD = "USD"
    ...
````

* Rename CryptoAmount to CurrencyAmount
* Add support for FIAT most common currencies: USD, EUR, CHF, GBP, JPY
* Add support for json libraries encoding
  * json
  * simplejson
  * ujson
  * orjson
* Add support for BTC units like SAT, MSAT, etc
