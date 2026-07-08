from __future__ import annotations

from selenium.webdriver.common.by import By

from selenium_portfolio.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def load(self) -> None:
        self.open("/login")

    def login(self, username: str, password: str) -> None:
        self.visible(self.USERNAME).send_keys(username)
        self.visible(self.PASSWORD).send_keys(password)
        self.clickable(self.SUBMIT).click()

    def flash_message(self) -> str:
        return self.visible(self.FLASH).text
