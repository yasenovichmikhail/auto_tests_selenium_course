import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_forms = browser.find_elements(By.CLASS_NAME, 'form')
    for form in input_forms:
        form.send_keys('Text')
    send_btn = browser.find_element(By.XPATH, "//input[@id='btn']")
    send_btn.click()
    key = browser.find_element(By.XPATH, "//span[@id='result']").text
    print(key)
    time.sleep(5)
