import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get(url='https://parsinger.ru/expectations/4/index.html')
    click_btn_element = (By.XPATH, "//button[@id='btn']")
    WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable(click_btn_element)).click()
    title = WebDriverWait(driver=driver, timeout=50).until(EC.title_contains('JK8HQ'))
    if title:
        result = driver.title
        print(result)
