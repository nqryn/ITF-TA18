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

# Gaseste-mi elementul cu id-ul "first-name"
# first_name = browser.find_element(value="first-name")
# print(first_name.tag_name)
# print(first_name.text)
# first_name.send_keys("Adela")
#
# time.sleep(1)
#
# last_name = browser.find_element(by=By.ID, value="last-name")
# last_name.send_keys("Kacso-Vidrean")
#
# time.sleep(1)

# components_link = browser.find_element(by=By.ID, value="navbarDropdownMenuLink")
# components_link.click()
# time.sleep(2)


"""
Nu va merge sa dau click direct pe autcomplete, pentru ca nu e vizibil, 
trebuie intai sa deschid dropdown-ul de la Components.
"""
# autocomplete_link = browser.find_element(by=By.LINK_TEXT, value="Autocomplete")
# autocomplete_link.click()

# formy_link = browser.find_element(by=By.LINK_TEXT, value="FORMY")
# formy_link.click()

# links = browser.find_elements(by=By.TAG_NAME, value="a")
# for link in links:
#     print(f"{link.tag_name}: {link.text}")

# time.sleep(3)

"""
find_elements (atentie la S de la final) va returna MEREU o lista de elemente
In general, folosim find_element cand avem ID sau alte modalitati de a gasi elemente unice
Si find_elements cand avem selector de clasa, tagname, etc, care returneaza mai multe elemente.
"""
# navbar_brand_elements = browser.find_elements(by=By.CLASS_NAME, value="navbar-brand")
# for element in navbar_brand_elements:
#     print(f"{element.text}: {element.tag_name}")
#
#
# # Va fi linkul de FORMY (este primul si singurul cu clasa navbar-brand
# navbar_brand_elements[0].click()

"""
Daca folosim un selector care in mod normal ar returna mai multe elemente cu metoda find_element (fara s)
atunci o sa ne returneze de fiecare data doar primul element gasit.
"""
# last_name = browser.find_element(by=By.CLASS_NAME, value="form-control")
# last_name.send_keys("Nume de Familie")

form_controls = browser.find_elements(by=By.CLASS_NAME, value="form-control")
first_name = form_controls[0]
first_name.send_keys("Adela")
last_name = form_controls[1]
last_name.send_keys("Neacsu")
job_title = form_controls[2]
job_title.send_keys("Programator")

data = form_controls[4]
data.send_keys("02/15/2022")

time.sleep(4)

print("Am inchis browserul!")
