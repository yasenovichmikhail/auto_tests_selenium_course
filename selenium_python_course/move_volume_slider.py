import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://parsinger.ru/selenium/5.10/6/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)
    actions = ActionChains(driver=driver)
    volume_slider = driver.find_element(By.XPATH, "//input[@class='volume-slider']")
    slider_width = volume_slider.size['width']
    print(slider_width)
    offset = slider_width / 100
    print(offset)
    current_value = driver.find_element(By.XPATH, "//span[@class='current-value']").text
    target_value = driver.find_element(By.XPATH, "//span[@class='target-value']").text
    print(target_value)
    if int(target_value) < int(current_value):
        actions.click_and_hold(volume_slider).perform()
        for i in range(int(target_value)):
            actions.move_by_offset(offset, 0).perform()
            time.sleep(1)
    elif int(target_value) > int(current_value):
        actions.click_and_hold(volume_slider).send_keys(Keys.ARROW_LEFT).perform()
    time.sleep(5)

