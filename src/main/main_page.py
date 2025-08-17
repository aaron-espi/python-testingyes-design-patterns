from src.common.top_bar import TopBar
from src.common.search_widget import SearchWidget
from src.common.product_grid import ProductGrid
from src.config.environment_config import BASE_URL


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.top_bar = TopBar(driver)
        self.search_widget = SearchWidget(driver)
        self.product_grid = ProductGrid(driver)

    def go_to(self):
        self.driver.get(BASE_URL)
