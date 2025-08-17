from src.common.abstract_component import AbstractComponent
from src.results.results_locators import SORT_BY_DROPDOWN_MENU, SORT_BY_LABEL
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class SortByWidget(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)

    def _get_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, SORT_BY_LABEL)

    def _get_sort_dropdown(self):
        return self.driver.find_element(By.CSS_SELECTOR, SORT_BY_DROPDOWN_MENU)

    def is_displayed(self) -> bool:
        try:
            self.wait.until(
                lambda driver: self._get_label().is_displayed()
                and self._get_sort_dropdown().is_displayed()
            )
            return True
        except TimeoutException:
            return False
