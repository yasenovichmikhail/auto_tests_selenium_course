import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    height = browser.execute_script("return document.body.scrollHeight")
    width = browser.execute_script("return document.body.scrollWidth")
    time.sleep(2)
    visible_height = browser.execute_script("return window.innerHeight")
    visible_width = browser.execute_script("return window.innerWidth")

    print(height)
    print(width)
    print(visible_height)
    print(visible_width)

