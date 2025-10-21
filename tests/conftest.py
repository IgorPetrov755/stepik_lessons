import pytest
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service
from path_helper import project_root_dir

@pytest.fixture()
def browser() -> WebDriver:
    """
    Фикстура для инициализации браузера Firefox.

    Returns:
        WebDriver: Экземпляр Firefox WebDriver

    Note:
        После выполнения теста браузер автоматически закрывается
    """
    options = webdriver.FirefoxOptions()

    # Путь к geckodriver (драйверу)
    geckodriver_path = project_root_dir() / "chromedriver" / "geckodriver.exe"

    # Создаем сервис с указанием пути к драйверу
    service = Service(executable_path=str(geckodriver_path))

    # Если нужно указать путь к браузеру Firefox (обычно не требуется)
    # options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

    browser = webdriver.Firefox(service=service, options=options)
    browser.implicitly_wait(10)  # Устанавливаем неявные ожидания
    browser.maximize_window()  # Максимизируем окно браузера
    yield browser
    browser.quit()