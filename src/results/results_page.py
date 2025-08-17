from common.product_grid import ProductGrid
from common.search_widget import SearchWidget
from results.no_results_pannel import NoResultsPanel
from results.sort_by_widget import SortByWidget
from results.search_results_header import SearchResultsHeader


class ResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_grid = ProductGrid(driver)
        self.search_widget = SearchWidget(driver)
        self.no_results_panel = NoResultsPanel(driver)
        self.sort_by_widget = SortByWidget(driver)
        self.search_results_header = SearchResultsHeader(driver)
