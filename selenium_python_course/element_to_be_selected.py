from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/5.9/6/index.html")
    checkbox = (By.XPATH, "//input[@id='myCheckbox']")
    element = WebDriverWait(driver=driver, timeout=10).until(EC.element_located_to_be_selected(checkbox))
    if element:
        click_btn = driver.find_element(By.XPATH, "//button[@onclick='checkCheckbox()']")
        click_btn.click()
        result = driver.find_element(By.XPATH, "//p[@id='result']").text
        print(result)

