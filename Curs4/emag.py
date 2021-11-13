from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(By.ID, 'searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()

product = browser.find_element(By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[4]/div[2]/form/button')
product.click()
time.sleep(20)
