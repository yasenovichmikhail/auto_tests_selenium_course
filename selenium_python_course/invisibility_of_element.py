import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get(url='https://parsinger.ru/selenium/5.9/4/index.html')
    close_btn = driver.find_element(By.XPATH, "//span[@class='close']")
    close_btn.click()
    ad = driver.find_element(By.XPATH, "//div[@id='ad']")
    WebDriverWait(driver=driver, timeout=100).until(EC.invisibility_of_element_located(ad))
    secret_btn = driver.find_element(By.XPATH, "//button[@onclick='showSecretNumber()']")
    secret_btn.click()
    result = driver.find_element(By.XPATH, "//p[@id='message']").text
    print(result)
