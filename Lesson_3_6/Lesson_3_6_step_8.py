from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import time

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
browser = webdriver.Chrome(options=options)


# link = "http://selenium1py.pythonanywhere.com/"

# def test_guest_should_see_login_link_pass(browser):
#     browser.get(link)
#     browser.find_element_by_css_selector("#login_link")
#     time.sleep(3)

# def test_guest_should_see_login_link_fail(browser):
#     browser.get(link)
#     browser.find_element_by_css_selector("#magic_link")
#     time.sleep(3)