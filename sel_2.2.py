from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, '#num1').text) + int(browser.find_element(By.CSS_SELECTOR, '#num2').text)


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(x))

    btn=browser.find_element(By.CSS_SELECTOR, 'button.btn-default')
    btn.click()


finally:
    print(x)
    time.sleep(10)
    browser.quit()