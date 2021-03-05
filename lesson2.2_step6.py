from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
   
    
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    

    browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    chkbx_option = browser.find_element_by_id("robotCheckbox")
    chkbx_option.click()
    
    radio_option = browser.find_element_by_id("robotsRule")
    radio_option.click()
    
    
    button.click()
    
    
	
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
  #  browser.quit()





