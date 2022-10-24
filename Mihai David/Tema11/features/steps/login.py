import time

from behave import *

@given("I am on the login page")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(1)

@when("I click the auth form menu")
def step_impl(context):
    form_auth = context.browser.access_form_auth()
    form_auth.click()
    time.sleep(2)


@when("I enter a incorrect username")
def step_impl(context):
    context.browser.enter_username("username")


@when("I enter a incorrect password")
def step_impl(context):
    context.browser.enter_password("password")


@when("I enter a correct username")
def step_impl(context):
    context.browser.enter_username("tomsmith")


@when("I enter a correct password")
def step_impl(context):
    context.browser.enter_password("SuperSecretPassword!")


@when("I click the login button")
def step_impl(context):
    context.browser.click_login()
    time.sleep(1)


@when("I click the logout button")
def step_impl(context):
    context.browser.click_logout()
    time.sleep(1)


@then("I should see warning message")
def step_impl(context):
    expected_page_menu_text = "Your password is invalid!"
    assert context.browser.get_page_menu().text == expected_page_menu_text


@then("I should see Secure Area")
def step_impl(context):
    expected_page_menu_text = "Secure Area"
    assert context.browser.get_page_menu().text == expected_page_menu_text