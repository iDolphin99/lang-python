import numpy as np
import csv  # csv 파일을 쉽게 읽어드리기 위해 사용하는 모듈
import matplotlib.pyplot as plt

# 데이터를 읽어온다
f = open('age.csv')
data = csv.reader(f)
next(data) # data 첫 번째 row는 header이기 때문에 row 첫줄, header 정보를 건너뛰는 것

# 선택한 지역의 이름을 입력 받는다 
home = []
name = input("인구 구조가 알고 싶은 지역의 이름(읍면동 단위)를 입력해주세요: ")
for row in data :       # 데이터를 한 행씩 읽어옴 
    if name in row[0] : # 입력한 이름이 행정구역명 열과 같을 때 
        home = np.array(row[3:], dtype=int) 
        # 실제 엑셀의 첫 번째 줄은 header이므로 row 0번째 줄은 필요 없음
        # row의 3번 인덱스부터 처리, 0세가 시작하는 부분 
        # dtype = int : 리스트를 numpy 배열로 저장할 때 데이터 타입을 정수로 변환
print(home)
# 0세인구 1세인구 ... 100세인구 

plt.rc('font', family='Malgun Gothic') # rc() : 폰트, 글씨체를 지정해주는 함수 
plt.title(name+"지역의 인구 구조")
plt.plot(home)
plt.show()



### 선택한 지역과 가장 비슷한 인구구조를 가진 지역 찾기 ### 
# 선택한 지역의 각 세대별 인구 비율(home)을 다른 지역의 모든 세대별 인구 비율(away)과의 차이의 합을 계산 
# 지방은 인구수가 적고 서울은 인구수가 많기 때문에 인구수로 하는 것은 적절하지 않음 -> 인구비율로 따져야 함 
# csv에서 전체 인구수를 알고 있음, 각 나이대별 인구에 전체 인구수를 나눠줌으로써 비율을 알 수 있음 
# 비율을 전국의 모든 읍면동과 비교하고, 차이의 합이 가장 적은 동네가 가장 비슷한 지역이 됨 
# 하지만 차이의 합은 차이가 많이 나는 부분과 차이가 많이 나는 부분이 보상처리가 되어 (음수 <-> 양수) 좋은 방법이 아님 
# 차이의 합이 아닌, 차이 제곱의 합으로 바꿔야 함 
# 즉, 선택한 지역 - 모든 지역의 인구에 제곱(음수가 나올 수 있으므로) 한 값이 가장 작은 지역이 가장 비슷한 인구구조를 가짐 
for row in data : 
    away = np.array(row[3:], dtype=int)/int(row[2])
    s = np.sum((home-away)**2)          # home : 입력한 지역, away : 전체 읍면동의 인구 비율을 담음 
    if s < mn and name not in row[0] :  # 가장 작은 s가 나오는 곳이 result_name
        mn = s                          # not in row[0] : 입력한 home은 제외 
        result_name = row[0]
        result = away

# 선택한 지역의 인구 구조와 가장 비슷한 곳의 인구 구조를 시각화한다 
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.title(name+"지역과 가장 비슷한 인구 구조를 가진 지역")
plt.plot(home, label = name)
plt.plot(result, label = result_name)
plt.legend()
plt.show()