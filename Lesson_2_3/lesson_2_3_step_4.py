from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()
    time.sleep(1)

    alert = browser.switch_to.alert
    alert.accept()    

    input_value = browser.find_element_by_id('input_value').text

    browser.find_element_by_id('answer').send_keys(calc(input_value))

    browser.find_element_by_tag_name("button").click()    

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла