import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as driver:
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/selenium/5.7/4/index.html')
    for i in range(18):
        last_child_container = driver.find_element(By.XPATH, "//div[@class='child_container'][last()]")
        driver.execute_script("return arguments[0].scrollIntoView(true);", last_child_container)
    rows_checkboxes = driver.find_elements(By.XPATH, "//div[@class='child_container']")
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkboxes:
        value = checkbox.get_attribute("value")
        if int(value) % 2 == 0:
            checkbox.click()
    time.sleep(3)
    alert_btn = driver.find_element(By.XPATH, "//button[@class='alert_button']")
    alert_btn.click()
    alert = driver.switch_to.alert
    print(alert.text)
