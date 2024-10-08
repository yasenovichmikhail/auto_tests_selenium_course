import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    total = 0
    driver.get('https://parsinger.ru/selenium/7/7.html')
    all_drop_down_list_value = driver.find_elements(By.XPATH, "//select[@id='opt']//option")
    for item in all_drop_down_list_value:
        total += int(item.text)
    input_field = driver.find_element(By.XPATH, "//input[@id='input_result']")
    input_field.send_keys(total)
    send_btn = driver.find_element(By.XPATH, "//input[@id='sendbutton']")
    send_btn.click()
    result = driver.find_element(By.XPATH, "//p[@id='result']").text
    print(result)
