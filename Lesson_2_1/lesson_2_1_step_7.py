from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

#ищем картинку по идентификатору и вытаскиваем значение
    find_img = browser.find_element_by_id("treasure")
    valuex = find_img.get_attribute("valuex")
    print("Found value: ", valuex)
    print("Result funccalc: ", calc(valuex))

    browser.find_element_by_id("answer").send_keys(calc(valuex))

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    time.sleep(1)


finally:
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла