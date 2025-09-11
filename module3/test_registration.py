from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration:
    def test_registration1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            firstname_input = browser.find_element(By.XPATH, "//label[contains(text(),'First name')]//following::input")
            firstname_input.send_keys('My first name')

            lastname_input = browser.find_element(By.XPATH, "//label[contains(text(),'Last name')]//following::input")
            lastname_input.send_keys('My last name')

            email_input = browser.find_element(By.XPATH, "//label[contains(text(),'Email')]//following::input")
            email_input.send_keys('My email')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_registration2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            firstname_input = browser.find_element(By.XPATH, "//label[contains(text(),'First name')]//following::input")
            firstname_input.send_keys('My first name')

            lastname_input = browser.find_element(By.XPATH, "//label[contains(text(),'Last name')]//following::input")
            lastname_input.send_keys('My last name')

            email_input = browser.find_element(By.XPATH, "//label[contains(text(),'Email')]//following::input")
            email_input.send_keys('My email')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()
