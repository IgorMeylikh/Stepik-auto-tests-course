from selenium import webdriver
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_value = browser.find_element_by_id('input_value').text

    browser.find_element_by_id('answer').send_keys(calc(input_value))

    browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
    radio_robot = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robot)
    radio_robot.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robot)
    #_ = button.location_once_scrolled_into_view
    time.sleep(1)
    
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла