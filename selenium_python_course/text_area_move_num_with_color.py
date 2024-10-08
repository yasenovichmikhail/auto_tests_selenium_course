import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/selenium/5.5/4/1.html')
    all_boxes = webdriver.find_elements(By.XPATH, "//div[@class='parent']")
    for i in range(1, len(all_boxes) + 1):
        gray_text_area = webdriver.find_element(By.XPATH,
                                                f"//*[@id='container']/div[{i}]/textarea[1]")
        gray_text = gray_text_area.text
        gray_text_area.clear()
        blue_text_area = webdriver.find_element(By.XPATH,
                                                f"//*[@id='container']/div[{i}]/textarea[2]").send_keys(gray_text)
        check_btn = webdriver.find_element(By.XPATH, f"//*[@id='container']/div[{i}]/button")
        check_btn.click()
    check_all_btn = webdriver.find_element(By.XPATH, "//button[@id='checkAll']")
    check_all_btn.click()
    result = webdriver.find_element(By.XPATH, "//p[@id='congrats']").text
    print(result)
