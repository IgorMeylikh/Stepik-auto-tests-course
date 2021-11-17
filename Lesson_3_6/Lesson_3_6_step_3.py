from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import time
import math



@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



#answer = math.log(int(time.time()))
class TestCheckForms:
    find_message = ''
    reference = 'Correct!'
    links_array = [
                    "https://stepik.org/lesson/236895/step/1", 
                    "https://stepik.org/lesson/236896/step/1",
                    "https://stepik.org/lesson/236897/step/1",
                    "https://stepik.org/lesson/236898/step/1",
                    "https://stepik.org/lesson/236899/step/1",
                    "https://stepik.org/lesson/236903/step/1",
                    "https://stepik.org/lesson/236904/step/1",
                    "https://stepik.org/lesson/236905/step/1"
                    ]

    # links_array = [
    #                 "https://stepik.org/lesson/236898/step/1",
    #                 "https://stepik.org/lesson/236899/step/1",
    #                 "https://stepik.org/lesson/236903/step/1",
    #                  ]         
    print (find_message)
    @pytest.mark.parametrize('link', links_array)
    def test_run_all_link(self, browser, link):
        
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_tag_name('textarea').send_keys(str(math.log(int(time.time()))))
        
        WebDriverWait(browser, 5).until_not(
            EC.element_to_be_clickable((By.CLASS_NAME, '.submit-submission'))
        )  
        button = browser.find_element_by_tag_name('button[class="submit-submission"]')
      
        button.click()
        time.sleep(0)
        attempt = WebDriverWait(browser, 5).until(
            (EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
            #(EC.visibility_of_element_located((By.ID, 'ember93')))
        )
        
        find_text = attempt.text
        if find_text != self.reference:
            self.find_message += find_text
    
