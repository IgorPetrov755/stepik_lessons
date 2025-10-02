import pytest
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver


@pytest.fixture
def browser() -> WebDriver:
    """
    Фикстура для инициализации браузера Firefox.

    Returns:
        WebDriver: Экземпляр Firefox WebDriver

    Note:
        После выполнения теста браузер автоматически закрывается
    """
    options = webdriver.FirefoxOptions()
    options.binary_location = "J:\projects\stepik_lessons\chromedriver\geckodriver.exe"
    browser = webdriver.Firefox(options=options)
    browser.implicitly_wait(10)  # Устанавливаем неявные ожидания
    browser.maximize_window()  # Максимизируем окно браузера
    yield browser
    browser.quit()
