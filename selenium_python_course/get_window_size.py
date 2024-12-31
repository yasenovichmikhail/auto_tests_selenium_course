import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('---window-size=555,555')

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/window_size/1/')
    width_actual = driver.get_window_size().get('width')
    height_actual = driver.get_window_size().get('height')
    width_visible = driver.find_element(By.XPATH, "//span[@id='width']").text.split(" ")
    height_visible = driver.find_element(By.XPATH, "//span[@id='height']").text.split(" ")
    diff_x = width_actual - int(width_visible[-1])
    diff_y = height_actual - int(height_visible[-1])
    driver.set_window_size(554 + diff_x, 555 + diff_y)
    time.sleep(10)

