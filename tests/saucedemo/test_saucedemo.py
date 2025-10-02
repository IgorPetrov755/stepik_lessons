import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.saucedemo_cart import SauceDemoCart
from pages.saucedemo_landing import SauceDemoLanding
from pages.saucedemo_products import SauceDemoProducts


class TestSaucedemo:
    @pytest.fixture
    def firefox_browser(self):
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

    def test_saucedemo(self, firefox_browser):
        browser = firefox_browser
        """Test Case 1: test"""
        # 1. Перейти на сайт Saucedemo.
        page = SauceDemoLanding(browser)
        page.open()

        # 2. Проверить, что заголовок страницы соответствует "Swag Labs".
        logo_text = page.get_element_text(page.logo)
        assert logo_text == "Swag Labs", 'заголовок страницы не соответствует "Swag Labs"'

        # 3. Проверить, текст кнопки логина.
        login_button_text = page.get_element_attribute(page.login_button, 'value')
        assert login_button_text == "Login", "текст кнопки Логин некорректен"

        # 4. Выполнить вход под учетной записью standard_user с паролем secret_sauce.
        page.login(username='standard_user', password='secret_sauce')

        products_page = SauceDemoProducts(browser)
        assert products_page.url in products_page.get_current_url(), 'Не выполнен редирект после логина'
        assert products_page.check_element_exist(products_page.shopping_cart_link), 'Не найдена корзина'

        # 5. Проверить фильтр по умолчанию
        filter_text = products_page.get_current_filter()
        assert filter_text == "Name (A to Z)", 'Фильтр по умолчанию не "Name (A to Z)"'

        # 6. Добавить первый товар в корзину
        first_product = products_page.get_first_product()
        first_product_name = products_page.get_product_name(first_product)

        # Проверяем текст кнопки перед кликом
        add_button = first_product.find_element(*products_page.add_button)
        assert add_button.text == "Add to cart", 'Текст кнопки не соответствует ожидаемому'

        products_page.add_product_to_cart(first_product)

        # 7. Проверить счетчик корзины
        cart_count = products_page.get_cart_items_count()
        assert cart_count == 1, f'Неверный счетчик корзины. Ожидалось: 1, получено: {cart_count}'

        # 8. Добавить последний товар в корзину
        last_product = products_page.get_last_product()
        last_product_name = products_page.get_product_name(last_product)
        products_page.add_product_to_cart(last_product)

        # 9. Проверить обновленный счетчик корзины
        cart_count = products_page.get_cart_items_count()
        assert cart_count == 2, f'Неверный счетчик корзины. Ожидалось: 2, получено: {cart_count}'

        # 10. Удалить первый товар из корзины
        products_page.remove_product_from_cart(first_product)

        # 11. Проверить счетчик после удаления
        cart_count = products_page.get_cart_items_count()
        assert cart_count == 1, f'Неверный счетчик корзины после удаления. Ожидалось: 1, получено: {cart_count}'

        # 12. Перейти в корзину
        products_page.go_to_cart()

        cart_page = SauceDemoCart(browser)
        cart_page.wait_for_page_load()
        assert cart_page.url in cart_page.get_current_url(), 'Не выполнен переход в корзину'

        # 13. Проверить товары в корзине
        cart_items_count = cart_page.get_cart_items_count()
        assert cart_items_count == 1, f'В корзине не один элемент. Найдено: {cart_items_count}'

        cart_item_names = cart_page.get_cart_item_names()
        assert last_product_name in cart_item_names, f'Товар "{last_product_name}" отсутствует в корзине'
        assert first_product_name not in cart_item_names, f'Удаленный товар "{first_product_name}" присутствует в корзине'

        # 14. Вернуться к каталогу товаров
        cart_page.continue_shopping()
        products_page.wait_for_page_load()
        assert products_page.url in products_page.get_current_url(), 'Не выполнен переход к списку товаров'

        # 15. Изменить фильтр сортировки
        products_page.select_filter("lohi")  # Price (low to high)

        # 16. Проверить корректность сортировки
        current_filter = products_page.get_current_filter()
        assert "Price (low to high)" in current_filter, 'Фильтр не установлен на Price (low to high)'

        # Проверяем сортировку цен
        products = products_page.get_all_products()
        if len(products) >= 2:
            first_price = products_page.get_product_price(products[0])
            last_price = products_page.get_product_price(products[-1])
            assert first_price <= last_price, \
                f'Сортировка неверна. Первая цена: {first_price}, последняя: {last_price}'
