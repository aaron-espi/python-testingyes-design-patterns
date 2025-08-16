from common.search_widget import SearchWidget
from common.product_grid import ProductGrid
from common.top_bar import TopBar
from config.environment_config import BASE_URL


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.top_bar = TopBar(driver)
        self.search_widget = SearchWidget(driver)
        self.product_grid = ProductGrid(driver)

    def go_to(self):
        self.driver.get(BASE_URL)

    def get_top_bar(self):
        return self.top_bar

    def get_search_widget(self):
        return self.search_widget

    def get_product_grid(self):
        return self.product_grid
