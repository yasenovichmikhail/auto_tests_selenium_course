import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/selenium/5.5/5/1.html')
    all_boxes = webdriver.find_elements(By.XPATH, "//*[@id='main-container']/div")
    for i in range(1, len(all_boxes) + 1):
        color = webdriver.find_element(By.XPATH, f"//*[@id='main-container']/div[{i}]/span").text
        webdriver.find_element(By.XPATH, f"//*[@id='main-container']/div[{i}]/select").click()
        all_colors_drop_down_list = webdriver.find_elements(By.XPATH, f"//*[@id='main-container']/div[{i}]/select/option")
        for col in all_colors_drop_down_list:
            x = col.text
            if x == color:
                col.click()
        set_of_colors = webdriver.find_elements(By.XPATH, f"//*[@id='main-container']/div[{i}]/div/button")
        for color_in_set in set_of_colors:
            hex_color = color_in_set.get_attribute('data-hex')
            if hex_color == color:
                color_in_set.click()
        checkbox = webdriver.find_element(By.XPATH, f"//*[@id='main-container']/div[{i}]/input[1]")
        checkbox.click()
        input_field = webdriver.find_element(By.XPATH, f"//*[@id='main-container']/div[{i}]/input[2]")
        input_field.send_keys(color)
        check_btn = webdriver.find_element(By.XPATH, f"//*[@id='main-container']/div[{i}]/button")
        check_btn.click()
        check_all_btn = webdriver.find_element(By.XPATH, "//body/button")
        check_all_btn.click()
    result = webdriver.switch_to.alert.text
    print(result)





