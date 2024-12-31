import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/2/index.html')
    all_btn = driver.find_elements(By.XPATH, "//input[@type='button']")
    input_field = driver.find_element(By.XPATH, "//input[@id='input']")
    check_btn = driver.find_element(By.XPATH, "//input[@value='Проверить']")
    result = driver.find_element(By.XPATH, "//p[@id='result']")
    for btn in all_btn:
        btn.click()
        modal = driver.switch_to.alert
        pin_code = modal.text
        modal.accept()
        input_field.send_keys(pin_code)
        check_btn.click()
        result = driver.find_element(By.XPATH, "//p[@id='result']")
        if result.text != 'Неверный пин-код':
            print(result.text)

