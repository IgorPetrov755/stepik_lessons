import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Открыть страницу http://suninjuly.github.io/file_input.html
# 2. Заполнить текстовые поля: имя, фамилия, email
# 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# 4 .Нажать кнопку "Submit"

try:
    # 1. Открыть страницу http://suninjuly.github.io/file_input.html
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome() # Открыть браузер
    browser.get(link) # перейти на страницу link

    # 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file_input = browser.find_element(By.CSS_SELECTOR, '#file')  # input[type="file"]
    file_input.send_keys(file_path)  # ввести путь в поле ввода

    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
