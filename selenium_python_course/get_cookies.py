from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    cookies = webdriver.get_cookies()
    pprint(cookies)


with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    cookies = webdriver.get_cookies()
    for cookie in cookies:
        print(cookie['name']) # или cookie['value'] чтобы получить их значение


with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    print(webdriver.get_cookie('_ym_uid')['expiry'])