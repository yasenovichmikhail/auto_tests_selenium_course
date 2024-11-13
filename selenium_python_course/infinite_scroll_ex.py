import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    tags_input = browser.find_elements(By.TAG_NAME, 'input')

    for input in tags_input:
        input.send_keys(Keys.DOWN)
        time.sleep(1)