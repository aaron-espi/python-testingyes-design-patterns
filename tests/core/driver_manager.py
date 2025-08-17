import threading
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class DriverManager:
    _thread_local = threading.local()

    @staticmethod
    def init_driver():
        if (
            not hasattr(DriverManager._thread_local, "driver")
            or DriverManager._thread_local.driver is None
        ):
            service = Service(GeckoDriverManager().install())
            DriverManager._thread_local.driver = webdriver.Firefox(service=service)

    @staticmethod
    def get_driver():
        return getattr(DriverManager._thread_local, "driver", None)

    @staticmethod
    def quit_driver():
        driver = getattr(DriverManager._thread_local, "driver", None)
        if driver is not None:
            driver.quit()
            DriverManager._thread_local.driver = None
