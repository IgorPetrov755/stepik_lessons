import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 1. Открыть страницу https://suninjuly.github.io/selects1.html
# 2. Посчитать сумму заданных чисел
# 3. Выбрать в выпадающем списке значение равное расчитанной сумме
# 4. Нажать кнопку "Submit"

try:
    # 1. Открыть страницу https://suninjuly.github.io/selects1.html
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome() # Открыть браузер
    browser.get(link) # перейти на страницу link

    # 2. Посчитать сумму заданных чисел
    num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    num1 = int(num1.text)
    num2 = int(num2.text)
    summa = num1 + num2

    # 3. Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summa))

    # 4. Нажать кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
