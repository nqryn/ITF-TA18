import time

from selenium import webdriver
from selenium.common import NoSuchFrameException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

"""
Initializam o variabila in care avem un driver ce are abilitatea de a interactiona cu browserul din partea noastra!
"""
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
initial_url = "https://jules.app/"
browser.get(initial_url)

browser.maximize_window()

# Wait implicit: de aici incolo, de fiecare data cand incerc sa gasesc un element,
# Selenium va incerca timp de 5 secunde sa il gaseasca
# La fiecare 500ms (jum de secunda), Selenium va incerca sa gaseasca elementul
# DACA il gaseste, merge mai departe, si NU MAI ASTEAPTA restul timpului
browser.implicitly_wait(5)

"""
Wait explicit: selenium asteapta folosind WebDriverWait dupa o anumita conditie (ExpectedCondition - EC)
"""

wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

# Acum ar trebui sa putem gasi butonul
sign_in_button = browser.find_element(by=By.XPATH, value="//button[@type='submit']")
print(sign_in_button.text)

print(browser.current_url)
assert initial_url != browser.current_url, "Eroare: Nu s-a facut redirect!"
assert browser.current_url == "https://jules.app/sign-in", "Mesaj eroare"

"""
Exemplul 2
"""
# browser.get("https://www.demo.guru99.com/V4/")
# browser.implicitly_wait(10)
# try:
#     browser.switch_to.frame("gdpr-consent-notice")
#     save = browser.find_element(By.ID, "save")
#     save.click()
#     print("A mers")
# except NoSuchFrameException:
#     print("A crapat")
#     pass