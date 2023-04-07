from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_login_stepik(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.implicitly_wait(10)
    browser.get(link)
    login_button = browser.find_element(By.ID, value="ember33")
    login_button.click()
    time.sleep(1)

    email = browser.find_element(By.ID, value='id_login_email')
    email.send_keys("yasenovich.mikhail@mail.ru")
    time.sleep(1)

    password = browser.find_element(By.ID, value='id_login_password')
    password.send_keys("mnrvP888")
    time.sleep(1)

    button = browser.find_element(By.XPATH, value='//button[@class="sign-form__btn button_with-loader "]')
    button.click()
    time.sleep(1)

    browser.implicitly_wait(10)
    text_arrea = browser.find_element(By.XPATH, "//textarea[@class='ember-text-area ember-view textarea string-quiz__textarea']")
    text_arrea.send_keys(math.log(int(time.time())))
    time.sleep(1)

    browser.implicitly_wait(10)
    submit_button = WebDriverWait(browser, 15).until(
       EC.element_to_be_clickable(
        (By.XPATH, '//button[@class="submit-submission"]')))
    submit_button.click()
    time.sleep(1)

    feedback = WebDriverWait(browser, 15).until(
       EC.visibility_of_element_located(
        (By.XPATH, "//p[@class='smart-hints__hint']")))
    print(feedback.text)
    feedback_text_act = feedback.text
    print(feedback_text_act)
    feedback_text_exp = 'Correct!'
    assert feedback_text_act == feedback_text_exp, f"expected {feedback_text_exp}, got {feedback_text_act}"
    result = []
    if feedback_text_act != feedback_text_exp:
        result.append(feedback_text_act)
    print(result)
    time.sleep(1)





