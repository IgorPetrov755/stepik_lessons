from selenium.webdriver.common.by import By
from .base_page import BasePage


class SauceDemoCart(BasePage):
    """
    Page Object для страницы корзины Saucedemo.
    """

    # Локаторы
    cart_list = (By.CLASS_NAME, 'cart_list')
    cart_items = (By.CLASS_NAME, 'cart_item')
    continue_shopping_button = (By.ID, 'continue-shopping')
    checkout_button = (By.ID, 'checkout')
    item_name = (By.CLASS_NAME, 'inventory_item_name')
    item_price = (By.CLASS_NAME, 'inventory_item_price')

    @property
    def url(self):
        return '/cart.html'

    def get_cart_items(self):
        """Возвращает список товаров в корзине."""
        return self._find_elements(self.cart_items)

    def get_cart_items_count(self) -> int:
        """Возвращает количество товаров в корзине."""
        return len(self.get_cart_items())

    def get_cart_item_names(self) -> list:
        """Возвращает список названий товаров в корзине."""
        items = self.get_cart_items()
        return [item.find_element(*self.item_name).text for item in items]

    def continue_shopping(self):
        """Возвращается к странице продуктов."""
        self.click_element(self.continue_shopping_button)

    def proceed_to_checkout(self):
        """Переходит к оформлению заказа."""
        self.click_element(self.checkout_button)

    def wait_for_page_load(self):
        """Ожидает загрузки страницы корзины."""
        self.wait_for_element_to_be_visible(self.cart_list)