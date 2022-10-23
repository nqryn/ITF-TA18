import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
#from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("http://automationpractice.com/index.php")
browser.maximize_window()
time.sleep(2)

# ID
contact_link = browser.find_element(by=By.ID, value="contact-link")
contact_link.click()

email_address = browser.find_element(by=By.ID, value="email")
email_address.send_keys("manolea@yahoo.com")

id_order = browser.find_element(by=By.ID, value="id_order")
id_order.send_keys('1250')
time.sleep(2)

# Link text
sign_in = browser.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in.click()

time.sleep(2)
forgot_pass = browser.find_element(by=By.LINK_TEXT, value="Forgot your password?")
forgot_pass.click()

dresses = browser.find_element(by=By.LINK_TEXT, value="Women")
dresses.click()

time.sleep(2)

# PARTIAL_LINK_TEXT
size_dresses = browser.find_element(by=By.PARTIAL_LINK_TEXT, value="M")
print(size_dresses.is_enabled())

time.sleep(2)
composition_dresses = browser.find_element(by=By.PARTIAL_LINK_TEXT, value="Cotton")
print(composition_dresses.is_enabled())
time.sleep(2)

# Name
email_newsletter = browser.find_element(by=By.NAME, value='email')
email_newsletter.send_keys("andreea@yahoo.com")
time.sleep(2)

submit_newsletter = browser.find_element(by=By.NAME, value='submitNewsletter')
submit_newsletter.click()
time.sleep(2)

search_query = browser.find_element(by=By.NAME, value='search_query')
search_query.send_keys("blouses")
time.sleep(2)

#Class name

banner = browser.find_element(by=By.CLASS_NAME, value='img-responsive')
banner.click()
time.sleep(2)

sign_in = browser.find_element(by=By.CLASS_NAME, value='login')
sign_in.click()
time.sleep(2)

facebook_button = browser.find_element(by=By.CLASS_NAME, value='facebook')
facebook_button.click()
time.sleep(2)

#Tag Name - am incercat mai multe variante- imi da eroare, cred ca nu le identific corect


time.sleep(2)

print('Am terminat!')
