import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    total = 0
    driver.get('https://parsinger.ru/selenium/3/3.html')

    all_containers = driver.find_elements(By.XPATH, "//div[@class='text']")
    result = []
    for block in all_containers:
        result.append(block.text.split('\n'))
    for i in result:
        for j in range(len(i)):
            if j == 1:
                total += int(i[j])

    print(total)
