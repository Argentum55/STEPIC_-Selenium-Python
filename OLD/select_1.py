from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time 
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    # добавляем товар в корзину
    num1_el = browser.find_elements(By.CSS_SELECTOR, "[id = 'num1']")
    num1 = num1_el.text
    num2_el = browser.find_elements(By.CSS_SELECTOR, "[id = 'num2']")
    num2 = num2_el.text
    sum = int(num1)+int(num2)

    select = browser.find_elements(By.CSS_SELECTOR, "[id = 'dropdown']")
    select.click()
    select.select_by_value(sum)

finally:
        # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()