from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Рассчет
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    x = int(num1.text)
    y = int(num2.text)
    result = x + y

    # Выбор
    select = Select(browser.find_element_by_tag_name("select"))
    print(result)
    select.select_by_value(str(result))

    # Отправляем
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
