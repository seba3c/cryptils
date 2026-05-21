# Agent Context for cryptils

## Project Overview
`cryptils` is a small Python utility library for representing cryptocurrency and fiat amounts with proper decimal precision. It provides currency-specific classes (crypto: BTC, ETH, USDC, USDT; fiat: USD, EUR, JPY, GBP, CNY, AUD, CAD, CHF, HKD, NZD) built on shared abstract bases.

## Architecture
- **Source layout**: `src/cryptils/`
- **Core class**: `CurrencyAmount` (`_core.py`) — abstract base handling decimals, arithmetic, comparisons, hashing, string formatting, and Pydantic v2 integration.
- **Currency hierarchy**: `CryptoAmount` (`_crypto.py`) and `FiatAmount` (`_fiat.py`) are intermediate abstract bases. Concrete classes (e.g. `BTCAmount`, `USDAmount`) are thin subclasses setting `_currency` to a `Currency` enum member.
- **Currency enum**: `_currency.py` defines all currencies (crypto + fiat) with `code`, `name`, and `decimals`.
- **Public API**: `__init__.py` exports all concrete classes with an explicit `__all__`.
- **Type hints**: `py.typed` marker file is included for PEP 561 compliance.

## Build & Tooling
- **Environment**: [uv](https://docs.astral.sh/uv/) is the primary environment manager (`uv sync`, `uv run`).
- **Python**: >= 3.11 (default dev version pinned in `.python-version` as `3.13`).
- **Test matrix**: tox with tox-uv (`py311`, `py312`, `py313`, `coverage`).
- **Lint / format**: ruff (target Python 3.11, line length 100).
  - Selected rules: `E`, `F`, `I`, `W`, `UP`, `B`, `C4`, `SIM`, `S`, `A`, `BLE`, `N`, `PLE`, `PLW`, `RET`, `ARG`, `RUF`.
  - Ignored: `S101` (assert for pytest), `UP037` (keep quotes in type annotations).
- **Pre-commit**: `.pre-commit-config.yaml` runs ruff (check + format) and basic pre-commit hooks (trailing-whitespace, end-of-file-fixer, check-yaml, check-added-large-files).
- **Coverage**: 90% minimum (`tool.coverage.report.fail_under`).
- **CI/CD**: GitHub Actions workflows for tests (`tests.yml`) and PyPI publishing (`publish-pypi.yml`, `publish-testpypi.yml`).

## Dependency Management
- **Runtime dependencies**: none (empty `dependencies` in `pyproject.toml`).
- **Optional test deps**: `[project.optional-dependencies] test` includes `pydantic>=2.0`, `pytest>=8.0`, `pytest-cov>=4.0`, `tox>=4.0`.
- **Dev deps**: `[dependency-groups] dev` (uv feature) includes the above plus `pre-commit>=3.0`, `ruff>=0.15.13`, `tox-uv>=1.0`.
- **Tox environments** use `extras = test` rather than manual `deps` lists.

## Coding Conventions
- Use `from __future__ import annotations`.
- Follow existing ruff rules (see Build & Tooling).
- Currency classes are thin subclasses of `CryptoAmount` or `FiatAmount`; put shared logic in `_core.py`.
- Pydantic integration lives in `_core.py` and uses a lazy import of `pydantic_core` at the top of the module so the library works without Pydantic installed.
- Tests exist per currency class plus `test_core.py` and `test_pydantic.py`.

## Important Notes
- `CurrencyAmount` cannot be instantiated directly (raises `TypeError`).
- `CryptoAmount` and `FiatAmount` are also abstract and cannot be instantiated directly.
- Arithmetic between two instances of the same class is allowed; cross-currency operations are not.
- Multiplying or dividing two currency instances is prohibited.
- Decimal quantization uses each currency's `_decimals` class variable.
- Instances expose `name`, `code`, and `decimals` properties.
- `str(instance)` returns the raw decimal value (e.g., `"1.50000000"`); `to_string()` returns `"BTC 1.50000000"` (code + value).
- JPY uses 0 decimal places; all other fiat currencies use 2.
- Pydantic validation accepts `str`, `int`, `float`, `Decimal`, or an instance of the same currency class. Cross-currency instances raise `ValidationError`.
