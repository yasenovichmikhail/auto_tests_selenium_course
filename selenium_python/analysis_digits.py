import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/3/3.html')

    all_digits = driver.find_elements(By.XPATH, "//p")
    total = 0
    for digit in all_digits:
        num = digit.text
        total += int(num)

    print(total)
