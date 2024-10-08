import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.5/1/1.html')
    all_fields = driver.find_elements(By.XPATH, "//input[@class='text-field']")
    for field in all_fields:
        field.clear()
    check_button = driver.find_element(By.ID, "checkButton")
    check_button.click()
    alert = driver.switch_to.alert.text
    print(alert)
