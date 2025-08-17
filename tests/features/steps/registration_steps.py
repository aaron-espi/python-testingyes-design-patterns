from behave import when, then, given
from tests.core.driver_manager import DriverManager
from src.main.main_page import MainPage
from src.login.login_page import LoginPage
from src.registration.registration_page import RegistrationPage
from tests.utils.model.test_user import TestUser
from tests.utils.factory.email_factory import EmailFactory
from tests.constants.registration_constants import ALREADY_USED_EMAIL_ERROR
from tests.constants.search_constants import (
    FIRST_NAME_FIELD,
    BIRTHDAY_FIELD,
    LAST_NAME_FIELD,
    PASSWORD_FIELD,
)


@given("the user is on the registration page")
def navigate_to_registration_page(context):
    driver = DriverManager.get_driver()

    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to()
    assert main_page.product_grid.is_displayed()

    main_page.top_bar.go_to_login()
    assert login_page.login_form.is_displayed()

    login_page.login_form.create_account()
    assert registration_page.registration_form.is_displayed()

    context.driver = driver
    context.main_page = main_page
    context.login_page = login_page
    context.registration_page = registration_page


@when("the user fills in the form with the following data")
def fill_form_with_data(context):
    data = context.table.as_dicts()
    row = data[0]

    first_name = row[FIRST_NAME_FIELD]
    last_name = row[LAST_NAME_FIELD]
    birthday = row[BIRTHDAY_FIELD]
    password = row[PASSWORD_FIELD]

    registration_page = context.registration_page

    registration_page.registration_form.check_social_title_mr()
    registration_page.registration_form.type_first_name(first_name)
    registration_page.registration_form.type_last_name(last_name)
    registration_page.registration_form.type_birthday(birthday)
    registration_page.registration_form.type_password(password)
    registration_page.registration_form.check_terms_and_privacy()

    context.user = TestUser(first_name, last_name, None, password, birthday)


@when("uses a unique email address")
def fill_with_unique_email(context):
    email = EmailFactory.generate_unique_email()
    context.registration_page.registration_form.type_email(email)
    context.user.email = email


@when("submits the registration form")
def submit_registration_form(context):
    context.registration_page.registration_form.save_customer()


@then("the user is redirected to the main page")
def should_be_redirected_to_main_page(context):
    assert context.main_page.product_grid.is_displayed()


@then("they should see their name displayed in the top bar")
def should_see_name_in_top_bar(context):
    expected_name = f"{context.user.first_name} {context.user.last_name}"
    assert expected_name == context.main_page.top_bar.get_logged_in_username()


@when("uses an already registered email address")
def fill_in_already_used_email(context):
    email = EmailFactory.already_used_email()
    context.registration_page.registration_form.type_email(email)
    context.user.email = email


@then("the user is informed that the email is already in use")
def should_see_email_error_message(context):
    error_message = context.registration_page.registration_form.get_error_message_text()
    assert error_message == ALREADY_USED_EMAIL_ERROR


@then("the registration should not be completed")
def still_in_registration_page(context):
    assert context.registration_page.registration_form.is_displayed()
