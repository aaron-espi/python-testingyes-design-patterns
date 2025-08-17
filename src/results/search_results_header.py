from src.common.abstract_component import AbstractComponent
from src.results.results_locators import RESULTS_PAGE_BREADCRUMB_NAVIGATION, RESULTS_PAGE_TITLE_TEXT
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class SearchResultsHeader(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)

    def _get_breadcrumb_nav(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, RESULTS_PAGE_BREADCRUMB_NAVIGATION
        )

    def _get_title(self):
        return self.driver.find_element(By.ID, RESULTS_PAGE_TITLE_TEXT)

    def is_displayed(self) -> bool:
        try:
            self.wait.until(
                lambda driver: self._get_breadcrumb_nav().is_displayed()
                and self._get_title().is_displayed()
            )
            return True
        except TimeoutException:
            return False
