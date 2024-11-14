from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://parsinger.ru/selenium/5.7/2/index.html")

draggable = driver.find_element(By.ID, "draggable")

actions = ActionChains(driver)

actions.drag_and_drop_by_offset(draggable, -100, 0).perform()

actions.drag_and_drop_by_offset(draggable, 0, 100).perform()

actions.drag_and_drop_by_offset(draggable, 100, 0).perform()

actions.drag_and_drop_by_offset(draggable, 0, -100).perform()
actions.

driver.quit()
