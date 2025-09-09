import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
# 2. Нажать на кнопку
# 3. Переключиться на новую вкладку
# 4. Пройти капчу для робота и получить число-ответ
# по завершению закрыть браузер

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # 1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome() # Открыть браузер
    browser.get(link) # перейти на страницу link

    # 2. Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
    button.click()

    # 3. Переключиться на новую вкладку
    new_window = browser.window_handles[1] # узнать имя окна
    browser.switch_to.window(new_window) # переключиться на окно по имени

    # 4. Пройти капчу для робота и получить число-ответ
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