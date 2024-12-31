import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    time.sleep(3)
    browser.execute_script("window.scrollBy(0,10000)")
