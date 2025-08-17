from src.common.product_grid import ProductGrid
from src.common.search_widget import SearchWidget
from src.results.no_results_pannel import NoResultsPanel
from src.results.sort_by_widget import SortByWidget
from src.results.search_results_header import SearchResultsHeader


class ResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_grid = ProductGrid(driver)
        self.search_widget = SearchWidget(driver)
        self.no_results_panel = NoResultsPanel(driver)
        self.sort_by_widget = SortByWidget(driver)
        self.search_results_header = SearchResultsHeader(driver)
