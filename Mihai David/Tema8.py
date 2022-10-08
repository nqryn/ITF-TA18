'''Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchFrameException

browser = webdriver.Chrome()

class enter_website:
    def enter(self):
        browser.get("https://www.techlistic.com/p/selenium-practice-form.html")
        time.sleep(3)
        #browser.switch_to.frame("google esf");
        div = browser.find_element(By.ID, "ez-cookie-dialog-wrapper")
        accept = div.find_element(By.ID, "ez-accept-all")
        accept.click()
        time.sleep(3)
        print("enter website")
website = enter_website()
website.enter()

#browser.get("http://automationpractice.com/index.php")
#browser.maximize_window()
#time.sleep(1)

'''banner = browser.find_element(By.CLASS_NAME, "img-responsive")
banner.click()
time.sleep(1)

logo = browser.find_element(By.CSS_SELECTOR, "#header_logo > a > img")
logo.click()
time.sleep(1)'''

'''search = browser.find_element(By.XPATH, "//*[@id='search_query_top']").send_keys("dresses")
time.sleep(1)

submit_search = browser.find_element(By.NAME, "submit_search")
submit_search.click()'''

'''browser.get("http://automationpractice.com/index.php")

search_bar = browser.find_element(By.XPATH, "//*[@id='search_query_top']").send_keys("dresses")
time.sleep(1)

submit_search = browser.find_element(By.NAME, "submit_search")
submit_search.click()

dress = browser.find_element(By.XPATH, "//*[@id='center_column']/ul/li[1]/div/div[1]/div/a[1]/img")
dress.click()
time.sleep(1)

try:
    browser.switch_to.frame("fancybox-frame1664712218770");
except NoSuchFrameException:
    pass

size = Select(browser.find_element(By.ID, "group_1" ))
size.select_by_visible_text("M")
time.sleep(2)

#colour = Select(browser.find_element(By.XPATH, "//label[@class='attribute_label']" ))
#colour = Select(browser.find_element(By.CLASS_NAME, "attribute label"))
#for label in size:
#    size.select_by_value("BLUE")

colour = browser.find_element(By.NAME, "Blue")
colour.click()
time.sleep(2)

add_to_cart = browser.find_element(By.XPATH, "//span[normalize-space()='Add to cart']")
add_to_cart.click()
time.sleep(1)

proceed_to_checkout = browser.find_element(By.XPATH, "//a[@title='Proceed to checkout']")
proceed_to_checkout.click()
time.sleep (1)

checkout = browser.find_element(By.XPATH, "//a[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]")
checkout.click()
time.sleep(1)
browser.maximize_window()

email = browser.find_element(By.CSS_SELECTOR, "#email_create").send_keys("userkyrosa@yahoo.com")
create = browser.find_element(By.CSS_SELECTOR, "button[id='SubmitCreate'] span").click()
time.sleep(10)
'''
