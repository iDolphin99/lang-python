'''
지오 데이터 분석 

주소 데이터 수집 - 커피빈 매장 데이터를 크롤링으로 수집, 이를 정규화 처리를 해주어야 함 
주소 체계 변경 - 서울, 서울시, 서울특별시 등 여러 지명이 존재하므로 "행정구역주소체계"에 맞게 변경, 띄어쓰기로 분리 
분석 모델 구축 및 시각화 - 지도 객체 생성

'''


# 1) Pandas로 데이터 로딩하기 
import pandas as pd 
CB = pd.read_csv("CoffeeBean.csv", encoding="CP949", index_col=0, header=0, engine='python')
#print(CB.head())


# 2) 주소 체계 변경 
addr1 = []
for address in CB.address :
    addr1.append(str(address).split())
#print(addr1)

addr2 = []
for i in range(len(addr1)) : 
    if addr1[i][0] == "서울" : addr1[i][0] = "서울특별시"
    elif addr1[i][0] == "서울시" : addr1[i][0] = "서울특별시"
    elif addr1[i][0] == "부산시" : addr1[i][0] = "부산광역시"
    elif addr1[i][0] == "인천" : addr1[i][0] = "인천광역시"
    elif addr1[i][0] == "광주" : addr1[i][0] = "광주광역시"
    elif addr1[i][0] == "대전시" : addr1[i][0] = "대전광역시"
    elif addr1[i][0] == "울산시" : addr1[i][0] = "울산광역시"
    elif addr1[i][0] == "세종시" : addr1[i][0] = "세종특별자치시"
    elif addr1[i][0] == "경기" : addr1[i][0] = "경기도"
    elif addr1[i][0] == "충북" : addr1[i][0] = "충청북도"
    elif addr1[i][0] == "충남" : addr1[i][0] = "충청남도"
    elif addr1[i][0] == "전북" : addr1[i][0] = "전라북도"
    elif addr1[i][0] == "전남" : addr1[i][0] = "전라남도"
    elif addr1[i][0] == "경북" : addr1[i][0] = "경상북도"
    elif addr1[i][0] == "경남" : addr1[i][0] = "경상남도"
    elif addr1[i][0] == "제주" : addr1[i][0] = "제주특별자치도"
    elif addr1[i][0] == "제주도" : addr1[i][0] = "제주특별자치도"
    elif addr1[i][0] == "제주시" : addr1[i][0] = "제주특별자치도"
    
    addr2.append(' '.join(addr1[i]))

#print(addr2)
    

# 3) 결과를 DataFrame 타입으로 변경하고 컬럼 이름을 address2 추가
# CB와 addr2를 옆으로 결합(axis=1)하여 CB2 생성 
# CoffeeBean2.csv 저장 
# 전처리 작업 완료 
addr2 = pd.DataFrame(addr2, columns=['address2'])
CB2 = pd.concat([CB, addr2], axis=1)
CB2.to_csv('CoffeBean2.csv', encoding='CP949', index=False)
print(CB2.head())


# 4 - test) 지도 객체 생성 - 포리움 라이브러리 사용 
# Map() : (입력한)위도와 경도를 GPS 좌표를 중심 위치로 하는 지도 객체 생성 
import folium

map_test = folium.Map(location=[37.559943,126.975314], zoom_start=16) # zoom_start : 확대의 단위
map_test.save('map_test.html')


# 4) 매장의 행정주소를 모두 위도와 경도 좌표로 전환 
# 오픈소스인 Geocoder-Xr 이용 
# CB_geo.ship.csv 파일 생성 
CB_geoData = pd.read_csv('CB_geo.ship.csv', encoding = 'CP949', engine='python')
map_CB = folium.Map(location=[37.559943,126.975314], zoom_strat=15)
for i, store in CB_geoData.iterrows() :
    folium.Marker(location=[store['위도'], store['경도']], popup=store['store'], icon=folium.Icon(color='red', icon='star')).add_to(map_CB)
map_CB.save('map_CB.html')

import webbrowser 
webbrowser.open('map_CB.html')
