import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/3/index.html')
    all_btn = driver.find_elements(By.XPATH, "//div[@class='main']/span")
    check_btn = driver.find_element(By.XPATH, "//input[@value='Проверить']")
    result = driver.find_element(By.XPATH, "//p[@id='result']")
    pin_codes = []
    for btn in all_btn:
        pin = btn.text
        pin_codes.append(pin)

    for pin_code in pin_codes:
        check_btn.click()
        modal = driver.switch_to.alert
        modal.send_keys(pin_code)
        modal.accept()
        result = driver.find_element(By.XPATH, "//p[@id='result']")
        if result.text != 'Неверный пин-код':
            print(result.text)
