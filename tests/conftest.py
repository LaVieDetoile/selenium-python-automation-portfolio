from __future__ import annotations

from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium_portfolio.config.settings import settings


@pytest.fixture()
def driver():
    if settings.browser == "firefox":
        options = FirefoxOptions()
        if settings.headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        if settings.headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    driver.set_window_size(1440, 900)
    yield driver
    driver.quit()


@pytest.fixture()
def upload_file(tmp_path: Path) -> Path:
    file_path = tmp_path / "portfolio-upload.txt"
    file_path.write_text("Public-safe Selenium upload fixture", encoding="utf-8")
    return file_path
