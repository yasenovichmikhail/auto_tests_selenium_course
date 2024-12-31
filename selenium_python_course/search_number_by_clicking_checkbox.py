from selenium import webdriver
from selenium.webdriver.common.by import By
import re


with webdriver.Chrome() as driver:
    result = []
    driver.get('https://parsinger.ru/scroll/2/index.html')
    all_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for i in range(1, len(all_checkboxes) + 1):
        text_before = driver.find_element(By.XPATH, f"//div[@class='item'][{i}]/div").text
        checkbox = driver.find_element(By.XPATH, f"//*[@id='{i}']")
        checkbox.click()
        text_after = driver.find_element(By.XPATH, f"//div[@class='item'][{i}]/div").text
        if text_after != text_before:
            lst = re.split("[.!?]", text_after)
            result.append(int(lst[-1]))
    total = sum(result)
    print(total)
