from selenium import webdriver
import time

link = "https://SunInJuly.github.io/execute_script.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    time.sleep(1)
    _ = button.location_once_scrolled_into_view

    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла