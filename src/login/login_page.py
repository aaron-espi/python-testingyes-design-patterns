from src.login.login_form import LoginForm


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_form = LoginForm(driver)
