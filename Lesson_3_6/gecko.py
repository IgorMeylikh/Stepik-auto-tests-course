# from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Firefox()
# driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
# driver.get("https://stepik.org/lesson/25969/step/8")



#Простой вариант
# link = "http://selenium1py.pythonanywhere.com/"

# def test_guest_should_see_login_link(browser):
#     browser.get(link)
#     browser.find_element_by_css_selector("#login_link")
#######################################################


# Параметризация тестов для выбора браузера

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"
drivers = ['webdriver.Chrome()', 'webdriver.Firefox()']

@pytest.mark.parametrize('browser', drivers)
def test_guest_should_see_login_link(browser):
    with eval(browser) as br:
        br.get(link)
        br.find_element_by_css_selector("#login_link")