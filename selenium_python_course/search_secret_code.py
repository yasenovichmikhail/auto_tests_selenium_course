import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/1/index.html')
    all_btn = driver.find_elements(By.XPATH, "//input[@type='button']")
    for btn in all_btn:
        btn.click()
        driver.switch_to.alert.accept()
        result = driver.find_element(By.XPATH, "//p[@id='result']")
        print(result.text)
        if len(result.text) > 1:
            print(result.text)

