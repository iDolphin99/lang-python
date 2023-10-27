from bs4 import BeautifulSoup

r = BeautifulSoup.requests.get('https://www.yes24.com/Product/Goods/122774229')
print(r.encoding) # utf-0
 
# parsing 정보를 문서로 저장 -> 가져온 정보가 많을 경우 한 번 저장해주면 좋음 
open('the planning.html', 'w').wrtie(r.text) 

html = open('the planning.html').read()
print(html)

print(html.title)
print(html.find_all('a'))  # a tag (link)를 사용한 부분을 전부 추출 
print(html.find_all('h2')) # h2는 시각적인 속성이긴 함 
print(html.find_all('h2', attrs={'class': 'gd_name'})[0])
print(html.find_all('h3', attrs={'class': 'gd_nameE'})[0])