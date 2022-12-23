from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from math import log, sin

# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.
# Ваша программа должна:

# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
# Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.

# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу http://suninjuly.github.io/get_attribute.html.
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    treasure = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = treasure.get_attribute("valuex")

    # Посчитать математическую функцию от x (сама функция остаётся неизменной).
    func_x = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    answer.send_keys(func_x)
    # Отметить checkbox "I'm the robot".
    robot_checkbox_el = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    robot_checkbox_el.click()

    robot_rule = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    robot_rule.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()

    button_send = 30
    
finally:
        # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()