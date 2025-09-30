from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SauceDemoProducts(BasePage):
    shopping_cart_link = (By.CSS_SELECTOR, '*[data-test="shopping-cart-link"]')
    filter_active_value = (By.CSS_SELECTOR, '*[data-test="active-option"]')

    def __init__(self, browser):
        super().__init__(browser)

    @property
    def url(self):
        return 'https://www.saucedemo.com/inventory.html'

    def open(self):
        self.go_to('/')
