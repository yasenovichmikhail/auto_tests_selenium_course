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
    actions = ActionChains(driver)
    container1 = []
    container2 = []
    container3 = []
    container4 = []
    container5 = []
    total = 0
    while len(container5) != 100:
        for i in range(1, 6):
            container = driver.find_element(By.XPATH, f"//div[@id='scroll-container_{i}']")
            container_content = container.text.split()
            scroll_container = driver.find_element(By.XPATH, f"//*[@id='scroll-container_{i}']/div")
            if i == 1:
                for digit in container_content:
                    if digit not in container1:
                        container1.append(digit)
                        total += int(digit)
            elif i == 2:
                for digit in container_content:
                    if digit not in container2:
                        container2.append(digit)
                        total += int(digit)
            elif i == 3:
                for digit in container_content:
                    if digit not in container3:
                        container3.append(digit)
                        total += int(digit)
            elif i == 4:
                for digit in container_content:
                    if digit not in container4:
                        container4.append(digit)
                        total += int(digit)
            elif i == 5:
                for digit in container_content:
                    if digit not in container5:
                        container5.append(digit)
                        total += int(digit)
            actions.move_to_element(scroll_container).scroll_by_amount(0, 100).perform()
    print(total)



