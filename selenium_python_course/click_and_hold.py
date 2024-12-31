from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.implicitly_wait(10)
    driver.get('https://parsinger.ru/draganddrop/3/index.html')

    block = driver.find_element(By.XPATH, "//div[@id='block1']")

    actions = ActionChains(driver)

    actions.click_and_hold(block).perform()

    for _ in range(5):
        actions.move_by_offset(50, 0).perform()

    actions.release().perform()
    res = driver.find_element(By.XPATH, "//p[@id='message']").text
    print(res)
    time.sleep(3)

