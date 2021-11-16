from selenium import webdriver

#import unittest
import time



browser = webdriver.Chrome()
def input_field_and_send_form(link, first_name, last_name, user_email):
    
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
    #time.sleep(1)   

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text 
    
    return welcome_text     
    
    
def test_link_1():
    result_func = input_field_and_send_form('http://suninjuly.github.io/registration1.html', 'First name', 'Last name', 'email@mail.ru')
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == result_func, "Failed"
def test_link_2():
    result_func = input_field_and_send_form('http://suninjuly.github.io/registration2.html', 'First name', 'Last name', 'email@mail.ru')

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == result_func, "Failed"

#time.sleep(3)
#browser.quit
