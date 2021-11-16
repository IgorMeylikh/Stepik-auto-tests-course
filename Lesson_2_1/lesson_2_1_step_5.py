from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Получаем значение элемента по идентификатору контейнера
    input_value = browser.find_element_by_id("input_value").text;
    result_func = calc(input_value)
   
    browser.find_element_by_id("answer").send_keys(result_func)

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    time.sleep(20)

    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    #welcome_text = welcome_text_elt.text

    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()




