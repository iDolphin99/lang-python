'''
크롤링 예제 : 할리스커피 매장 정보 

한 페이지에는 마정 전체가 아닌 10개의 매장 정보 
나머지 매장은 페이지 맨 아래에 있는 페이지 번호 확인 pageNo=2, 3... 57
'''


import re
import requests 
from bs4 import BeautifulSoup

import urllib.request
import pandas as pd
import datetime

def hollys_store(result) :
    for page in range(1,57) : 
        url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' % page
        #print(url)
        html = urllib.request.urlopen(url)
        soupHollys = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupHollys.find('tbody') 
        for store in tag_tbody.find_all('tr') :
            if len(store) <= 3 : 
                break 
            store_td = store.find_all('td')
            store_sido = store_td[0].string 
            store_name = store_td[1].string 
            store_address = store_td[3].string 
            store_phone = store_td[5].string 
            result.append([store_name] + [store_sido] + [store_address] + [store_phone])

def main() : 
    results = [] 
    print("Hollys store crawling >>>>>>>>>>>>>>>>>>>")
    hollys_store(results)
    hollys_tbl = pd.DataFrame(results, columns = ('store', 'sido-gu', 'address', 'phone'))
    hollys_tbl.to_csv('hollys.csv', encoding='cp949', mode = 'w', index= True)
    del results[:]

if __name__ == '__main__' :
    main()