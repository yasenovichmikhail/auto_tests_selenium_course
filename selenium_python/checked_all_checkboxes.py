import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/4/4.html')
    all_checkboxes = driver.find_elements(By.XPATH, "//input[@class='check']")
    for check_box in all_checkboxes:
        check_box.click()
    send_btn = driver.find_element(By.XPATH, "//input[@class='btn']")
    send_btn.click()
    time.sleep(2)
    secret_number = driver.find_element(By.XPATH, "//p[@id='result']").text
    print(secret_number)
