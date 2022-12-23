from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

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
    add_button = browser.find_element(By.CSS_SELECTOR, ".add")
    add_button.click()

    # открываем страницу второго товара
    browser.get("https://fake-shop.com/book2.html")

    # добавляем товар в корзину
    add_button = browser.find_element(By.CSS_SELECTOR, ".add")
    add_button.click()

    # тестовый сценарий
    # открываем корзину
    browser.get("https://fake-shop.com/basket.html")

    # ищем все добавленные товары
    goods = browser.find_elements(By.CSS_SELECTOR, ".good")

    # проверяем, что количество товаров равно 2
    assert len(goods) == 2
finally:
        # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()