import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get(url='https://parsinger.ru/expectations/3/index.html')
    btn_locator = driver.find_element(By.XPATH, "//button[@id='btn']")
    click_btn = WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable(btn_locator)).click()
    title = WebDriverWait(driver=driver, timeout=50).until(EC.title_is('345FDG3245SFD'))
    if title:
        result = driver.find_element(By.XPATH, "//p[@id='result']")
        print(result.text)
