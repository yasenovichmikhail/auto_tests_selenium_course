import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/selenium/5.5/3/1.html')
    all_text_area = webdriver.find_elements(By.XPATH, "//textarea")
    total = 0
    for text in all_text_area:
        num = text.text
        if int(num) != 0:
            total += int(num)
    print(total)
        # if checkbox.is_selected():
        #     text = webdriver.find_element(By.XPATH, "//textarea").text
        #     # print(text)
        #     total += int(text)
    time.sleep(5)
