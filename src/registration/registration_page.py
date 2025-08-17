from src.registration.registration_form import RegistrationForm


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.registration_form = RegistrationForm(driver)
