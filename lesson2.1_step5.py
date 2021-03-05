from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
   
    
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    
    chkbx_option = browser.find_element_by_id("robotCheckbox")
    chkbx_option.click()
    
    radio_option = browser.find_element_by_id("robotsRule")
    radio_option.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    
	
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
  #  browser.quit()