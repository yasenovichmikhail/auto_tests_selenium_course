import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.10/8/index.html"

all_stages = [i + 100 for i in range(0, 800, 100)]

with webdriver.Chrome() as driver:
    driver.get(url)
    actions = ActionChains(driver=driver)
    for stage in all_stages:
        box = driver.find_element(By.XPATH, f"//div[@id='piece_{stage}']")
        target = driver.find_element(By.XPATH, f"//div[@id='range_{stage}']")
        actions.drag_and_drop(source=box, target=target).perform()
        res = driver.find_element(By.XPATH, "//p[@id='message']").text
    print(res)
