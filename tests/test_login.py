import pytest

from selenium_portfolio.pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area" in page.flash_message()


@pytest.mark.negative
def test_invalid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("invalid", "wrong")

    assert "Your username is invalid" in page.flash_message()
