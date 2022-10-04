import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

"""
Initializam o variabila in care avem un driver ce are abilitatea de a interactiona cu browserul din partea noastra!
"""
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("https://formy-project.herokuapp.com/form")
time.sleep(1)

browser.maximize_window()

first_name_by_id = browser.find_element(by=By.ID, value="first-name")
# Diezul (#) reprezinta ID in CSS
first_name_by_css_id = browser.find_element(by=By.CSS_SELECTOR, value="#first-name")
assert first_name_by_css_id == first_name_by_id

# Punctul (.) reprezinta clasa in CSS
first_name_by_class = browser.find_element(by=By.CLASS_NAME, value="form-control")
first_name_by_css_class = browser.find_element(by=By.CSS_SELECTOR, value=".form-control")
assert first_name_by_css_class == first_name_by_class

first_name_by_placeholder = browser.find_element(by=By.CSS_SELECTOR,
                                                 value="input[placeholder='Enter first name']")
# first_name_by_placeholder.send_keys("Gasit dupa placeholder")
#
# time.sleep(2)

h1_title = browser.find_element(by=By.CSS_SELECTOR, value="body div h1")
print(h1_title.text)

last_name_container = browser.find_element(by=By.CSS_SELECTOR,
                                           value="body > div > form > div > div:nth-child(3)")

last_name_container2 = browser.find_element(by=By.CSS_SELECTOR,
                                            value=".form-group div:nth-child(3)")
assert last_name_container2 == last_name_container

last_name_input = last_name_container.find_element(by=By.TAG_NAME, value="input")
last_name_input.send_keys("Luat din parinte.")

time.sleep(2)
