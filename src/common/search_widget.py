from abstract_component import AbstractComponent
from selenium.webdriver.common.by import By
from common_locators import HEADER_SEARCH_INPUT, HEADER_SEARCH_BUTTON
from selenium.common.exceptions import TimeoutException


class SearchWidget(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)

    def _get_search_input(self):
        return self.driver.find_element(By.NAME, HEADER_SEARCH_INPUT)

    def _get_search_button(self):
        return self.driver.find_element(By.XPATH, HEADER_SEARCH_BUTTON)

    def type_search_query(self, query):
        self._get_search_input().clear()
        self._get_search_input().sendKeys(query)

    def click_search_button(self):
        self._get_search_button().click()

    def is_displayed(self) -> bool:
        try:
            self.wait.until(
                lambda driver: self._get_search_input().is_displayed()
                and self._get_search_button().is_displayed()
            )
            return True
        except TimeoutException:
            return False
