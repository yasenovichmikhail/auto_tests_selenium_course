from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.7/1/index.html')
    piece_uranium_element = driver.find_elements(By.XPATH, "//div[@class='button-container']")
    for element in piece_uranium_element:
        driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
    alert_window = driver.switch_to.alert
    print(alert_window.text)
