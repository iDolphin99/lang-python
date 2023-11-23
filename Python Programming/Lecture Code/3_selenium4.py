# 기상청 홈페이지 들어가서 이번 주 날씨 정보를 tbody tag 내에서 하나씩 꺼내기
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://https://www.weather.go.kr/w/index.do#close')

element = driver.find_element(By.NAME, "오늘") 
element.click()

rows = driver.find_elements(By.TAG_NAME, 'tr')
rlist = [e for e in rows[0].find_elements(By.TAG_NAME, 'id')]
print(rlist)

driver.close()