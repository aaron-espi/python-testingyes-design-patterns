from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait


class AbstractComponent(ABC):
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @abstractmethod
    def is_displayed(self) -> bool:
        pass
