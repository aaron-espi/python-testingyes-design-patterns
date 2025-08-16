from login_form import LoginForm


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_form = LoginForm(driver)

    def get_login_form(self):
        return self.login_form
