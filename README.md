<div align="center">
  <h1>cryptils</h1>
  <div>
    <img src="https://github.com/seba3c/cryptils/actions/workflows/tests.yml/badge.svg" alt="Tests">
    <img src="https://img.shields.io/badge/coverage-100%25-brightgreen" alt="Coverage">
    <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
    <img src="https://img.shields.io/pypi/v/cryptils?include_prereleases=true" alt="PyPI">
    <img src="https://img.shields.io/pypi/v/cryptils?include_prereleases=true&pypi_base=https://test.pypi.org/simple&label=testpypi" alt="TestPyPI">
  </div>
  <em>A utility library for representing cryptocurrency and fiat amounts in Python.</em>
</div>

## Installation

```bash
pip install cryptils
```

## Quick Start

```python
from cryptils import BTCAmount, ETHAmount, USDCAmount, USDTAmount, USDAmount, JPYAmount

# Create amounts with exact decimal precision
btc = BTCAmount("1.5")
print(btc)  # 1.50000000 BTC

eth = ETHAmount("2.0")
print(eth)  # 2.000000000000000000 ETH

# Arithmetic with other amounts
result = BTCAmount("0.5") + BTCAmount("0.25")
print(result)  # 0.75000000 BTC

# Arithmetic with built-in types (int, float, Decimal)
from decimal import Decimal

btc = BTCAmount("1.0")
print(btc + 0.5)  # 1.50000000 BTC (added float)
print(btc + 2)  # 3.00000000 BTC (added int)
print(btc + Decimal("0.5"))  # 1.50000000 BTC (added Decimal)
print(2 * btc)  # 2.00000000 BTC (int * BTC)
print(10 - BTCAmount("2.5"))  # 7.50000000 BTC (int - BTC)

# Different currencies maintain their own precision
usdc = USDCAmount("100")
print(usdc)  # 100.000000 USDC

# Access the raw Decimal value
print(btc.to_decimal())  # Decimal('1.50000000')

# Get the formatted string explicitly
print(btc.to_string())  # BTC 1.50000000

# Fiat amounts with proper precision
usd = USDAmount("99.99")
print(usd)              # 99.99
print(usd.to_string())  # USD 99.99

jpy = JPYAmount("150")
print(jpy)              # 150
print(jpy.to_string())  # JPY 150
```

## Features

- Uses `decimal.Decimal` internally to avoid floating-point errors.
- Consistent precision handling per currency (e.g., 8 decimals for BTC, 6 for USDC).
- Full fiat currency support (USD, EUR, GBP, JPY, etc.) with correct decimal precision.
- Simple, explicit API designed for financial precision.

## Pydantic Support

CurrencyAmount subclasses (crypto and fiat) work as Pydantic v2 field types:

```python
from pydantic import BaseModel
from cryptils import BTCAmount, ETHAmount, USDCAmount, USDAmount


class WalletBalance(BaseModel):
    btc: BTCAmount
    eth: ETHAmount
    usdc: USDCAmount
    usd: USDAmount


wallet = WalletBalance(btc="1.5", eth=2, usdc=100.0, usd="99.99")
print(wallet.model_dump_json())
# {"btc":"1.50000000","eth":"2.000000000000000000","usdc":"100.000000","usd":"99.99"}
```

Requires Pydantic v2 (`pip install pydantic`).

## Development

This project uses [uv](https://docs.astral.sh/uv/) for environment management, [ruff](https://docs.astral.sh/ruff/) for linting and formatting, and [tox](https://tox.wiki/) for testing across Python versions.

```bash
# Setup environment
uv sync

# Run tests
uv run pytest
# Run tests with coverage
uv run pytest --cov

# Run tests across all supported Python versions
uv run tox

# Format and lint
uv run ruff check --fix .
uv run ruff format .

# Install pre-commit hooks
uv run pre-commit install

# Run pre-commit on all files
uv run pre-commit run --all-files
```

## License

This project is licensed under the terms of the [MIT](./LICENSE) license.
