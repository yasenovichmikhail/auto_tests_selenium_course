from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
import math

link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


# @pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_login_stepik(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    login_button = browser.find_element(By.ID, value="ember33")
    login_button.click()

    email = browser.find_element(By.ID, value='id_login_email')
    email.send_keys("yasenovich.mikhail@mail.ru")
    password = browser.find_element(By.ID, value='id_login_password')
    password.send_keys("mnrvP888")

    button = browser.find_element(By.XPATH, value='//button[@class="sign-form__btn button_with-loader "]')
    button.click()

    # answer = math.log(int(time.time()))

    text_arrea = WebDriverWait(browser, 15).until(
       EC.element_to_be_clickable(
            (By.ID, "ember93")))
    text_arrea.send_keys(math.log(int(time.time())))

    submit_button = browser.find_element(By.XPATH, value='//button[@class="submit-submission"]')
    submit_button.click()


    time.sleep(10)





