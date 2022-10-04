from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchFrameException
import time


browser = webdriver.Chrome()
# browser.get("https://formy-project.herokuapp.com/")
# # browser.maximize_window()
# form = browser.find_element(By.LINK_TEXT, value="Form")
# form.click()
# time.sleep(1)
# first_name = browser.find_element(value="first-name")
# first_name.send_keys("Cosmin")
# second_name = browser.find_element(value="last-name")
# second_name.send_keys("Craciun")
# job_title = browser.find_element(value="job-title")
# job_title.send_keys("software tester")
# level_education = browser.find_element(value="radio-button-1")
# level_education.click()
# sex = browser.find_element(value="checkbox-1")
# sex.click()
# experience = Select(browser.find_element(By.ID, "select-menu"))
# experience.select_by_value("1")
# time.sleep(3)

#_______________________________________________________________________________________________________________________
browser.get("http://automationpractice.com/index.php")
browser.maximize_window()
women = browser.find_element(By.LINK_TEXT, value="Women")
women.click()
time.sleep(2)
dresses = browser.find_element(By.LINK_TEXT, value="Dresses")
dresses.click()
time.sleep(2)
browser.find_element(By.LINK_TEXT, value="Summer Dresses").click()
time.sleep(2)


