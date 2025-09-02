import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    time.sleep(2) # подождать 2 секунды
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome() # Открыть браузер
    browser.get(link) # перейти на страницу link

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(y)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robots_rule = browser.find_element(By.ID, 'robotsRule')
    robots_rule.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    time.sleep(10) # подождать 10 секунд

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
