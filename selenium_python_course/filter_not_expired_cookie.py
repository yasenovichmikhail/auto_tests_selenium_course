from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/5/index.html')
    all_urls = webdriver.find_elements(By.XPATH, "//div[@class='urls']")
    all_expiry_date = []
    all_text = []
    for url in all_urls:
        url.click()
        text = webdriver.find_element(By.XPATH, "//p[@id='result']").text
        all_text.append(text)
        all_cookies = webdriver.get_cookies()
        for expiry_date in all_cookies:
            max_expiry = 0
            all_expiry_date.append(expiry_date['expiry'])
        webdriver.back()
    max_expiry = max(all_expiry_date)
    my_dict = dict(zip(all_expiry_date, all_text))
    for key, value in my_dict.items():
        if key == max_expiry:
            print(value)