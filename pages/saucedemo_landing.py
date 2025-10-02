from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SauceDemoLanding(BasePage):
    logo = (By.CSS_SELECTOR, '.login_logo')
    login_button = (By.CSS_SELECTOR, '*[data-test="login-button"]')
    username_input = (By.CSS_SELECTOR, 'input[data-test="username"]')
    password_input = (By.CSS_SELECTOR, 'input[data-test="password"]')

    def open(self):
        self.go_to('/')

    def wait_for_page_load(self):
        """Ожидает загрузки страницы логина."""
        self.wait_for_element_to_be_visible(self.login_button)

    def login(self, username: str, password: str):
        """
        Выполняет вход в систему.

        Args:
            username: Логин пользователя
            password: Пароль пользователя
        """
        self.fill_element(locator=self.username_input, text_to_type=username)
        self.fill_element(locator=self.password_input, text_to_type=password)
        self.click_element(self.login_button)
