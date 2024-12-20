from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    btn=browser.find_element(By.CSS_SELECTOR, 'button.trollface ')
    btn.click()

    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y=calc(x)


    pole = browser.find_element(By.CSS_SELECTOR, '#answer')
    pole.send_keys(y)

    btn=browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')

    btn.click()

finally:
    print(browser.switch_to.alert.text)
    browser.quit()