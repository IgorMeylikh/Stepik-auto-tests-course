import os
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_field = browser.find_element_by_name('firstname')
    first_field.send_keys("First name")
    
    second_field = browser.find_element_by_name('lastname')
    second_field.send_keys("Last name")    

    third_field = browser.find_element_by_name('email')
    third_field.send_keys("mail@mail.ru")  

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)

    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)

    element = browser.find_element_by_css_selector('[type="file"]')
    element.send_keys(file_path)

    browser.find_element_by_tag_name('button').click()
    time.sleep(3)

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла