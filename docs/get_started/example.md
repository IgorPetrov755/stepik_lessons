# Пример кода, который открывает указанную ссылку

```python 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Открыть страницу https://suninjuly.github.io/selects1.html
# по завершению закрыть браузер

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome() # Открыть браузер
    browser.get(link) # перейти на страницу link

    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
```