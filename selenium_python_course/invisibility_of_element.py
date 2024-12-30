import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
               'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

with webdriver.Chrome() as driver:
    driver.get(url='https://parsinger.ru/selenium/5.9/3/index.html')
    for ids in ids_to_find:
        element = (By.ID, ids)
        WebDriverWait(driver=driver, timeout=100).until(EC.visibility_of_element_located(element)).click()
    result = WebDriverWait(driver=driver, timeout=1).until(EC.alert_is_present()).text
    print(result)