from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time


class Browser:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def get_current_url(self):
        return self.driver.current_url

    def access_frames(self): #homepage1
        frames_selector = (By.XPATH, "//a[normalize-space()='Frames']")
        return self.driver.find_element(*frames_selector)

    def access_forgot_password(self): #homepage2
        forgot_password_selector = (By.XPATH, '//*[@id="content"]/ul/li[20]/a')
        return self.driver.find_element(*forgot_password_selector)

    def access_dropdown(self): #homepage2
        dropdown_selector = (By.XPATH, "//a[normalize-space()='Dropdown']")
        return self.driver.find_element(*dropdown_selector)

    def access_form_auth(self): #homepage3
        form_auth_selector = (By.XPATH, "//a[normalize-space()='Form Authentication']")
        return self.driver.find_element(*form_auth_selector)

    def enter_username(self, username):
        email_input = self.driver.find_element(By.ID, 'username')
        email_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login"]/button')
        login_button.click()

    def get_warning_message(self):
        warning_message = (By.XPATH, "//div[@id='flash']")
        return self.driver.find_element(*warning_message)

    def click_logout(self):
        logout_button = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/a')
        logout_button.click()
        raise NotImplementedError("To be implemented")

    def get_page_menu(self):
        page_menu_selector = (By.XPATH, "//h2[normalize-space()='Secure Area']")
        return self.driver.find_element(*page_menu_selector)