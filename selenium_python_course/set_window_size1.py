import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:

    window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

    result_code = []
    driver.get('https://parsinger.ru/window_size/2/index.html')
    width_actual = driver.get_window_size().get('width')
    height_actual = driver.get_window_size().get('height')
    width_visible = driver.find_element(By.XPATH, "//span[@id='width']").text.split(" ")
    height_visible = driver.find_element(By.XPATH, "//span[@id='height']").text.split(" ")
    diff_x = (width_actual - int(width_visible[-1])) - 1
    diff_y = height_actual - int(height_visible[-1])

    for i in window_size_x:
        for j in window_size_y:
            driver.set_window_size(i + diff_x, j + diff_y)
            result = driver.find_element(By.XPATH, "//span[@id='result']")
            result = result.text
            if len(result) > 1:
                window_size = driver.get_window_size()
                print(window_size)
                break
