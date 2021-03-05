from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try: 
   
    
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
   
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(int(x)+int(y)))    
   
    
    
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    
	
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()