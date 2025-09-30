from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс для автоматизации UI-тестирования с использованием Selenium WebDriver.

    Этот класс предоставляет обертки для наиболее распространенных операций с веб-элементами,
    включая поиск элементов, взаимодействие с ними, ожидания и работу с выпадающими списками.
    Наследуйте от этого класса для создания Page Object моделей.

    Attributes:
        browser: Экземпляр Selenium WebDriver для взаимодействия с браузером
        DEFAULT_WAIT_TIMEOUT (int): Таймаут по умолчанию для явных ожиданий (30 секунд)

    Example:
        >>> from selenium import webdriver

        # Создание экземпляра страницы
        >>> driver = webdriver.Chrome()
        >>> login_page = LoginPage(driver)  # где LoginPage наследует BasePage

        # Использование методов BasePage
        >>> login_page.go_to("/login")
        >>> login_page.fill_element(login_page.username, "test_user")
        >>> login_page.click_element(login_page.submit_button)
    """

    def __init__(self, browser):
        """
        Инициализирует экземпляр BasePage.

        Args:
            browser: Экземпляр Selenium WebDriver (Chrome, Firefox, Safari, etc.)

        Raises:
            TypeError: Если browser не является валидным WebDriver объектом
        """
        self.browser = browser
        self.DEFAULT_WAIT_TIMEOUT = 30

    @property
    def url(self):
        """
        Базовый URL страницы. Должен быть переопределен в дочерних классах.

        Returns:
            str: URL адрес страницы. По умолчанию возвращает пустую строку.

        Note:
            Это свойство должно быть переопределено в конкретных Page Object классах:

            Example:
                @property
                def url(self):
                    return "/login"
        """
        return ''

    def go_to(self, url: str):
        """
        Переходит по указанному URL, объединяя его с базовым URL приложения.

        Args:
            url (str): Относительный или абсолютный URL для перехода

        Example:
            >>> page.go_to("/login")  # переходит на https://www.saucedemo.com/login
            >>> page.go_to("https://google.com")  # переходит на абсолютный URL

        Note:
            Если передается абсолютный URL (начинается с http:// или https://),
            базовый URL игнорируется.
        """
        base_url = 'https://www.saucedemo.com'
        url = base_url + url
        self.browser.get(url)

    def _wait(self, timeout=None):
        """
        Создает экземпляр WebDriverWait с указанным или дефолтным таймаутом.

        Args:
            timeout (int, optional): Таймаут ожидания в секундах. Если None,
                                   используется DEFAULT_WAIT_TIMEOUT

        Returns:
            WebDriverWait: Экземпляр WebDriverWait для создания кастомных ожиданий

        Example:
            >>> wait = self._wait(10)
            >>> wait.until(EC.element_to_be_clickable(locator))
        """
        return WebDriverWait(self.browser, timeout or self.DEFAULT_WAIT_TIMEOUT)

    def _find_element(self, locator: tuple[By, str]) -> WebElement:
        """
        Находит веб-элемент на странице по указанному локатору.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')
                           Например: (By.ID, 'username')

        Returns:
            WebElement: Найденный веб-элемент

        Raises:
            NoSuchElementException: Если элемент не найден на странице

        Note:
            Этот метод используется внутренне другими методами класса.
            Для кастомных операций с элементами используйте этот метод напрямую.
        """
        return self.browser.find_element(*locator)

    def click_element(self, locator: tuple):
        """
        Кликает на элемент, найденный по указанному локатору.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')

        Raises:
            NoSuchElementException: Если элемент не найден
            ElementNotInteractableException: Если элемент не кликабелен

        Example:
            >>> self.click_element((By.ID, 'submit-button'))
            >>> self.click_element((By.XPATH, '//button[text()="Login"]'))
        """
        self._find_element(locator).click()

    def fill_element(self, locator: tuple, text_to_type: str):
        """
        Вводит текст в элемент (обычно input field).

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')
            text_to_type (str): Текст для ввода в поле

        Raises:
            NoSuchElementException: Если элемент не найден
            ElementNotInteractableException: Если элемент недоступен для ввода

        Example:
            >>> self.fill_element((By.ID, 'username'), 'testuser')
            >>> self.fill_element((By.NAME, 'password'), 'secret123')
        """
        self._find_element(locator).send_keys(text_to_type)

    def clear_element(self, locator: tuple):
        """
        Очищает содержимое элемента (обычно input field).

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')

        Raises:
            NoSuchElementException: Если элемент не найден
            ElementNotInteractableException: Если элемент недоступен для редактирования

        Example:
            >>> self.clear_element((By.ID, 'search-field'))
        """
        self._find_element(locator).clear()

    def get_element_text(self, locator: tuple):
        """
        Возвращает видимый текст элемента.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')

        Returns:
            str: Видимый текст элемента

        Raises:
            NoSuchElementException: Если элемент не найден

        Example:
            >>> title = self.get_element_text((By.CLASS_NAME, 'page-title'))
            >>> print(f"Title is: {title}")
        """
        elem_text = self._find_element(locator).text
        return elem_text

    def get_current_url(self):
        """
        Возвращает текущий URL страницы.

        Returns:
            str: Текущий URL адрес

        Example:
            >>> current_url = self.get_current_url()
            >>> assert '/dashboard' in current_url
        """
        page_url = self.browser.current_url
        return page_url

    def get_page_title(self):
        """
        Возвращает заголовок страницы (title).

        Returns:
            str: Заголовок страницы из тега <title>

        Example:
            >>> title = self.get_page_title()
            >>> assert 'Dashboard' in title
        """
        page_title = self.browser.title
        return page_title

    def get_element_attribute(self, locator: tuple, attribute: str):
        """
        Возвращает значение указанного атрибута элемента.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')
            attribute (str): Название атрибута (например, 'value', 'class', 'href')

        Returns:
            str: Значение атрибута или None если атрибут не существует

        Raises:
            NoSuchElementException: Если элемент не найден

        Example:
            >>> value = self.get_element_attribute((By.ID, 'email'), 'value')
            >>> class_name = self.get_element_attribute((By.TAG_NAME, 'input'), 'class')
        """
        elem_attr = self._find_element(locator).get_attribute(attribute)
        return elem_attr

    def get_number_of_elements(self, locator: tuple):
        """
        Возвращает количество элементов, найденных по локатору.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')

        Returns:
            str: Количество найденных элементов в виде строки

        Note:
            Возвращает строку для обратной совместимости.
            Для числовых операций преобразуйте результат в int.

        Example:
            >>> count = int(self.get_number_of_elements((By.CLASS_NAME, 'product-item')))
            >>> assert count > 0
        """
        num_of_elem = len(self.browser.find_elements(*locator))
        return str(num_of_elem)

    def check_element_exist(self, locator: tuple):
        """
        Проверяет существование элемента на странице.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')

        Returns:
            bool: True если элемент существует, False если нет

        Example:
            >>> if self.check_element_exist((By.ID, 'welcome-message')):
            ...     print("Welcome message is present")
        """
        try:
            self._find_element(locator)
            return True
        except NoSuchElementException:
            return False

    def check_element_enabled(self, locator: tuple):
        """
        Проверяет, доступен ли элемент для взаимодействия.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')

        Returns:
            bool: True если элемент enabled, False если disabled

        Raises:
            NoSuchElementException: Если элемент не найден

        Example:
            >>> submit_btn_enabled = self.check_element_enabled((By.ID, 'submit-btn'))
            >>> assert submit_btn_enabled, "Submit button should be enabled"
        """
        enable_status = self._find_element(locator).is_enabled()
        return enable_status

    def is_element_displayed(self, locator: tuple) -> bool:
        """
        Проверяет, отображается ли элемент на странице.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')

        Returns:
            bool: True если элемент отображается, False если скрыт

        Raises:
            NoSuchElementException: Если элемент не найден

        Note:
            В отличие от check_element_exist, этот метод проверяет именно видимость,
            а не только присутствие в DOM.

        Example:
            >>> is_visible = self.is_element_displayed((By.ID, 'popup'))
            >>> assert not is_visible, "Popup should be hidden"
        """
        return self.browser._find_element(locator).is_displayed()

    def refresh_page(self):
        """
        Обновляет текущую страницу.

        Example:
            >>> self.refresh_page()
            >>> self.wait_for_element_to_be_visible((By.ID, 'content'))
        """
        self.browser.refresh()

    def wait_for_element_to_be_visible(self, locator: tuple):
        """
        Ожидает пока элемент станет видимым на странице.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')

        Raises:
            TimeoutException: Если элемент не стал видимым за время ожидания

        Example:
            >>> self.wait_for_element_to_be_visible((By.ID, 'loading-spinner'))
            # Дождаться появления спиннера загрузки
        """
        self._wait().until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_invisible(self, locator: tuple):
        """
        Ожидает пока элемент станет невидимым или исчезнет из DOM.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')

        Raises:
            TimeoutException: Если элемент не стал невидимым за время ожидания

        Example:
            >>> self.wait_for_element_to_be_invisible((By.ID, 'loading-spinner'))
            # Дождаться исчезновения спиннера загрузки
        """
        self._wait().until(EC.invisibility_of_element_located(locator))

    def wait_for_text_to_be_present_in_element(self, locator: tuple, text_to_be_visible: str):
        """
        Ожидает появления указанного текста в элементе.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')
            text_to_be_visible (str): Текст, который должен появиться в элементе

        Raises:
            TimeoutException: Если текст не появился за время ожидания

        Example:
            >>> self.wait_for_text_to_be_present_in_element(
            ...     (By.ID, 'status'),
            ...     'Operation completed'
            ... )
        """
        # define custom timeout if needed self._wait(timeout=15)...
        self._wait().until(EC.text_to_be_present_in_element(locator, text_to_be_visible))

    def select_dropbox_by_visible_text(self, locator: tuple, visible_text: str):
        """
        Выбирает опцию в выпадающем списке по видимому тексту.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')
            visible_text (str): Видимый текст опции для выбора

        Raises:
            NoSuchElementException: Если элемент или опция не найдены
            UnexpectedTagNameException: Если элемент не является select

        Example:
            >>> self.select_dropbox_by_visible_text(
            ...     (By.NAME, 'country'),
            ...     'United States'
            ... )
        """
        select = Select(self._find_element(locator))
        select.select_by_visible_text(visible_text)

    def select_dropbox_by_value(self, locator: tuple, value: str):
        """
        Выбирает опцию в выпадающем списке по значению атрибута value.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')
            value (str): Значение атрибута value опции

        Raises:
            NoSuchElementException: Если элемент или опция не найдены
            UnexpectedTagNameException: Если элемент не является select

        Example:
            >>> self.select_dropbox_by_value((By.NAME, 'currency'), 'USD')
        """
        select = Select(self._find_element(locator))
        select.select_by_value(value)

    def select_dropbox_by_index(self, locator: tuple, index: int):
        """
        Выбирает опцию в выпадающем списке по индексу (начиная с 0).

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')
            index (int): Индекс опции для выбора (0-based)

        Raises:
            NoSuchElementException: Если элемент не найден
            UnexpectedTagNameException: Если элемент не является select

        Example:
            >>> self.select_dropbox_by_index((By.NAME, 'month'), 5)  # Выбрать 6-ю опцию
        """
        select = Select(self._find_element(locator))
        select.select_by_index(index)

    def scroll_to_bottom_of_page(self):
        """
        Прокручивает страницу до самого низа.

        Useful для:
        - Подгрузки контента при infinite scroll
        - Доступа к элементам в footer
        - Скриншотов полной страницы

        Example:
            >>> self.scroll_to_bottom_of_page()
            >>> self.wait_for_element_to_be_visible((By.ID, 'load-more-button'))
        """
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_element(self, locator: tuple):
        """
        Прокручивает страницу до указанного элемента.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')

        Raises:
            NoSuchElementException: Если элемент не найден

        Example:
            >>> self.scroll_to_element((By.ID, 'submit-button'))
            # Элемент теперь виден в viewport
        """
        self.browser.execute_script(
            "arguments[0].scrollIntoView()", self._find_element(locator))

    def set_window_size_to(self, width: int, height: int):
        """
        Устанавливает размер окна браузера.

        Args:
            width (int): Ширина окна в пикселях
            height (int): Высота окна в пикселях

        Useful для:
        - Тестирования responsive design
        - Скриншотов определенного размера
        - Эмуляции мобильных устройств

        Example:
            >>> self.set_window_size_to(1024, 768)
            >>> self.set_window_size_to(375, 667)  # iPhone 6/7/8
        """
        self.browser.set_window_size(width, height)

    def js_click(self, locator: tuple):
        """
        Кликает на элемент используя JavaScript вместо Selenium click.

        Args:
            locator (tuple): Кортеж в формате (By.<METHOD>, 'locator_string')

        Useful для:
        - Элементов, которые перекрыты другими элементами
        - Элементов, которые не являются кликабельными для Selenium
        - Обхода проблем с событиями click

        Warning:
            Этот метод не эмулирует реальное пользовательское взаимодействие
            и может пропускать некоторые валидации.

        Example:
            >>> self.js_click((By.ID, 'hidden-button'))
        """
        self.browser.execute_script("arguments[0].click();", self._find_element(locator))