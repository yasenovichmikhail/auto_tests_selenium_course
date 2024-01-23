from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, value="input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, value='answer')
    input1.send_keys(y)
    
    option1 = browser.find_element(By.ID, value="robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(30)

    browser.quit()
