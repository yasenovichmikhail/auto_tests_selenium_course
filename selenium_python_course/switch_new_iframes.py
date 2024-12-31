import time

from selenium import webdriver
from selenium.webdriver.common.by import By

all_frames = ['iframe1', 'iframe2', 'iframe3', 'iframe4', 'iframe5', 'iframe6', 'iframe7', 'iframe8', 'iframe9']

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/5/index.html')
    # all_frame = driver.find_elements(By.XPATH, "//iframe")
    check_input = driver.find_element(By.XPATH, "//input[@id='guessInput']")
    check_btn = driver.find_element(By.XPATH, "//button[@id='checkBtn']")
    for i in all_frames:
        frame = driver.find_element(By.XPATH, f"//iframe[@id='{i}']")
        driver.switch_to.frame(frame)
        btn = driver.find_element(By.XPATH, "//button[@onclick='showNumber()']")
        btn.click()
        code = driver.find_element(By.XPATH, "//p[@id='numberDisplay']").text
        driver.switch_to.default_content()
        check_input.send_keys(code)
        check_btn.click()
        try:
            x = driver.switch_to.alert.text
            if len(x) > 0:
                print(x)
                driver.switch_to.default_content()
        except Exception as e:
            print('There is no code here')
        check_input.clear()
    time.sleep(5)
