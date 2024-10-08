from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/selenium/5.5/2/1.html')
    all_elements = webdriver.find_elements(By.XPATH, "//input[@class='text-field']")
    for element in all_elements:
        if not element.get_attribute('disabled'):
            element.clear()
    check_btn = webdriver.find_element(By.XPATH, "//button[@id='checkButton']")
    check_btn.click()
    code = webdriver.switch_to.alert.text
    print(code)

