import unittest
import time
from selenium import webdriver

class TestReg(unittest.TestCase):
            

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
        browser.find_element_by_css_selector(".first_block .second").send_keys("Ivan")
        browser.find_element_by_css_selector(".first_block .third").send_keys("test@test.ru")
        browser.find_element_by_css_selector("button.btn.btn-default").click()
 
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
				
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be absolute value of a number")
        browser.quit()
        
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
        browser.find_element_by_css_selector(".first_block .second").send_keys("Ivan")
        browser.find_element_by_css_selector(".first_block .third").send_keys("test@test.ru")
        browser.find_element_by_css_selector("button.btn.btn-default").click()
        
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be absolute value of a number")
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()