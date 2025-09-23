import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class TestCase1:
    def test_saucedemo(self):
        """Test Case 1: test"""
        # 1. Перейти на сайт Saucedemo.
        try:
            link = "https://www.saucedemo.com/"

            options = Options()
            options.add_argument('start-maximized')
            options.add_argument('--avoid-stats')
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-notifications")
            options.add_argument("--no-sandbox")
            options.add_experimental_option("excludeSwitches", ["disable-prompt-on-repost", "enable-automation"])
            options.add_experimental_option("prefs", {
                "profile.default_content_setting_values.notifications": 2,  # disable all notice
                "profile.default_content_setting_values.media_stream_mic": 2,  # disable microphone
                "profile.default_content_setting_values.media_stream_camera": 2,  # disable camera
                "profile.default_content_setting_values.geolocation": 2,  # disable geolocations
                "credentials_enable_service": False,  # Отключаем сервис автозаполнения
                "profile.password_manager_enabled": False,  # Отключаем менеджер паролей
                "safebrowsing.enabled": False,
            })
            browser = webdriver.Chrome(service=None, options=options)  # Открыть браузер

            browser.get(link)  # перейти на страницу link

        # 2. Проверить, что заголовок страницы соответствует "Swag Labs".
            logo = browser.find_element(By.CSS_SELECTOR, '.login_logo')
            assert logo.text == "Swag Labs", 'заголовок страницы не соответствует "Swag Labs"'

        # 3. Проверить, текст кнопки логина.
            login_button = browser.find_element(By.CSS_SELECTOR, '*[data-test="login-button"]')
            assert login_button.get_attribute(name='value') == "Login", "текст кнопки Логин некорректен"

        # 4. Выполнить вход под учетной записью standard_user с паролем secret_sauce.
            username_input = browser.find_element(By.CSS_SELECTOR, 'input[data-test="username"]')
            username_input.send_keys("standard_user")
            password_input = browser.find_element(By.CSS_SELECTOR, 'input[data-test="password"]')
            password_input.send_keys("secret_sauce")
            login_button.click()

            # Переключение на активное всплывающее окно
            time.sleep(5)

            assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'Не выполнен редирект после логина'
            shopping_cart_link = browser.find_elements(By.CSS_SELECTOR, '*[data-test="shopping-cart-link"]')
            assert len(shopping_cart_link) == 1, 'Не найдена корзина'

        # 5. Проверить, что выбранный фильтр в выпадающем списке по умолчанию имеет значение "Name (A to Z)".
            filter_active_value = browser.find_element(By.CSS_SELECTOR, '*[data-test="active-option"]')
            assert filter_active_value.text == "Name (A to Z)", \
                'фильтр в выпадающем списке по умолчанию не имеет значение "Name (A to Z)"'

        # 6. Добавить первый товар из списка в корзину, нажав на кнопку "Add to cart".
            first_card = browser.find_element(By.CSS_SELECTOR, 'div.inventory_item:first-child')
            cart_button = first_card.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
            assert cart_button.text == "Add to cart", 'Текст кнопки не соответствует ожидаемому'
            cart_button.click()

        # 7. Проверить, что иконка корзины в правом верхнем углу отображает счетчик с цифрой 1.
            cart_badge = browser.find_elements(By.CSS_SELECTOR, 'span[data-test="shopping-cart-badge"]')
            assert len(cart_badge) == 1, 'Товар не добавлен в корзину'
            assert cart_badge[0].text == "1", 'Неверный текст счетчика корзины'

        # 8. Добавить последний товар из списка в корзину, нажав на кнопку "Add to cart".
            last_card = browser.find_element(By.CSS_SELECTOR, 'div.inventory_item:last-child')
            last_card_name = last_card.find_element(By.CSS_SELECTOR, '*[data-test="inventory-item-name"]').text
            cart_button = last_card.find_element(By.CSS_SELECTOR, 'button.btn_inventory')
            cart_button.click()

        # 9. Проверить, что значение счетчика на иконке корзины увеличилось и теперь отображает цифру 2.
            cart_badge = browser.find_elements(By.CSS_SELECTOR, 'span[data-test="shopping-cart-badge"]')
            assert len(cart_badge) == 1, 'Товар не добавлен в корзину'
            assert cart_badge[0].text == "2", 'Неверный текст счетчика корзины'

        # 10. Удалить первый товар из корзины, нажав на кнопку "Remove" у первого товара в списке.
            first_card = browser.find_element(By.CSS_SELECTOR, 'div.inventory_item:first-child')
            cart_button = first_card.find_element(By.CSS_SELECTOR, 'button.btn_inventory')
            assert cart_button.text == "Remove", 'Текст кнопки не соответствует ожидаемому'
            cart_button.click()

        # 11. Проверить, что значение счетчика на иконке корзины изменилось и теперь отображает цифру 1.
            cart_badge = browser.find_elements(By.CSS_SELECTOR, 'span[data-test="shopping-cart-badge"]')
            assert len(cart_badge) == 1, 'Товар не добавлен в корзину'
            assert cart_badge[0].text == "1", 'Неверный текст счетчика корзины'

        # 12. Кликнуть на иконку корзины 🛒 в правом верхнем углу для перехода в корзину.
            cart_link = browser.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')
            cart_link.click()
            assert browser.current_url == 'https://www.saucedemo.com/cart.html', 'Не выполнен переход в карточку корзины'

        # 13. Проверить, что добавленный товар (последний из списка) отображается на странице корзины.
            card_list = browser.find_elements(By.CSS_SELECTOR, '.cart_item')
            assert len(card_list) == 1, 'В корзине не один элемент'
            card_item_name = card_list[0].find_element(By.CSS_SELECTOR, '*[data-test="inventory-item-name"]').text
            assert card_item_name == last_card_name, 'Заголовок элемента в корзине не равен последнему элементу'

        # 14. Нажать на кнопку "Continue Shopping" для возврата к каталогу товаров.
            continue_shopping_button = browser.find_element(By.CSS_SELECTOR, 'button[data-test="continue-shopping"]')
            continue_shopping_button.click()
            assert browser.current_url == 'https://www.saucedemo.com/invertory.html', 'Не выполнен переход к списку товаров'

        # 15. Изменить фильтр в выпадающем списке с "Name (A to Z)" на "Price (low to high)".
            select = Select(browser.find_element(By.CSS_SELECTOR, 'select[data-test="product-sort-container"]'))
            select.select_by_value("Price (low to high)")

        # 16. Проверить, что список товаров отсортирован правильно: цена первого товара меньше цены последнего.
            first_card = browser.find_element(By.CSS_SELECTOR, 'div.inventory_item:first-child')
            first_card_price = first_card.find_element(By.CSS_SELECTOR, '*[data-test="inventory-item-price"]').text

            last_card = browser.find_element(By.CSS_SELECTOR, 'div.inventory_item:last-child')
            last_card_price = last_card.find_element(By.CSS_SELECTOR, '*[data-test="inventory-item-price"]').text

            assert first_card_price < last_card_price, \
                'При фильтре Price (low to high) список товаров отсортирован неправильно'
        finally:
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()
