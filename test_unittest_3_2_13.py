from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class test_class_name(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

    # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        time.sleep(2)
        input2 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys("Hello Hello Hello")
        time.sleep(2)
        input3 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("qa4fexbox.org")
        time.sleep(2)

    # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        expected_result = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_result, f"Should be{expected_result}, got{welcome_text}")
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

    # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        time.sleep(2)
        input2 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys("Hello Hello Hello")
        time.sleep(2)
        input3 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("qa4fexbox.org")
        time.sleep(2)

    # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        expected_result = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_result, f"Should be{expected_result}, got{welcome_text}")
        
if __name__ == "__main__":
    unittest.main()