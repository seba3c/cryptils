# cryptils

A precise utility library for representing cryptocurrency amounts in Python.

## Installation

```bash
pip install cryptils
```

## Quick Start

```python
from cryptils import BTC, Sats

# Create BTC amounts with exact decimal precision
btc = BTC("1.5")
print(btc)  # 1.50000000 BTC

# Convert between BTC and satoshis
sats = btc.to_sats()
print(sats)  # 150000000 sats

# Convert back
back_to_btc = sats.to_btc()
print(back_to_btc)  # 1.50000000 BTC

# Arithmetic
result = BTC("0.5") + BTC("0.25")
print(result)  # 0.75000000 BTC
```

## Features

- Uses `decimal.Decimal` internally to avoid floating-point errors.
- Type-safe conversions between units (e.g., BTC and Satoshis).
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

MIT
