from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    
    button = browser.find_element(By.CSS_SELECTOR, value='.trollface.btn.btn-primary')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, value="input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, value='answer')
    input.send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button1.click()

finally:
    time.sleep(2)
    browser.quit()

# не забываем оставить пустую строку в конце файла