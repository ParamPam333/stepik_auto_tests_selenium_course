from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')
    x = x_element.text
    y = calc(x)

    pole = browser.find_element(By.CSS_SELECTOR, '.form-control#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", pole)
    time.sleep(2)
    pole.send_keys(y)

    check=browser.find_element(By.CSS_SELECTOR, '.form-check-input#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    time.sleep(2)
    check.click()

    radio=browser.find_element(By.CSS_SELECTOR, '.form-check-input#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    time.sleep(2)
    radio.click()

    btn=browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    time.sleep(2)
    btn.click()

finally:
    print(x)
    time.sleep(10)
    browser.quit()