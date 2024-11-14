import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_2/')
#     div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
#     while True:
#         ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_3/')
    container_1 = driver.find_element(By.XPATH, "//*[@id='scroll-container_1']/div")
    actions = ActionChains(driver)
    for i in range(5):
        actions.move_to_element(container_1).scroll_by_amount(0, 100).perform()
