import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    # driver.get("http://suninjuly.github.io/registration1.html")
    driver.get("http://suninjuly.github.io/registration2.html")

    driver.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
    driver.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Ivanov")
    driver.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("iviv@mail.com")

    driver.find_element(By.CSS_SELECTOR, ".btn").click()

    time.sleep(1)

    assert driver.find_element(By.CSS_SELECTOR, "h1").text == "Congratulations! You have successfully registered!"

finally:

    driver.quit()
