import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.10/2/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)
    width = driver.get_window_size()
    all_boxes = driver.find_elements(By.XPATH, "//div[@class='draganddrop ui-draggable ui-draggable-handle']")
    box_size = 50
    offset = width['width'] - box_size
    actions = ActionChains(driver=driver)
    for box in all_boxes:
        actions.drag_and_drop_by_offset(box, offset, 0).perform()
    res = driver.find_element(By.XPATH, "//p[@id='message']").text
    print(res)
