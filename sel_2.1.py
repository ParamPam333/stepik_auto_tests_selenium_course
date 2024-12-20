from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')
    x = x_element.text
    y = calc(x)

    pole = browser.find_element(By.CSS_SELECTOR, '.form-control#answer')
    pole.send_keys(y)

    check=browser.find_element(By.CSS_SELECTOR, '.form-check-input#robotCheckbox')
    check.click()

    radio=browser.find_element(By.CSS_SELECTOR, '.form-check-input#robotsRule')
    radio.click()

    btn=browser.find_element(By.CSS_SELECTOR, 'button.btn-default')
    btn.click()


finally:
    print(x)
    time.sleep(10)
    browser.quit()