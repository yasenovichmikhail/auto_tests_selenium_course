import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.implicitly_wait(5)
    driver.get(url='https://parsinger.ru/selenium/5.9/5/index.html')
    all_btn = driver.find_elements(By.XPATH, "//div[@class='box_button']")
    results = []
    for i in range(1, len(all_btn) + 1):
        element = WebDriverWait(driver=driver, timeout=50).until(EC.visibility_of_element_located((By.XPATH, f"//div[@class='box_button'][{i}]")))
        element.click()
        close_btn = driver.find_element(By.XPATH, "//button[@id='close_ad']")
        close_btn.click()
        len_result = 0
        while len_result == 0:
            tmp_res = driver.find_element(By.XPATH, f"//div[@class='box_button'][{i}]")
            res = tmp_res.text
            if len(res) > 0:
                len_result = int(len(res))
                results.append(res)
            else:
                continue
    print(results)
    finish_results = '-'.join(results)
    print(finish_results)
