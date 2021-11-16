from selenium import webdriver
import pytest
import time

@pytest.fixture

def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()
    

def input_field_and_send_form(link, first_name, last_name, user_email, browser):
    
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    first_field = browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']")
    first_field.send_keys(first_name)

    second_field = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']") 
    second_field.send_keys(last_name)    

    third_field = browser.find_element_by_xpath("//input[@placeholder = 'Input your email']") 
    third_field.send_keys(user_email)  

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()   

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)   

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text 
    
    return welcome_text      
     
def test_link_1(browser):
    result_func = input_field_and_send_form('http://suninjuly.github.io/registration1.html', 'First name', 'Last name', 'email@mail.ru', browser)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == result_func, "Failed"
def test_link_2(browser):
    result_func = input_field_and_send_form('http://suninjuly.github.io/registration2.html', 'First name', 'Last name', 'email@mail.ru', browser)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == result_func, "Failed"


