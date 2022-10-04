from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
import time

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    driver.set_window_size(1400, 1080)

    # luam al doilea site din lista data
    driver.get('http://automationpractice.com/index.php')
    time.sleep(1)
    # cautam id-ul 1, contact button (contact-link)
    contact_button = driver.find_element(By.ID, value='contact-link')
    contact_button.click()
    time.sleep(5)
    # dupa intrarea pe pagina de contact, vom alege subiectele care au id
    driver.find_element(By.ID, value='email').send_keys('madalinadiana728@yahoo.com')
    time.sleep(3)
    driver.find_element(By.ID, value='id_order').send_keys('2768')
    time.sleep(3)
    driver.find_element(By.ID, value='message').send_keys('Mesajul de testare')
    time.sleep(3)
    # selectam din dropdown elementul dorit
    subject_element = Select(driver.find_element(By.ID, value='id_contact'))
    subject_element.select_by_value('2')        # Customer service
    time.sleep(3)
    # trimitem formularul -am folosit 5 selectoare de tip id
    driver.find_element(By.ID, value='submitMessage').click()
    # intram in pagina de women folosind xpath
    driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a').click()
    time.sleep(1)
    # # scriem in bara de search rochie rosie folosind name
    n = driver.find_element(By.NAME, 'search_query')
    n.send_keys('long dress')
    time.sleep(1)
    ##folosim name pentru a accesa butonul de cautare
    driver.find_element(By.NAME, 'submit_search').click()
    time.sleep(2)
    # folosim class name pentru a accesa rochia
    driver.find_element(By.CLASS_NAME, 'product_img_link').click()
    time.sleep(3)
    driver.execute_script('window.scrollTo(0, 600)')
    time.sleep(3)
    # selectam marimea potrivita folosind name - am folosit astfel 4 selectori de tip name
    marime = Select(driver.find_element(By.NAME, value='group_1'))
    marime.select_by_value('2')
    time.sleep(5)
    driver.find_element(By.NAME, 'Submit').click()
    time.sleep(3)
    l = driver.find_element(By.XPATH, "//a[@title='Proceed to checkout']")
    l.click()
    time.sleep(3)
    # stergem rochia adaugata in cos folosind class_name 3
    driver.find_element(By.CLASS_NAME, 'cart_quantity_delete').click()
    time.sleep(2)
    # selectam butonul de intoarcere la pagina principala folosind css selector
    driver.find_element(By.CSS_SELECTOR, '#columns > div.breadcrumb.clearfix > a').click()
    time.sleep(3)
    driver.quit()
    print("Done")

