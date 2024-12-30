import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/draganddrop/2/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)
    actions = ActionChains(driver=driver)
    red_box = driver.find_element(By.XPATH, "//div[@id='draggable']")
    target1 = driver.find_element(By.XPATH, "//div[@id='box1']")
    target2 = driver.find_element(By.XPATH, "//div[@id='box2']")
    target3 = driver.find_element(By.XPATH, "//div[@id='box3']")
    target4 = driver.find_element(By.XPATH, "//div[@id='box4']")
    actions.drag_and_drop(red_box, target1).perform()
    actions.drag_and_drop(red_box, target2).perform()
    actions.drag_and_drop(red_box, target3).perform()
    actions.drag_and_drop(red_box, target4).perform()
    res = driver.find_element(By.XPATH, "//div[@id='message']").text
    print(res)
