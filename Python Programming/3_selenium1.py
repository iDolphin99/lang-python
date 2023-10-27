# How to use Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# browser 와 python 사이의 제어 driver가 필요함 
driver = webdriver.Chrome()

driver.get('http://www.python.org') 
element = driver.find_element(By.NAME, "q") # 찾은 객체를 변수에 저장 

# Python official document에서 "Go" button 찾기 
element.get_attribute('id')
element = driver.find_element(By.NAME, "submit")
element.click()

driver.close()
