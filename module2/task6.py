import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Открыть страницу http://suninjuly.github.io/alert_accept.html
# 2. Нажать на кнопку
# 3. Принять confirm
# 4. На новой странице решить капчу для роботов, чтобы получить число с ответом
# по завершению закрыть браузер

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # 1. Открыть страницу http://suninjuly.github.io/alert_accept.html
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome() # Открыть браузер
    browser.get(link) # перейти на страницу link

    # 2. Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

    # 3. Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # 4. На новой странице решить капчу для роботов, чтобы получить число с ответом
    # 4.1. Получить x
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    # 4.2. Ввести в поле ввода
    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(y)
    # 4.3. Нажать кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()