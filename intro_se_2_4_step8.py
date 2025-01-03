from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


link = 'https://suninjuly.github.io/explicit_wait2.html'

try:
    browser_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=browser_service)
    browser.maximize_window()
    browser.get(link)

    price = Wait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element(By.ID, 'book')
    button.click()

    def calc(*args):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    send_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    send_answer.send_keys(y)

    solve = browser.find_element(By.ID, "solve")
    solve.click()

finally:
    time.sleep(15)
    browser.quit()
