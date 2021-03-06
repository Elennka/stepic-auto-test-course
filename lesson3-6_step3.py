import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(2)
    browser.quit()

@pytest.mark.parametrize('page', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_correct_text_in_feedback(browser, page):
    link = f"https://stepik.org/lesson/{page}/step/1"
    browser.get(link)
   
    browser.implicitly_wait(10)
    input1=browser.find_element_by_class_name("textarea")
    input1.send_keys(str(math.log(int(time.time()))))
    
    
    browser.find_element_by_css_selector("button.submit-submission").click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    actual_result=browser.find_element_by_css_selector("pre.smart-hints__hint").text
   
    assert actual_result=="Correct!", print (actual_result)
    #ember97