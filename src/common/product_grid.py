from src.common.abstract_component import AbstractComponent
from selenium.webdriver.common.by import By
from src.common.common_locators import PRODUCT_ITEMS, PRODUCT_TITLE_TEXT
from selenium.common.exceptions import TimeoutException


class ProductGrid(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)

    def _get_product_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, PRODUCT_ITEMS)

    def select_product_by_index(self, index):
        self._get_product_items()[index].click()

    def contains_products_matching_query(self, query):
        return any(
            query.lower()
            in item.find_element(By.CSS_SELECTOR, PRODUCT_TITLE_TEXT).text.lower()
            for item in self._get_product_items()
        )

    def is_displayed(self) -> bool:
        try:
            self.wait.until(
                lambda driver: len(self._get_product_items()) != 0
                and self._get_product_items()[0].is_displayed()
            )
            return True
        except TimeoutException:
            return False
