import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/6/6.html')

    key = ((12434107696 * 3) * 2) + 1
    drop_down_list = driver.find_element(
        By.XPATH, "//select[@id='selectId']"
    )
    drop_down_list.click()
    all_item = driver.find_elements(By.TAG_NAME, "option")
    for item in all_item:
        if int(item.text) == key:
            item.click()
    send_btn = driver.find_element(
        By.XPATH, "//input[@id='sendbutton']"
    )
    send_btn.click()
    result = driver.find_element(
        By.XPATH, "//p[@id='result']"
    ).text
    print(result)



