from selenium import webdriver
#from selenium.webdriver.support.ui import Select

import time
import math

#select = Select(browser.find_element_by_tag_name("select"))
#select.select_by_value("1") # ищем элемент с текстом "Python"

#link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)

#ищем картинку по идентификатору и вытаскиваем значение
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    sum = int(num1) + int(num2)

    print (sum)

    browser.find_element_by_id("dropdown").click()
    #browser.find_element_by_css_selector("[value='" + str(sum) + "']").click()
    browser.find_element_by_css_selector(f"[value='{sum}']").click()


    browser.find_element_by_css_selector("[type='submit']").click()

    time.sleep(10)
finally:
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла