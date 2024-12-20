from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    pole = browser.find_element(By.CSS_SELECTOR, 'input.form-control[name="firstname"]')
    pole.send_keys('11')

    pole1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control[name="lastname"]')
    pole1.send_keys('11')

    pole2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control[name="email"]')
    pole2.send_keys('11')

    file=browser.find_element(By.CSS_SELECTOR, 'input#file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'answer.txt')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)

    btn=browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')

    btn.click()

finally:
    time.sleep(10)
    browser.quit()