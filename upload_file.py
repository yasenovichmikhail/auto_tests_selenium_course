import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.NAME, value='firstname')
    input1.send_keys('michael')

    input2 = browser.find_element(By.NAME, value='lastname')
    input2.send_keys('yasenovich')

    input3 = browser.find_element(By.NAME, value='email')
    input3.send_keys('1@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "1.txt"
    file_path = os.path.join(current_dir, file_name) 
    element = browser.find_element(By.ID, value='file')
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

