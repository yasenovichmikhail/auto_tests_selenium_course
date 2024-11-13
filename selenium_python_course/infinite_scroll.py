import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

with webdriver.Chrome() as driver:
    lst = []
    total = 0
    driver.get('https://parsinger.ru/infiniti_scroll_1/')
    scroll_container = driver.find_element(By.XPATH, "//div[@id='scroll-container']")
    actions = ActionChains(driver)
    while True:
        actions.move_to_element(scroll_container).perform()
        container = scroll_container.text.split()
        for digit in container:
            if digit not in lst:
                lst.append(digit)
                total += int(digit)
        actions.send_keys_to_element(scroll_container, Keys.DOWN).perform()
        length_lst = len(lst)
        if length_lst == 100:
            break
    print(total)
