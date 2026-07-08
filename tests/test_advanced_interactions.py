import pytest

from selenium_portfolio.pages.advanced_page import AdvancedPage


@pytest.mark.regression
def test_javascript_alert(driver):
    page = AdvancedPage(driver)
    page.load_alerts()
    text = page.trigger_alert()

    assert text == "I am a JS Alert"
    assert page.result_text() == "You successfully clicked an alert"


@pytest.mark.regression
def test_iframe_text(driver):
    page = AdvancedPage(driver)
    page.load_frames()

    assert page.replace_frame_text("Selenium frame coverage") == "Selenium frame coverage"
