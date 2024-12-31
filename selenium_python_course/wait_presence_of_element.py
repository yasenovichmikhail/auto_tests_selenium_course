import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get(url='https://parsinger.ru/selenium/5.9/2/index.html')
    element = (By.ID, "qQm9y1rk")
    WebDriverWait(driver=driver, timeout=50).until(EC.presence_of_element_located(element)).click()
    result = driver.switch_to.alert.text
    print(result)
