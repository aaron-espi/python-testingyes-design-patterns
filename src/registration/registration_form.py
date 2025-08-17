from common.abstract_component import AbstractComponent
from common.common_locators import EMAIL_INPUT, PASSWORD_INPUT
from registration_locators import (
    BIRTHDAY_INPUT,
    ERROR_MESSAGE,
    FIRSTNAME_INPUT,
    LASTNAME_INPUT,
    NEWSLETTER_CHECK,
    RECEIVE_OFFERS_CHECK,
    SAVE_BUTTON,
    SOCIAL_TITLE_MR_RADIO,
    SOCIAL_TITLE_MRS_RADIO,
    TERMS_AND_PRIVACY_CHECK,
)
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class RegistrationForm(AbstractComponent):
    def __init__(self, driver):
        super().__init__(driver)

    def _get_social_title_mr(self):
        return self.driver.find_element(By.CSS_SELECTOR, SOCIAL_TITLE_MR_RADIO)

    def _get_social_title_mrs(self):
        return self.driver.find_element(By.CSS_SELECTOR, SOCIAL_TITLE_MRS_RADIO)

    def _get_first_name(self):
        return self.driver.find_element(By.NAME, FIRSTNAME_INPUT)

    def _get_last_name(self):
        return self.driver.find_element(By.NAME, LASTNAME_INPUT)

    def _get_email(self):
        return self.driver.find_element(By.NAME, EMAIL_INPUT)

    def _get_password(self):
        return self.driver.find_element(By.NAME, PASSWORD_INPUT)

    def _get_birthday(self):
        return self.driver.find_element(By.NAME, BIRTHDAY_INPUT)

    def _get_receive_offers(self):
        return self.driver.find_element(By.NAME, RECEIVE_OFFERS_CHECK)

    def _get_newsletter_signup(self):
        return self.driver.find_element(By.NAME, NEWSLETTER_CHECK)

    def _get_terms_and_privacy(self):
        return self.driver.find_element(By.NAME, TERMS_AND_PRIVACY_CHECK)

    def _get_save_button(self):
        return self.driver.find_element(By.XPATH, SAVE_BUTTON)

    def _get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, ERROR_MESSAGE)

    def check_social_title_mr(self):
        self._get_social_title_mr().click()

    def check_social_title_mrs(self):
        self._get_social_title_mrs().click()

    def type_first_name(self, first_name):
        self._get_first_name().send_keys(first_name)

    def type_last_name(self, last_name):
        self._get_last_name().send_keys(last_name)

    def type_email(self, email):
        email_input = self._get_email()
        email_input.clear()
        email_input.send_keys(email)

    def type_password(self, password):
        self._get_password().send_keys(password)

    def type_birthday(self, birthday):
        self._get_birthday().send_keys(birthday)

    def check_receive_offers(self):
        self._get_receive_offers().click()

    def check_newsletter_signup(self):
        self._get_newsletter_signup().click()

    def check_terms_and_privacy(self):
        self._get_terms_and_privacy().click()

    def save_customer(self):
        self._get_save_button().click()

    def get_error_message_text(self):
        return self._get_error_message().text.strip()

    def is_displayed(self) -> bool:
        try:
            self.wait.until(
                lambda driver: self._get_first_name().is_displayed()
                and self._get_email().is_displayed()
                and self._get_password().is_displayed()
                and self._get_save_button().is_displayed()
            )
            return True
        except TimeoutException:
            return False
