from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from faker import Faker


try:
    link = "http://suninjuly.github.io/registration1.html"
    browser_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=browser_service)
    browser.maximize_window()
    browser.get(link)

    fake = Faker()
    word = fake.word()

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    first_name.send_keys(word)
    last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    last_name.send_keys(word)
    mail = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    mail.send_keys(word)
    phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
    address = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
