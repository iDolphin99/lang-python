'''
데이터 수집 - "1000개의 해외 학술 문서 제목 분석"
데이터 처리 - 파일 병합하기 
데이터 전처리 - "제목" 추출, nltk 라이브러리 사용 
데이터 탐색 - 단어 빈도 구하기 
워드 클라우드 시각화 

glob 모듈 : 경로와 이름을 지정하여 파일을 다루는 파일 처리 작업을 위한 모듈 
            * : 모든 문자를 처리해줌, 아무 문자나 하나만 오면 됨 
람다 함수 : 정의 없이 간단하게 만드는 익명의 함수 
'''


# 1) glob 모듈을 이용해 데이터 읽어오기
import pandas as pd
import glob

all_files = glob.glob('myCabinetExcelData*.xls')
#print(all_files)


# 2) pandas의 DataFrame을 이용하여 각각의 엑셀 파일 읽어 10개를 저장하기 
all_files_data = []
for file in all_files :
    data_frame = pd.read_excel(file)
    all_files_data.append(data_frame)
#print(all_files_data[0])


# 3) pnadas 의 concat 메서드를 이용하여 10개의 엑셀 파일 병합하기 
all_files_data_concat = pd.concat(all_files_data, axis = 0, ignore_index = True)
#print(all_files_data_concat)


# 4) 수집한 데이터에서 제목을 추출하여 전처리 수행하기 
# cleaning 작업 완료, 본격적인 전처리 시작 
all_title = all_files_data_concat['제목']
#print(all_title)


# 5) nltk 라이브러리를 이용한 전처리 작업 실행 -> 제목에서 단어로 표제어를 추출하는 작업 
# 영어가 아닌 단어는 제거, 소문자로 정규화, 단어 토큰화 ,불용어 제거, 던어 형태를 일반화
# 표제어(기본 사전형 단어) 추출 작업 진행 
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

stopWords = set(stopwords.words("english"))
lemma = WordNetLemmatizer() 
words1 = [] # 모든 전처리가 끝난 단어들, 표제어를 넣을 예정 

for title in all_title : 
    EnWords = re.sub(r"[^a-zA-Z]+", " ", str(title))                        # sub() : () 가아니면 ()로 대체하라 -> 문자가 아니면 공백으로 대체하라 
    EnWordsToken = word_tokenize(EnWords.lower())
    EnWordsTokenStop = [w for w in EnWordsToken if w not in stopWords]      # stopwords에 있으면 처리하지 않겠다 
    EnWordsTokenStopLemma = [lemma.lemmatize(w) for w  in EnWordsTokenStop] # stopwords로 걸러진 것들의 표제어 추출 
    words1.append(EnWordsTokenStopLemma)
#print(words1)


# 6) 2차원 데이터를 1차원 데이터로 병합 
# reduce() : 2차원 리스트를 1차원 리스트로 줄이기 위한 함수 <- 원래는 리스트의 원소들을 다 더하는 경우에 사용함 
from functools import reduce 
words2 = list(reduce(lambda x,y : x+y, words1))
#print(words2)


# 7) 단어 빈도 구하기 
# Counter : 단어 별로 출현 횟수를 계산하기 위해 데이터 집합에서 개수를 자동으로 계산하기 위한 모듈 
# 출현 횟수가 많은 상위 50개 단어 중에서 단어 길이가 1보다 큰 것만 word_count 딕셔너리에 저장 
from collections import Counter 

count = Counter(words2)
print(count)

word_count = dict()
for tag, counts in count.most_common(50) : 
    if (len(str(tag))>1) :
        word_count[tag] = counts 
        print("%s : %d" %(tag, counts))
        

# 8) 워드 클라우드 시각화
# 워드 클라우드도 STOPWORD에 대해 따로 제공함  
from wordcloud import STOPWORDS, WordCloud 
import matplotlib.pyplot as plt 

stopwords = set(STOPWORDS)
wc = WordCloud(background_color = 'ivory', stopwords = stopwords, width=800, height=600)
cloud = wc.generate_from_frequencies(word_count)

plt.figure(figsize=(8,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()