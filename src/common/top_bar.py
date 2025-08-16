from abstract_component import AbstractComponent
from selenium.webdriver.common.by import By
from common_locators import LOGIN_LINK, LOGGED_IN_USERNAME_TEXT
from selenium.common.exceptions import TimeoutException


class TopBar(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)

    def _get_login_link(self):
        return self.driver.find_element(By.ID, LOGIN_LINK)

    def _get_username_text(self):
        return self.driver.find_element(By.ID, LOGGED_IN_USERNAME_TEXT)

    def go_to_login(self):
        self._get_login_link().click()

    def get_logged_in_username(self):
        return self._get_username_text().text.strip()

    def is_displayed(self):
        try:
            self.wait.until(lambda driver: self._get_login_link().is_displayed())
            return True
        except TimeoutException:
            return False
