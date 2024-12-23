import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/blank/3/index.html')
    all_btns = driver.find_elements(By.XPATH, "//input[@type='button']")
    total = 0
    nums = []
    for btn in all_btns:
        btn.click()
    for i in range(len(driver.window_handles)):
        driver.switch_to.window(driver.window_handles[i])
        title = driver.execute_script("return document.title;")
        nums.append(title)
    for code in nums:
        if code != 'alert':
            total += int(code)
        else:
            continue
    print(total)
