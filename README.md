# Selenium Python Automation Portfolio

[![Selenium Python Tests](https://github.com/LaVieDetoile/selenium-python-automation-portfolio/actions/workflows/selenium-tests.yml/badge.svg)](https://github.com/LaVieDetoile/selenium-python-automation-portfolio/actions/workflows/selenium-tests.yml)

Senior SDET-style Selenium WebDriver + Pytest portfolio for [The Internet](https://the-internet.herokuapp.com).

## Technologies
Python, Selenium WebDriver, Pytest, Page Object Model, explicit waits, pytest-html, Ruff, GitHub Actions.

## Coverage
Login, negative login, checkboxes, dropdowns, dynamic loading, JavaScript alerts, iframes, file upload, and cross-browser CI.

## Install and Run
```bash
poetry install
poetry run pytest
BROWSER=firefox poetry run pytest
poetry run ruff check .
```

## CI/CD
GitHub Actions runs Chrome and Firefox jobs, performs linting, executes tests, and uploads reports.

## Demonstrates
Explicit waits, POM abstraction, fixture-driven browser setup, cross-browser execution, and stable Selenium automation patterns.

## Public Portfolio Disclaimer
This project uses only public demo applications and generated local test data. It contains no company code, credentials, internal URLs, or proprietary logic.
