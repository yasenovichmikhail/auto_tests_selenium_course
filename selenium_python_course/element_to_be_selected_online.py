from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    all_code = []
    driver.get("https://parsinger.ru/selenium/5.9/7/index.html")
    all_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for i in range(1, len(all_checkboxes) + 1):
        check_box_locator = (By.XPATH, f"//div[@id='main_container']/div[{i}]/div/input")
        element = WebDriverWait(driver=driver, timeout=100).until(EC.element_located_to_be_selected(check_box_locator))
        if element:
            check_btn = driver.find_element(By.XPATH, f"//div[@id='main_container']/div[{i}]/button")
            check_btn.click()
    result = driver.find_element(By.XPATH, "//p[@id='result']").text
    print(result)
