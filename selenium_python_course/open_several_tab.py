from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    #browser.get("https://stepik.org/course/104774/promo") # Вместо вкладки data; будет вкладка в которой будет загружен степик
    driver.execute_script('window.open("http://parsinger.ru/blank/2/1.html", "_blank1");')
    driver.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank2");')
    driver.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank3");')
    driver.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank4");')

    for x in range(len(driver.window_handles)):  #reversed(range(len(browser.window_handles))) Для итерирования по порядку
        driver.switch_to.window(driver.window_handles[x])
        for y in driver.find_elements(By.CLASS_NAME, 'check'):
            y.click()
