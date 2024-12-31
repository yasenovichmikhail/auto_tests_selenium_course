import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.10/3/index.html"

colors = {'red': 'rgb(255, 0, 0)', 'green': 'rgb(0, 128, 0)', 'yellow': 'rgb(255, 255, 0)', 'cyan': 'rgb(0, 255, 255)',
          'brown': 'rgb(128, 0, 0)', 'blue': 'rgb(0, 0, 255)', 'purple': 'rgb(128, 0, 128)'}

with webdriver.Chrome() as driver:
    driver.get(url)
    big_squares = driver.find_elements(By.XPATH, "//div[@class='draganddrop_end']")
    small_squares = driver.find_elements(By.XPATH, "//div[@class='draganddrop ui-draggable ui-draggable-handle']")
    tmp_list = []
    actions = ActionChains(driver=driver)
    for big_square in big_squares:
        attribute = big_square.get_attribute('style')
        tmp_color = attribute.split(';')[0]
        color = tmp_color.split(': ')[1]
        print(color)
        for small_square in small_squares:
            attr = small_square.get_attribute('style')
            tmp_color_small = attr.split(';')[0]
            color_small = tmp_color_small.split(': ')[1]
            print(color_small)
            for key, value in colors.items():
                if key == color and value == color_small:
                    actions.drag_and_drop(small_square, big_square).perform()
                elif color == color_small:
                    actions.drag_and_drop(small_square, big_square).perform()
                else:
                    print('no')
    res = driver.find_element(By.XPATH, "//p[@id='message']").text
    print(res)