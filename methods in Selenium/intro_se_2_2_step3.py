from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

link_1 = 'https://suninjuly.github.io/select1.html'
link_2 = 'https://suninjuly.github.io/selects2.html'

try:
    browser_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=browser_service)
    browser.maximize_window()
    browser.get(link_2)

    first_element = browser.find_element(By.ID, 'num1')
    first = first_element.text
    second_element = browser.find_element(By.ID, 'num2')
    second = second_element.text
    y = str(int(first) + int(second))
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
