from __future__ import annotations

from pathlib import Path

from selenium.webdriver.common.by import By

from selenium_portfolio.pages.base_page import BasePage


class ElementsPage(BasePage):
    CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes input")
    DROPDOWN = (By.ID, "dropdown")
    START = (By.CSS_SELECTOR, "#start button")
    FINISH = (By.ID, "finish")
    FILE_INPUT = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILES = (By.ID, "uploaded-files")

    def load_checkboxes(self) -> None:
        self.open("/checkboxes")

    def load_dropdown(self) -> None:
        self.open("/dropdown")

    def load_dynamic_loading(self) -> None:
        self.open("/dynamic_loading/1")

    def load_upload(self) -> None:
        self.open("/upload")

    def checkbox_states(self) -> list[bool]:
        return [box.is_selected() for box in self.elements(self.CHECKBOXES)]

    def toggle_first_checkbox(self) -> None:
        self.elements(self.CHECKBOXES)[0].click()

    def select_dropdown_value(self, value: str) -> None:
        from selenium.webdriver.support.ui import Select

        Select(self.visible(self.DROPDOWN)).select_by_value(value)

    def selected_dropdown_text(self) -> str:
        from selenium.webdriver.support.ui import Select

        return Select(self.visible(self.DROPDOWN)).first_selected_option.text

    def start_dynamic_loading(self) -> None:
        self.clickable(self.START).click()

    def finish_text(self) -> str:
        return self.visible(self.FINISH).text

    def upload_file(self, file_path: Path) -> None:
        self.visible(self.FILE_INPUT).send_keys(str(file_path))
        self.clickable(self.UPLOAD_BUTTON).click()

    def uploaded_file_name(self) -> str:
        return self.visible(self.UPLOADED_FILES).text
