import os

from pages.saucedemo_landing import SauceDemoLanding
from dotenv import load_dotenv

INVALID_LOGIN_MESSAGE = 'Epic sadface: Username and password do not match any user in this service'
LOCKED_USER_MESSAGE = 'Epic sadface: Sorry, this user has been locked out.'

load_dotenv(True)


class TestSaucedemoLogin:
    def test_success_login(self, browser):
        """Тест успешной авторизации в системе"""
        page = SauceDemoLanding(browser)
        page.open()
        page.login(username='standard_user', password='secret_sauce')
        assert 'inventory' in browser.current_url

    def test_invalid_username(self, browser):
        """Тест ошибки при неверном логине"""
        page = SauceDemoLanding(browser)
        page.open()
        page.fill_username(username='testtest')
        page.fill_password(password='secret_sauce')
        page.submit()
        error_text = page.get_element_text(page.error_msg)
        assert error_text == INVALID_LOGIN_MESSAGE

    def test_invalid_password(self, browser):
        """Тест ошибки при неверном пароле"""
        page = SauceDemoLanding(browser)
        page.open()
        page.fill_username(username='standard_user')
        page.fill_password(password='testtest')
        page.submit()
        error_text = page.get_element_text(page.error_msg)
        assert error_text == INVALID_LOGIN_MESSAGE


    def test_login_blocked_user(self, browser):
        """Тест входа заблокированного пользователя"""
        page = SauceDemoLanding(browser)
        page.open()
        page.fill_username(username='locked_out_user')
        page.fill_password(password='secret_sauce')
        page.submit()
        error_text = page.get_element_text(page.error_msg)
        assert error_text == LOCKED_USER_MESSAGE
