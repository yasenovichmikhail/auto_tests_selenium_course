import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.10/4/index.html"

with webdriver.Chrome() as driver:
    driver.implicitly_wait(5)
    driver.get(url)
    actions = ActionChains(driver=driver)
    red_balls = driver.find_elements(By.XPATH, "//div[contains(@class, 'red_ball')]")
    red_basket = driver.find_element(By.XPATH, "//div[contains(@class, 'basket_color red')]")
    for ball in red_balls:
        actions.drag_and_drop(ball, red_basket).perform()
    blue_balls = driver.find_elements(By.XPATH, "//div[contains(@class, 'blue_ball')]")
    blue_basket = driver.find_element(By.XPATH, "//div[contains(@class, 'basket_color blue')]")
    for ball1 in blue_balls:
        actions.drag_and_drop(ball1, blue_basket).perform()
    green_balls = driver.find_elements(By.XPATH, "//div[contains(@class, 'ball_color green_ball')]")
    green_basket = driver.find_element(By.XPATH, "//div[contains(@class, 'basket_color green')]")
    for ball2 in green_balls:
        actions.drag_and_drop(ball2, green_basket).perform()
    black_balls = driver.find_elements(By.XPATH, "//div[contains(@class, 'ball_color black_ball')]")
    black_basket = driver.find_element(By.XPATH, "//div[contains(@class, 'basket_color black')]")
    for ball3 in black_balls:
        actions.drag_and_drop(ball3, black_basket).perform()
    time.sleep(3)
    result = driver.find_element(By.XPATH, "//p[@class='message']").text
    print(result)
