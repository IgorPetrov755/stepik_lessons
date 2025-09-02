import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome() # Открыть браузер
    browser.get(link) # перейти на страницу link

    sunduk = browser.find_element(By.CSS_SELECTOR, '#treasure')
    sunduk_valuex = sunduk.get_attribute("valuex")
    y = calc(sunduk_valuex)

    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(y)
    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robots_rule = browser.find_element(By.ID, 'robotsRule')
    robots_rule.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()


    time.sleep(10)  # подождать 10 секунд
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()