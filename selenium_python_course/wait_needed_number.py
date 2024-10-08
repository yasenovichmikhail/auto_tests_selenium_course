import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/methods/1/index.html')

    result = driver.find_element(By.ID, "result").text
    default_text = 'refresh page'

    while True:
        if result == default_text:
            driver.refresh()
            result = driver.find_element(By.ID, "result").text
        else:
            print(result)
            break
