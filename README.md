# cryptils

![Tests](https://github.com/seba3c/cryptils/actions/workflows/tests.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![PyPI](https://img.shields.io/pypi/v/cryptils)
![TestPyPI](https://img.shields.io/badge/testpypi-v0.1.0a1-blue)

An utility library for representing cryptocurrency amounts in Python.

## Installation

```bash
pip install cryptils
```

## Quick Start

```python
from cryptils import BTC, ETH, USDC, USDT

# Create amounts with exact decimal precision
btc = BTC("1.5")
print(btc)  # 1.50000000 BTC

eth = ETH("2.0")
print(eth)  # 2.000000000000000000 ETH

# Arithmetic
result = BTC("0.5") + BTC("0.25")
print(result)  # 0.75000000 BTC

# Different currencies maintain their own precision
usdc = USDC("100")
print(usdc)  # 100.000000 USDC

# Access the raw Decimal value
print(btc.as_decimal())  # Decimal('1.50000000')

# Get the formatted string explicitly
print(btc.to_string())  # 1.50000000 BTC
```

## Features

- Uses `decimal.Decimal` internally to avoid floating-point errors.
- Consistent precision handling per currency (e.g., 8 decimals for BTC, 6 for USDC).
- Simple, explicit API designed for financial precision.

## Development

This project uses [uv](https://docs.astral.sh/uv/) for environment management, [ruff](https://docs.astral.sh/ruff/) for linting and formatting, and [tox](https://tox.wiki/) for testing across Python versions.

```bash
# Setup environment
uv sync

# Run tests
uv run pytest

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

[MIT](./LICENSE)
