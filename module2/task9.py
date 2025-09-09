import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# 3. Нажать на кнопку "Book"
# 4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# по завершению закрыть браузер

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome() # Открыть браузер
    browser.get(link) # перейти на страницу link

    # 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    #price = browser.find_element(By.CSS_SELECTOR, '#price')
    # говорим Selenium проверять в течение 5 секунд, пока появится цена со значением = 100$
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), text_='$100')
    )

    # 3. Нажать на кнопку "Book"
    book_button = browser.find_element(By.CSS_SELECTOR, '#book')
    book_button.click()

    # 4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
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
