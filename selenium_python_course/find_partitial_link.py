import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/2/2.html')
    needed_link = driver.find_element(By.LINK_TEXT, "16243162441624")
    needed_link.click()
    result = driver.find_element(By.XPATH, "//p[@id='result']").text
    print(result)
