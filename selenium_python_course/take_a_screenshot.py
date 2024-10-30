import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://myfin.by')
    time.sleep(3)
    driver.get_screenshot_as_file(r'C:\Users\User\Desktop\test_picture.png')
