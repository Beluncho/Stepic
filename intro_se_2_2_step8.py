from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from faker import Faker
import os


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=browser_service)
    browser.maximize_window()
    browser.get(link)

    fake = Faker()
    word = fake.word()

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
    first_name.send_keys(word)
    last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
    last_name.send_keys(word)
    mail = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
    mail.send_keys(word)

    choose_file = browser.find_element(By.ID, 'file')
    with open('test.txt', 'w') as file:                         # Создаем файл
        content = file.write(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))    # задаем корректную
    file_path = os.path.join(current_dir, 'test.txt')           # ссылку (путь) к файлу.
    choose_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    path = 'test.txt'   # Del
    os.remove(path)     # file
    