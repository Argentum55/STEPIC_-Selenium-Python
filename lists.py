import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# link = "https://suninjuly.github.io/selects1.html"
link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    select1 = browser.find_element(By.XPATH, "//span[@id='num1']")
    num1 = select1.text
    
    select2 = browser.find_element(By.XPATH, "//span[@id='num2']")
    num2 = select2.text     
    result_text = int(num1) + int(num2)

    browser.find_element(By.XPATH,"//select[@class='custom-select']").click()
    selector = Select(browser.find_element(By.XPATH,"//select[@class='custom-select']"))
    selector.select_by_visible_text(str(result_text))
    browser.find_element(By.XPATH, "//button[@class='btn btn-default']").click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()