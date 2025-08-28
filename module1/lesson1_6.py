import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    time.sleep(2) # подождать 2 секунды
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome() # Открыть браузер
    browser.get(link) # перейти на страницу link
    button = browser.find_element(By.ID, "submit_button") # найти элемент по идентификатору
    button.click() # кликнуть по найденной кнопке
    time.sleep(10) # подождать 10 секунд

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
