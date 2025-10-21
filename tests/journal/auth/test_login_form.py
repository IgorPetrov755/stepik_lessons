import pytest
import os
import time

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

# JOURNAL_BASE_URL = os.getenv('JOURNAL_BASE_URL')
# JOURNAL_LOGIN = os.getenv('JOURNAL_LOGIN')
# JOURNAL_PASSWORD = os.getenv('JOURNAL_PASSWORD')
JOURNAL_BASE_URL = ''
JOURNAL_LOGIN = ''
JOURNAL_PASSWORD = ''
STUDENT_NAME = 'Афанасьев Андрей Анатольевич'

@pytest.mark.skip('Задайте переменные JOURNAL_LOGIN.. и тогда удалите эту строку')
class TestLoginJournal:
    def test_successful_login(self, browser):
        # 1. Перейти на страницу авторизации
        browser.get(url=JOURNAL_BASE_URL)
        # 2. Ввести логин
        login_field = browser.find_element(By.CSS_SELECTOR, "#username")
        login_field.send_keys(JOURNAL_LOGIN)
        # 3. Ввести пароль
        password_field = browser.find_element(By.ID, "password")
        password_field.send_keys(JOURNAL_PASSWORD)
        # 4. Нажать вход
        login_button = browser.find_element(By.CSS_SELECTOR, "button.login-action")
        login_button.click()
        # 5. Проверить, что вход выполнен успешно.
        elements = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".fio-stud"))
        )
        for elem in elements:
            if elem.is_displayed():
                fio_student = elem
                break
        assert fio_student.text == STUDENT_NAME, 'После входа не найдено ФИО студента'

    def test_change_languange(self, browser):
        """Проверка смены языка"""
        ru_button_locator = (By.XPATH, "//button[contains(., 'RU')]")
        en_button_locator = (By.XPATH, "//button[contains(., 'EN')]")
        username_locator = (By.CSS_SELECTOR, "#username")
        password_locator = (By.CSS_SELECTOR, "#password")
        login_button_locator = (By.CSS_SELECTOR, "button.login-action")

        # 1. Перейти на страницу авторизации
        browser.get(url=JOURNAL_BASE_URL)
        # 2. Проверить, что русский язык выставлен по умолчанию
        ru_button = browser.find_element(*(ru_button_locator))
        assert "background: rgb(221, 221, 221)" in ru_button.get_attribute("style")

        username = browser.find_element(*(username_locator))
        username_text = username.get_attribute("placeholder")
        assert username_text == 'Логин'
        password = browser.find_element(*(password_locator))
        password_text = password.get_attribute("placeholder")
        assert password_text == 'Пароль'
        login_button = browser.find_element(*(login_button_locator))
        assert login_button.text == 'Вход'

        # 3. Сменить язык
        en_button = browser.find_element(*(en_button_locator))
        en_button.click()
        assert "background: rgb(221, 221, 221)" in en_button.get_attribute("style")

        # 4. Проверить обновленный текст
        time.sleep(1)
        username_text = username.get_attribute("placeholder")
        assert username_text == 'Login'
        password_text = password.get_attribute("placeholder")
        assert password_text == 'Password'
        assert login_button.text == 'Enter'
