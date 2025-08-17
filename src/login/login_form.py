from src.common.abstract_component import AbstractComponent
from src.common.common_locators import EMAIL_INPUT, PASSWORD_INPUT
from src.login.login_locators import LOGIN_BUTTON, REGISTER_LINK
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class LoginForm(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)

    def _get_email_input(self):
        return self.driver.find_element(By.NAME, EMAIL_INPUT)

    def _get_password_input(self):
        return self.driver.find_element(By.NAME, PASSWORD_INPUT)

    def _get_login_button(self):
        return self.driver.find_element(By.ID, LOGIN_BUTTON)

    def _get_register_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, REGISTER_LINK)

    def create_account(self):
        self._get_register_link().click()

    def is_displayed(self):
        try:
            self.wait.until(
                lambda driver: self._get_email_input().is_displayed()
                and self._get_password_input().is_displayed()
                and self._get_login_button().is_displayed()
            )
            return True
        except TimeoutException:
            return False
