import pytest

from selenium_portfolio.pages.elements_page import ElementsPage


@pytest.mark.regression
def test_checkboxes(driver):
    page = ElementsPage(driver)
    page.load_checkboxes()
    before = page.checkbox_states()
    page.toggle_first_checkbox()
    after = page.checkbox_states()

    assert before[0] is False and after[0] is True


@pytest.mark.regression
def test_dropdown(driver):
    page = ElementsPage(driver)
    page.load_dropdown()
    page.select_dropdown_value("2")

    assert page.selected_dropdown_text() == "Option 2"


@pytest.mark.regression
def test_dynamic_loading(driver):
    page = ElementsPage(driver)
    page.load_dynamic_loading()
    page.start_dynamic_loading()

    assert page.finish_text() == "Hello World!"


@pytest.mark.regression
def test_file_upload(driver, upload_file):
    page = ElementsPage(driver)
    page.load_upload()
    page.upload_file(upload_file)

    assert page.uploaded_file_name() == upload_file.name
