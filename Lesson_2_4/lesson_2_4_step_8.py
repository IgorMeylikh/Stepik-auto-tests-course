from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element ((By.ID, 'price'), '100')
    )
    

    browser.find_element_by_id('book').click()

    browser.implicitly_wait(5)

    input_value = browser.find_element_by_id('input_value').text

    browser.find_element_by_id('answer').send_keys(calc(input_value))

    browser.find_element_by_id("solve").click()  

    
finally:
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла