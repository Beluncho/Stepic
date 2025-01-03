from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=browser_service)
    browser.maximize_window()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(*args):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    send_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    send_answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
