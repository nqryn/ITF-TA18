# Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
# - https://www.phptravels.net/
# - http://automationpractice.com/index.php
# - https://formy-project.herokuapp.com/
# - https://the-internet.herokuapp.com/
# - https://www.techlistic.com/p/selenium-practice-form.html
# - jules.app
# Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
# ● Id
# ● Link text
# ● Parțial link text
# ● Name
# ● Tag*
# ● Class name*
# ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
# observație:
# - Probabil nu vei găsi un singur website care să cuprindă toate variantele
# de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
#
# - Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
# Interactionează cu un element la alegere din listă.
# Pentru xpath identifică elemente după criteriile de mai jos:
# ● 3 după atribut valoare
# ● 3 după textul de pe element
# ● 1 după parțial text
# ● 1 cu SAU, folosind pipe |
# ● 1 cu *
# ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
# cu (xpath)[1]
# ● 1 în care să folosești parent::
# ● 1 în care să folosești fratele anterior sau de după (la alegere)
# ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
# ce element vreau să interacționez.
import webbrowser
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

first = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

first.get('https://www.techlistic.com/p/selenium-practice-form.html')

message = first.find_element(value="ez-accept-all")
message.click()

# Elemente Name

first_name = first.find_element(By.NAME, value="firstname")
print(first_name.tag_name)
print(first_name.text)
first_name.send_keys("Vali")

last_name = first.find_element(By.NAME, value="lastname")
print(last_name.tag_name)
print(last_name.text)
last_name.send_keys("MIT")

# date = first.find_element(By.NAME, value="datepicker")
# print(date.tag_name)
# print(date.text)
# date.send_keys("1/10/2022")

# Elemente Link text
primul_link = first.find_element(by=By.LINK_TEXT, value="SELENIUM")
primul_link.click()

primul_link.click()

aldoilea_link = first.find_element(by=By.LINK_TEXT, value="https://chromedriver.chromium.org/downloads")
aldoilea_link.click()

time.sleep(6)

print("Pagina web a fost deschisa")
