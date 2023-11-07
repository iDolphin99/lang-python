from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os
import urllib.request

# 1) Settings
current_path = os.getcwd() 
SCROLL_PAUSE_TIME = 1
NUMBER_OF_IMAGE = 20
SEARCH_WORDS = ["임시완", "강동원"]

# 2) Chrome 브라우저를 띄운 후 이미지 검색창으로 이동
driver = webdriver.Chrome()  
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")

# 3) 검색하고자 하는 단어 List로 부터 하나씩 꺼내서 검색 시작
for search_word in SEARCH_WORDS:
    element = driver.find_element(By.NAME, "q")  
    element.clear()
    element.send_keys(search_word)  
    element.send_keys(Keys.RETURN)
    
    # 4) 이미지 검생창의 최대 스크롤 길이 확보
    print("이미지 창 스크롤 길이 계산")
    last_height = driver.execute_script("return document.body.scrollHeight")  # Get scroll height from javascript
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 최하단(Bottom)까지 스크롤
        time.sleep(SCROLL_PAUSE_TIME)  # 페이지가 모두 로딩되기 전에 스크롤 길이를 구할 경우 에러가 발생하여 로딩을 기다리는 코드 추가
        new_height = driver.execute_script("return document.body.scrollHeight")  # Calculate new scroll height and compare with last scroll height
        if new_height == last_height:  # 스크롤을 최대로 내렸을 경우 
            try:    # [더 찾아보기] 버튼 클릭
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except: # [더 찾아보기] 버튼이 없을 경우 탈출  
                break
        last_height = new_height

    # 5) 이미지를 저장할 폴더 이름 설정
    folder_name = search_word           # 검색명과 동일한 이름의 폴더 생성 
    if not os.path.isdir(folder_name):  # 기존에 동일한 폴더가 존재하지 않을 경우 새로 생성
        os.mkdir(folder_name)

    # 6) 사전에 설정한 개수만큼의 이미지 크롤링 시작
    print("이미지 얻기 시작")            
    count = 0
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    for image in images:
        try:
            image.click()
            time.sleep(2)
            imgXpath = '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]'
            imgUrl = driver.find_element(By.XPATH, imgXpath).get_attribute("src")
            imgUrl.replace('https', 'http') 
            opener = urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, folder_name + "/" + search_word + "." + str(count) + ".jpg")
            count = count + 1
            if count == NUMBER_OF_IMAGE:  # 원하는 개수만큼 저장하였을 경우 탈출 
                print(count, "개의 이미지 저장")
                break
        except Exception as e:            # error상황을 찾기 위한 코드 
            print("Error: ", e) 
            pass
    
    # 7) driver를 뒤로 돌려(뒤로 가기) 검색 List의 다음 단어로 넘어감 
    driver.back()

# 8) 검색 단어 List 속 이미지명 마다 지정된 개수만큼 크롤링을 모두 마무리 할 경우 종료
print("웹 이미지 크롤링 자동화 프로그램 종료")
driver.close()