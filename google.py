from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 


link = "https://www.google.com/"

try:
    browser = webdriver.Chrome('chromedriver') 
    browser.get(link)
    
    browser.find_element_by_tag_name("input[title=\"Поиск\"]").send_keys("мама")
    browser.find_element_by_xpath("(//input[@name='btnK'])[2]").click()
    
    time.sleep(5)
    number_of_pages=len(browser.find_elements(By.CSS_SELECTOR,"a[class=fl][aria-label]"))+1
    number_of_elements=len(browser.find_elements_by_class_name("g"))
    
 
    
    print (number_of_pages)
    for i in range(1,100,1): 
        time.sleep(1)
        if i!=1: # если не 1-я страница, то переходим на следующую  подсчитываем количество элементов
            
            try:     
                my_selector="a[class=fl][aria-label=\"Page "+str(i)+"\"]"
                browser.find_element(By.CSS_SELECTOR,my_selector).click()  
            except: break
            
        try:
            if browser.find_element_by_xpath('//a[contains(@href,"avito.ru")]'): print ("элемент на "+str(i)+"странице") 
        except: print ("элемент на "+str(i)+"странице не найден")   
        # 
    
     #  browser.find_elements(By.CSS_SELECTOR,"div[class=g] > div > div:nth-child(1) > a")[2].click()
    #rso > div > div:nth-child(5) > div > div.yuRUbf > a
  #  print (number_of_pages)  "div[class=g] > div > div:nth-child(1) > a[contains(@href,\"mvideo\")]"
    
  #  for j in range(1,number_of_elements,1): #поиск по элементам на странице
 #  $$('div[class=g] > div > div:nth-child(1) > a')
  #  
  
   #if browser.find_element(By.CSS_SELECTOR,"div[class=g] > div > div:nth-child(1) > a[contains(text(), \"mvideo.ru\")]"): print ("элемент на "+i+"странице")
   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла