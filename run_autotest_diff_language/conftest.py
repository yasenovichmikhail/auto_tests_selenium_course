import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    # В переменную user_language передается параметр из командной строки
    user_language = request.config.getoption('language')
    
    # Инициализируются опции браузера
    options = Options()
    
    # В опции вебдрайвера передаем параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    
    browser.implicitly_wait(5)
    yield browser
    browser.quit()