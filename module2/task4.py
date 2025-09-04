import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Открыть страницу https://SunInJuly.github.io/execute_script.html.
# 2. Считать значение для переменной x.
# 3. Посчитать математическую функцию от x.
# 4. Проскроллить страницу вниз на 100px.
# 5. Ввести ответ в текстовое поле.
# 6. Выбрать checkbox "I'm the robot".
# 7. Переключить radiobutton "Robots rule!".
# 8. Нажать на кнопку "Submit".

try:
    # 1. Открыть страницу https://SunInJuly.github.io/execute_script.html.
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    # ...

    # 4. Проскроллить страницу вниз на 100px.
    browser.execute_script("window.scrollBy(0, 100);")

    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
