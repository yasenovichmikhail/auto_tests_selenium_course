import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/scroll/4/index.html')
    all_elements = webdriver.find_elements(By.CLASS_NAME, 'btn')
    total = 0
    for element in all_elements:
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        res = webdriver.find_element(By.XPATH, "//p[@id='result']").text
        total += int(res)
    print(total)
