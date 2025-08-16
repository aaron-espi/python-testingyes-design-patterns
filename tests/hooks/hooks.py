from tests.core.driver_manager import DriverManager


def before_scenario(context, scenario):
    DriverManager.init_driver()
    context.driver = DriverManager.get_driver()


def after_scenario(context, scenario):
    DriverManager.quit_driver()
