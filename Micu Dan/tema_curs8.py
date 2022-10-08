import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("http://automationpractice.com/index.php")
browser.maximize_window()

# search_query = browser.find_element(value="search_query_top")
# print(search_query.tag_name)
# search_query.send_keys('dress')
# time.sleep(3)

# submit_search = browser.find_element(by=By.NAME,value="submit_search")
# submit_search.click()
# time.sleep(12)


# links = browser.find_elements(by=By.TAG_NAME, value="a")
# for link in links:
#     print(f'{link.tag_name}: {link.text}')
# time.sleep(3)


# best_sellers = browser.find_element(by=By.CLASS_NAME, value="blockbestsellers")
# best_sellers.click()
# time.sleep(3)

# sale_25off = browser.find_element(by=By.CLASS_NAME, value="item-img")
# sale_25off.click()
# time.sleep(3)

# contact_us = browser.find_element(by=By.LINK_TEXT, value="Contact us")
# contact_us.click()
# time.sleep(12)

# cart_button = browser.find_element(by=By.LINK_TEXT, value="Sign in")
# cart_button.click()
# time.sleep(12)

# women_button = browser.find_element(by=By.LINK_TEXT, value="Women")
# women_button.click()
# time.sleep(12)

# blouse = browser.find_element(by=By.PARTIAL_LINK_TEXT,value="Blouse")
# blouse.click()
# time.sleep(12)

# chiffon_dress_links = browser.find_element(by=By.PARTIAL_LINK_TEXT,value="Chiffon Dress")
# chiffon_dress_links.click()
# time.sleep(12)

# contact_button = browser.find_element(by=By.PARTIAL_LINK_TEXT, value= "Contact")
# contact_button.click()
# time.sleep(12)

# sign_in = browser.find_element(by=By.CLASS_NAME, value="login")
# sign_in.click()
# time.sleep(3)

# email_create = browser.find_element(by=By.NAME, value="email_create")
# email_create.send_keys('dress@gmail.com')
# time.sleep(3)

# submit_email = browser.find_element(by=By.NAME, value="SubmitCreate")
# submit_email.click()
# time.sleep(12)