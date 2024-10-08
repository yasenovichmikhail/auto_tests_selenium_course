from selenium import webdriver
from selenium.webdriver.common.by import By

# Создание объекта ChromeOptions для дополнительных настроек браузера
options_chrome = webdriver.ChromeOptions()

# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
options_chrome.add_argument('--headless')

# Инициализация драйвера Chrome с указанными опциями
# Использование менеджера контекста 'with' для автоматического закрытия браузера после выполнения кода
with webdriver.Chrome(options=options_chrome) as driver:
    url = 'https://stepik.org/course/104774'
    driver.get(url)

    # Ищем элемент по тегу 'a' (ссылку)
    link = driver.find_element(By.TAG_NAME, 'a')

    # Выводим атрибут 'href' найденного элемента (URL ссылки)
    print(link.get_attribute('href'))
