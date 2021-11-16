from selenium import webdriver

import unittest
import time

class TestLink(unittest.TestCase):
    def test_link_1(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            

            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            first_field = browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']")
            first_field.send_keys("First name")
            
            second_field = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']") 
            second_field.send_keys("Last name")    

            third_field = browser.find_element_by_xpath("//input[@placeholder = 'Input your email']") 
            third_field.send_keys("mail@mail.ru")  
        

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

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Failed")
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()        
    def test_link_2(self):
        try: 
            link = "http://suninjuly.github.io/registration2.html"
            

            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            first_field = browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']")
            first_field.send_keys("First name")
            
            second_field = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']") 
            second_field.send_keys("Last name")    

            third_field = browser.find_element_by_xpath("//input[@placeholder = 'Input your email']") 
            third_field.send_keys("mail@mail.ru")  
        

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

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Failed")
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()            
if __name__ == "__main__":
    unittest.main()
