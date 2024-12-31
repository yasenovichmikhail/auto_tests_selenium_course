from selenium import webdriver
from selenium.webdriver.common.by import By
import math

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

blanks = ['_blank1', '_blank2', '_blank3', '_blank4', '_blank5', '_blank6']
total = 0
with webdriver.Chrome() as driver:
    driver.get('http://parsinger.ru/blank/2/1.html')
    for i in range(len(sites)):
        driver.execute_script(f'window.open("{sites[i]}", "{blanks[i]}");')
    for i in reversed(range(len(driver.window_handles))):
        if i != 0:
            driver.switch_to.window(driver.window_handles[i])
            checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
            checkbox.click()
            secret_code = driver.find_element(By.XPATH, "//span[@id='result']").text
            num = math.sqrt(int(secret_code))
            total += num
        else:
            continue
    result = round(total, 9)
    print(result)
