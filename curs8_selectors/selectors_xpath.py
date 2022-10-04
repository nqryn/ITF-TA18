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

# * = toate elementele
# [@atribut=valoare]
# Deci cautam toate elementele cu id 'first-name'
first_name = browser.find_element(by=By.XPATH, value="//*[@id='first-name']")
# XPath normal (luat din browser cu click dreapta - Copy XPath) => vom primi cel mai rapid XPath de obicei
print('//*[@id="first-name"]')
# Full Xpath (click dreapta - Copy full XPath) => vom primi un XPath care pleaca de la radacina arborelui HTML (adica html)
print('/html/body/div/form/div/div[1]/input')

# # Putem cauta in browser dupa XPath (in partea din dreapta - Developer Tools)
# last_name = browser.find_element(by=By.XPATH, value="(//input[@class='form-control'])[1]")
# last_name.send_keys("Hello, world!")
# time.sleep(2)
#
# for i in range(1, 4):
#     element = browser.find_element(by=By.XPATH, value=f"(//input[@class='form-control'])[{i}]")
#     element.send_keys(f"{i}" * 25)
#
# time.sleep(3)

h1_title = browser.find_element(by=By.XPATH, value='//*[@contains(text(), "Web")]')