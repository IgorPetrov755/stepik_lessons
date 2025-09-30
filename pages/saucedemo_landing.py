from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SauceDemoLanding(BasePage):
    logo = (By.CSS_SELECTOR, '.login_logo')

    def open(self):
        self.go_to('/')
