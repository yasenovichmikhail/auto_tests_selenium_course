from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    pprint(cookies)
    total = 0
    for cookie in cookies:
        name_value = str(cookie['name'])
        secret_number = name_value.split('_')
        number = int(secret_number[2])
        if number % 2 == 0:
            total += int(cookie['value'])
    print(total)
