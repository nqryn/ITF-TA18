import time

from behave import *


@given("I am on the homepage")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/")
    time.sleep(1)


@when("I click the frames menu")
def step_impl(context):
    frames = context.browser.access_frames()
    frames.click()
    time.sleep(2)


@when("I click the forgot password menu")
def step_impl(context):
    forgot_password = context.browser.access_forgot_password()
    forgot_password.click()
    time.sleep(2)


@when("I click the dropdown menu")
def step_impl(context):
    dropdown = context.browser.access_dropdown()
    dropdown.click()
    time.sleep(2)


@then('I am redirected to the "{expected_page}" page')
def step_impl(context, expected_page):
    expected_url = "https://the-internet.herokuapp.com/" + expected_page
    assert context.browser.get_current_url() == expected_url