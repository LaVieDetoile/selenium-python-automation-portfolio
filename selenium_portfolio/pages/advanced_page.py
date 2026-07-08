from __future__ import annotations

from selenium.webdriver.common.by import By

from selenium_portfolio.pages.base_page import BasePage


class AdvancedPage(BasePage):
    ALERT_BUTTON = (By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    RESULT = (By.ID, "result")
    IFRAME = (By.ID, "mce_0_ifr")
    BODY = (By.ID, "tinymce")

    def load_alerts(self) -> None:
        self.open("/javascript_alerts")

    def trigger_alert(self) -> str:
        self.clickable(self.ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def result_text(self) -> str:
        return self.visible(self.RESULT).text

    def load_frames(self) -> None:
        self.open("/iframe")

    def replace_frame_text(self, text: str) -> str:
        self.driver.switch_to.frame(self.visible(self.IFRAME))
        body = self.visible(self.BODY)
        self.driver.execute_script("arguments[0].innerText = arguments[1];", body, text)
        actual_text = body.text
        self.driver.switch_to.default_content()
        return actual_text
