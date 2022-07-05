import pytest
from selenium import webdriver


@pytest.fixture
def get_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Убирает ненужные логи варнинги (ssl, usb)
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')
    # options.add_argument('chrome')  # headless, если без использования UI
    # options.add_argument('--start-maximized')
    # options.add_argument('--window-size=800,600')
    return options


@pytest.fixture()
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')  # Область покрытия: func - при каждом тесте запускается браузер; session - один браузер для всех тестов
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://lyleandscott.ru/'
    if request.cls is not None:  # Являются ли тесты в классе (если да)
        request.cls.driver = driver  # Если класс, то даем драйвер
    driver.get(url)
    yield driver
    #  driver.close() # - закрытие окна
    driver.quit()
