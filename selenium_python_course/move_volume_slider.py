import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://parsinger.ru/selenium/5.10/6/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)
    actions = ActionChains(driver=driver)
    sliders = driver.find_elements(By.XPATH, "//div[@class='slider-container']")
    for i in range(1, len(sliders) + 1):
        current_value = int(driver.find_element(By.XPATH, f"//div[@class='slider-container'][{i}]/"
                                                          f"span[@class='current-value']").text)
        target_value = int(driver.find_element(By.XPATH, f"//div[@class='slider-container'][{i}]/"
                                                         "span[@class='target-value']").text)
        slider = driver.find_element(By.XPATH, f"//div[@class='slider-container'][{i}]/"
                                               f"input[@class='volume-slider']")
        if target_value < current_value:
            diff = current_value - target_value
            actions.click(slider).perform()
            for j in range(diff):
                actions.send_keys(Keys.ARROW_LEFT).perform()
        elif target_value > current_value:
            diff = target_value - current_value
            actions.click(slider).perform()
            for j in range(diff):
                actions.send_keys(Keys.ARROW_RIGHT).perform()
    result = driver.find_element(By.XPATH, "//p[@id='message']").text
    print(result)
    time.sleep(3)

