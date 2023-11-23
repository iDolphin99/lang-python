''' 
wine 통합 데이터 만들기 
1) 레드 와인과 화이트 와인의 ; 문자로 split하고 2.csv로 저장
2) 저장된 2.csv에 type 열을 추가해 각각 'red', 'white'값으로 채우고 두 데이터를 병합한다 (axis=0)
3) info() : 기본 정보를 확인할 수 있음 
'''


import pandas as pd

red_df = pd.read_csv('winequality-red.csv', sep=';', header=0, engine='python')     # sep 필수! 
white_df = pd.read_csv('winequality-white.csv', sep=';', header=0, engine='python')
red_df.to_csv('winquality-red2.csv', index=False)
white_df.to_csv('winquality-white2.csv', index=False)

red_df.insert(0, column = 'type', value='red')
white_df.insert(0, column = 'type', value='white')
wine_df = pd.concat([red_df,white_df], axis=0)                                      # 행과 열 중 열의 값이 같으므로 굳이 쓰지 않아도 위-아래로 연결됨
wine_df.columns = wine_df.columns.str.replace(' ', '_')
wine_df.to_csv('winequality.csv', index=False)
#print(wine_df)
#print(wine_df.info())     



''' 1) 기술 통계 구하기 '''
#print(wine_df.describe())
#print(sorted(wine_df.quality.unique()))
#print(wine_df.quality.value_counts())                                               # 9,8,3 과 같은 높/낮은 quality보다는 중간 quality 값들이 많이 존재함 

# 데이터 모델링 
# describe() 함수로 그룹 묶어서 비교하기 
'''
print(wine_df.groupby('type')['quality'].describe())            ,print()
print(wine_df.groupby('type')['quality'].mean())                ,print()
print(wine_df.groupby('type')['quality'].std())                 ,print()
print(wine_df.groupby('type')['quality'].agg(['mean','std']))   ,print()            # aggrigation, 집계 
'''



''' 2) 회귀 분석 모델 구하기 '''
from statsmodels.formula.api import ols,glm

Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'
regression_result = ols(Rformula, data=wine_df).fit()                               # 우리가 만든 회귀 분석 모델 
#print(regression_result.summary())

# 새로운 샘플 데이터의 품질 등급을 예측해보기 
# 샘플 데이터 1) 기존 wine에서 quality와 type을 제외한 sample1
# 샘플 데이터 2) 임의의 값을 딕셔너리 형태로 만들어 sample2
sample1 = wine_df[wine_df.columns.difference(['quality', 'type'])]                  # difference() : 기존 quality, type 열을 제외 한다 
sample1 = sample1[0:5][:]
sample1_predict = regression_result.predict(sample1)
#print(sample1_predict)                                          ,print("------------------ 정답 -----------------")
#print(wine_df[0:5]['quality'])

sample2_data = {"fixed_acidity": [8.5, 8.1], "volatile_acidity" : [0.8, 0.5], "citric_acid" : [0.3, 0.4], "residual_sugar" : [6.1, 5.8], "chlorides" : [0.055, 0.04], 
                "free_sulfur_dioxide" : [30.0, 31.0], "total_sulfur_dioxide" : [98.0, 0.99], "density" : [0.996, 0.91], "pH" : [3.25, 3.01], "sulphates" : [0.4, 0.35], "alcohol" : [9.0, 0.88]}
sample2 = pd.DataFrame(sample2_data, columns = sample1.columns)
sample2_predict = regression_result.predict(sample2)
#print(sample2_predict)



''' 3) 결과 시각화 - 히스토그램, 부분 회귀 플롯 '''
''' 히스토그램 '''
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set_style('dark')
red_wine_quality = wine_df.loc[wine_df['type']=='red', 'quality']
white_wine_quality = wine_df.loc[wine_df['type']=='white', 'quality']
#sns.distplot(red_wine_quality, kde=True, color='red', label='red wine')             # distplot() : kde 를 볼 수 있는 plot
#sns.distplot(white_wine_quality, kde=True, color='blue', label='white wine')
#plt.title("Quality of Wine Type")
#plt.legend()
#plt.show()

''' 부분 회귀 플롯 - fixed_acidity, volatile_acidity '''
import statsmodels.api as sm 

others = list(set(wine_df.columns).difference(set(['quality', 'fixed_acidity'])))
p, resids = sm.graphics.plot_partregress('quality', 'fixed_acidity', others, data=wine_df, ret_coords = True) # ret_coords : 잔차 데이터 반환 여부 
plt.show()

others = list(set(wine_df.columns).difference(set(['quality', 'volatile_acidity'])))
p, resids = sm.graphics.plot_partregress('quality', 'volatile_acidity', others, data=wine_df, ret_coords = True) # ret_coords : 잔차 데이터 반환 여부 
plt.show()

fig = plt.figure(figsize=(8,13))
sm.graphics.plot_partregress_grid(regression_result, fig=fig)
plt.show()
