import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Открыть страницу http://suninjuly.github.io/wait1.html
# 2. Нажать на кнопку "Verify"
# 3. Проверить, что появилась надпись "Verification was successful!"
# по завершению закрыть браузер

try:
    # 1. Открыть страницу http://suninjuly.github.io/wait1.html
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome() # Открыть браузер
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link) # перейти на страницу link

    # 2. Нажать на кнопку "Verify"
    button = browser.find_element(By.CSS_SELECTOR, 'button#verify')
    button.click()

    # 3. Проверить, что появилась надпись "Verification was successful!"
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()