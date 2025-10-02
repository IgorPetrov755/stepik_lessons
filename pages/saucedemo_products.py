from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SauceDemoProducts(BasePage):
    """
    Page Object для страницы продуктов Saucedemo.
    """

    # Локаторы
    inventory_list = (By.CLASS_NAME, 'inventory_list')
    inventory_items = (By.CLASS_NAME, 'inventory_item')
    shopping_cart_link = (By.CLASS_NAME, 'shopping_cart_link')
    shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
    filter_dropdown = (By.CLASS_NAME, 'product_sort_container')
    filter_active_value = (By.CLASS_NAME, 'active_option')
    add_button = (By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')

    @property
    def url(self):
        return '/inventory.html'

    def get_all_products(self):
        """Возвращает список всех продуктов на странице."""
        return self._find_elements(self.inventory_items)

    def get_first_product(self):
        """Возвращает первый продукт в списке."""
        products = self.get_all_products()
        return products[0] if products else None

    def get_last_product(self):
        """Возвращает последний продукт в списке."""
        products = self.get_all_products()
        return products[-1] if products else None

    def add_product_to_cart(self, product_element):
        """
        Добавляет продукт в корзину.

        Args:
            product_element: WebElement продукта
        """
        add_button = product_element.find_element(By.CSS_SELECTOR, 'button.btn_inventory')
        add_button.click()

    def remove_product_from_cart(self, product_element):
        """
        Удаляет продукт из корзины.

        Args:
            product_element: WebElement продукта
        """
        remove_button = product_element.find_element(By.CSS_SELECTOR, 'button.btn_inventory')
        remove_button.click()

    def get_product_name(self, product_element):
        """Возвращает название продукта."""
        return product_element.find_element(By.CSS_SELECTOR, '.inventory_item_name').text

    def get_product_price(self, product_element):
        """Возвращает цену продукта."""
        price_text = product_element.find_element(By.CSS_SELECTOR, '.inventory_item_price').text
        return float(price_text.replace('$', ''))

    def get_cart_items_count(self) -> int:
        """
        Возвращает количество товаров в корзине.

        Returns:
            int: Количество товаров (0 если корзина пуста)
        """
        try:
            badge = self._find_element(self.shopping_cart_badge)
            return int(badge.text)
        except NoSuchElementException:
            return 0

    def go_to_cart(self):
        """Переходит в корзину."""
        self.click_element(self.shopping_cart_link)

    def select_filter(self, filter_value: str):
        """
        Выбирает фильтр сортировки.

        Args:
            filter_value: Значение фильтра (az, za, lohi, hilo)
        """
        self.select_dropdown_by_value(self.filter_dropdown, filter_value)

    def get_current_filter(self) -> str:
        """Возвращает текст активного фильтра."""
        return self.get_element_text(self.filter_active_value)

    def wait_for_page_load(self):
        """Ожидает загрузки страницы продуктов."""
        self.wait_for_element_to_be_visible(self.inventory_list)