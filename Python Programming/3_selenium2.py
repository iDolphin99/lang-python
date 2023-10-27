# klas 페이지에서 mycoupang 들어가기 
# coupang 로그인 자동화 방법 찾아보기~ 
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://klas.kw.ac.kr/')
element = driver.find_element(By.ID, "loginId") 
element.send_keys('2018204094')     # put your id 
element = driver.find_element(By.ID, "loginPwd")  
element.send_keys('Gluon0824@kw\n') # put your passwd 

driver.close()