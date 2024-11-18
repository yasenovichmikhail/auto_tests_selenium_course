import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.7/5/index.html')
    buttons = driver.find_elements(By.XPATH, "//button[@class='timer_button']")
    actions = ActionChains(driver)
    for button in buttons:
        time = float(button.text)
        actions.click_and_hold(button).pause(time).release(button).perform()
    alert = driver.switch_to.alert
    print(alert.text)

