'''
Pandas로 인구 구조 분석하기 
'''


import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import csv

# 데이터 읽기 
# encoding 방식을 써줘야 한글이 덜 깨짐 
# index_col = 0 : 데이터를 읽을 때 기존 데이터의 0번째 열을 index로 그대로 사용하겠다 
df = pd.read_csv("age.csv", encoding="cp949", index_col=0)  
# 총 인구수가 0인 곳은 제외 
df = df[df["2021년04월_계_총인구수"]!=0]

# 서울과 지역의 인구수 차이가 큼 -> 비율로 따질 예정 
# 전체 column을 ""값으로 axis=0 행 방향으로 나누어준다 
df.div(df["2021년04월_계_총인구수"], axis=0)
del df["2021년04월_계_총인구수"], df["2021년04월_계_연령구간인구수"]
#print(df.head())

# 원하는 지역 입력받고 해당 지역의 인구 구조 저장 
name = input("원하는 지역의 이름을 입력해주세요: ")
a = df.index.str.contains(name) # 해당 행을 찾아서 해당 지역의 인구 구조를 저장, 행데이터를 저장 
df2 = df[a]
print(df2)

plt.rc("font", family="Malgun Gothic")
df2.T.plot() # 행과 열을 바꾸어줌 

# 원하는 지역의 인구구조와 가장 비슷한 인구 구조를 가진 지역 시각화하기 
# 궁금한 지역 A의 인구 비율에서 B의 인구 비율을 뺀다 
x = df.sub(df2.iloc[0], axis=1)
# A의 인구 비율에서 B의 인구 비율을 뺀 값에 제곱 값을 모두 더한다 
y = np.power(x,2)
z = y.sum(axis=1)
# sort_value 정렬 함수와 슬라이싱을 이용하여 상위 몇개 지역까지 찾을 수 있음
i = z.sort_values().index[:5]
# 결과를 꺽은선 그래프로 그려주면 됨 
df.loc[i].T.plot()
plt.show()