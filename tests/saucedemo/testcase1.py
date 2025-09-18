import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase1:
    def test_saucedemo(self):
        """Test Case 1: test"""
        # 1. Перейти на сайт Saucedemo.
        try:
            link = "https://www.saucedemo.com/"
            browser = webdriver.Chrome()  # Открыть браузер
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
            assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'Не выполнен редирект после логина'
            shopping_cart_link = browser.find_elements(By.CSS_SELECTOR, '*[data-test="shopping-cart-link"]')
            assert len(shopping_cart_link) == 1, 'Не найдена корзина'

        # 5. Проверить, что выбранный фильтр в выпадающем списке по умолчанию имеет значение "Name (A to Z)".
            filter_active_value = browser.find_element(By.CSS_SELECTOR, '*[data-test="active-option"]')
            assert filter_active_value.text == "Name (A to Z)", \
                'фильтр в выпадающем списке по умолчанию не имеет значение "Name (A to Z)"'

        # 6. Добавить первый товар из списка в корзину, нажав на кнопку "Add to cart".
        # 7. Проверить, что иконка корзины в правом верхнем углу отображает счетчик с цифрой 1.
        # 8. Добавить последний товар из списка в корзину, нажав на кнопку "Add to cart".
        # 9. Проверить, что значение счетчика на иконке корзины увеличилось и теперь отображает цифру 2.
        # 10. Удалить первый товар из корзины, нажав на кнопку "Remove" у первого товара в списке.
        # 11. Проверить, что значение счетчика на иконке корзины изменилось и теперь отображает цифру 1.
        # 12. Кликнуть на иконку корзины 🛒 в правом верхнем углу для перехода в корзину.
        # 13. Проверить, что добавленный товар (последний из списка) отображается на странице корзины.
        # 14. Нажать на кнопку "Continue Shopping" для возврата к каталогу товаров.
        # 15. Изменить фильтр в выпадающем списке с "Name (A to Z)" на "Price (low to high)".
        # 16. Проверить, что список товаров отсортирован правильно: цена первого товара меньше цены последнего.
        finally:
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()
