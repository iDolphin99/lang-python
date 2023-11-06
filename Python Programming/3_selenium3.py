# klas 내부 페이지는 iframe tag로 묶여 있어서 별도의 접근 방식이 필요함 
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # there is no needs to download chrome driver directly for selenium 

driver.get('https://klas.kw.ac.kr/')
element = driver.find_element(By.ID, "loginId") 
element.send_keys('2018204094')     # put your id 
element = driver.find_element(By.ID, "loginPwd")  
element.send_keys('Gluon0824@kw\n') # put your passwd 

# iframe tag를 찾아 접근 후 switch_to 함수를 통해 들어가야 함 
iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe)

driver.find_element(By.CSS_SELECTOR, '')

driver.close()