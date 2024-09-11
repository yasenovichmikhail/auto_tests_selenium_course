import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension(r'C:\Users\User\AppData\Local\Google\Chrome\User Data\Default\
                             Extensions\gkkmpbaijflcgbbdfjgihbgmpkhgpgof\coordinates.crx')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)
    time.sleep(15)
