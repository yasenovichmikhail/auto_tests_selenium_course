from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.LINK_TEXT, "224592")
    link.click()
    input1 = browser.find_element(By.TAG_NAME, value='input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value='last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value='form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, value="country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла