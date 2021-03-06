from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json 
import time 


link = "https://yandex.ru/"

try:
    browser = webdriver.Chrome('chromedriver') 
    browser.get(link)
    
    browser.find_element_by_link_text("Войти в почту").click()
    browser.switch_to.window(browser.window_handles[1])
    
    with open('tests.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
    
    
    browser.find_element_by_id("passp-field-login").send_keys("elennka.v@yandex.ru")
    browser.find_element_by_tag_name("button[type=\"submit\"]").click()
    
    try:
        if WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".Textinput-Hint.Textinput-Hint_state_error"))):
            print("Error in e-mail")
            exit()
    except: 
        print("E-mail exist")
    
    browser.find_element_by_id("passp-field-passwd").send_keys("Ak28Sl7788")
    time.sleep(1)
    browser.find_element_by_tag_name("button[type=\"submit\"]").click()
    try:
        if WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".Textinput-Hint.Textinput-Hint_state_error"))):
            print("Invalid password")
            exit()
    except: 
        print("You are welcome")
    
    
    
    
   
   

finally:
   
    time.sleep(5)
  #  закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла