from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver.get("https://jules.app/sign-in")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def get_forgot_pass_link(self):
        forgot_pass_selector = (By.XPATH, '//*[@data-test-id="forgot-password-link"]')
        return self.driver.find_element(*forgot_pass_selector)

    def get_current_url(self):
        return self.driver.current_url

    def get_sign_up_link(self):
        sign_up_selector = (By.XPATH, '//*[@data-test-id="sign-up-link"]')
        return self.driver.find_element(*sign_up_selector)

    def enter_username(self, username):
        email_input = self.driver.find_element(by=By.XPATH, value="//input[@type='text']")
        email_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element(by=By.XPATH, value="//input[@type='password']")
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(by=By.XPATH, value="//button[@data-test-id='login-button']")
        login_button.click()

    def get_page_menu(self):
        page_menu_selector = (By.XPATH, '//span[@aria-controls="simple-menu"]')
        return self.driver.find_element(*page_menu_selector)
