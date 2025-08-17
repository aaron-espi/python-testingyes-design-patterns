from src.common.abstract_component import AbstractComponent
from src.results.results_locators import (
    NO_RESULTS_TITLE_TEXT,
    NO_RESULTS_SUGGESTION_TEXT,
    NO_RESULTS_SEARCH_INPUT,
)
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class NoResultsPanel(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)

    def _get_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, NO_RESULTS_TITLE_TEXT)

    def _get_suggestion(self):
        return self.driver.find_element(By.CSS_SELECTOR, NO_RESULTS_SUGGESTION_TEXT)

    def _get_search_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, NO_RESULTS_SEARCH_INPUT)

    def get_title_text(self):
        return self._get_title().text.strip()

    def get_suggestion_text(self):
        return self._get_suggestion().text.strip()

    def is_displayed(self) -> bool:
        try:
            self.wait.until(
                lambda driver: self._get_title().is_displayed()
                and self._get_suggestion().is_displayed()
                and self._get_search_input().is_displayed()
            )
            return True
        except TimeoutException:
            return False
