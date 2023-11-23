''' 
상관 분석 Correlation analysis 

language와 english, math, science가 각각 관계를 가지고 있을까?  
-> 인과관계는 알 수 없음을 명심 
'''


import os
import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

path = os.getcwd()
student = pd.read_csv(path + '\Big Data Language\Dataset\student.csv')
#print(student.info())

#print(student.corr(method='pearson'))                       ,print()
#print(student['math'].corr(student['science']))             ,print()

sns.pairplot(student, hue='math')
plt.show()

