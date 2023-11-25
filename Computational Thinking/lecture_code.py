#1
name = input('이름이 뭔가요?')
print('만나서 반갑다', name, '아')
age = input('니 나이는?')
print('아.....', age, '살이군요')



#2
num1 = input('첫번째 정수 입력')
num2 = input('두번째 정수 입력') 
print(num1+num2) 



#3. 그래픽, 안하는걸로 알고 있음 
import turtle  #c에서는 #include <stdio.h>와 같음,
               #그래픽컬한 프로그래밍을 할 수 있음 
t = turtle.Pen()

t.pencolor('red')  #설정 안해주면 기본 검정색
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)



#4. 이진수 실습, 이거는 어렵, 외우는게 좋을 것 같음. 여기서 int는 함수 
dec = int ('000110', 2) #끝에 이진수임을 알려줌으로써 이에 해당하는 십진수를 알려줌
print(dec)
b = bin(168)
print(b)  #접두어  0b가 붙고 2진수로 168을 표현



#5
print(type(5))
print(type(5.0))
print(type('Hello'))
x = input('정수를 입력하시오: ')
y = float(x)
print(y)



#6. end = ' ', 공백 삽입 
x =10
print(x)
x = 10.0
print(x, end = ' ')
x = 'Hello'
print(x, end=', ')



#7. 오.. 의외로 자료형을 안써주면 문자열처럼 출력된다 주의하자
#주의, 숫자만 입력 가능 (int) 
x =float(input('데이터 입력 : '))
y =float(input('데이터 입력 : '))
print(x+y)



#8 (+#1) 
print('나는 현재 ' + str(20) + '살 입니다') 



#9 이렇듯 특정 인덱스 값을 변경할 수 있다 
shopping_list = ['milk','eggs','cheese']
print(shopping_list)
shopping_list[2] = 'noodle'
print(shopping_list)      



#10 append는 맨 뒤에 데이터 삽입 , pop은 맨 뒤에 데이터부터 꺼내기 
shopping_list = []
shopping_list.append('H')
shopping_list.append('e')
shopping_list.append('l')
shopping_list.append('l')
shopping_list.append('o')

print(shopping_list)

print(shopping_list.pop(), end='')
print(shopping_list.pop(), end='')
print(shopping_list.pop(), end='')
print(shopping_list.pop(), end='')
print(shopping_list.pop(), end='')        

i=0
while i<5 :
    print(shopping_list.pop(), end = ' ')
    i=i+1



#11. 1차 과제 알고리즘의 구현
strTmp = input("문자열 입력 : ")
shopping_list = []

for ch in strTmp :
    shopping_list.append(ch)
length = len(strTmp)
while length> 0 :
    print(shopping_list.pop(), end=' ')
    length = length - 1 



#12  
def Add(n1, n2) : #함수 정의
    result = n1 + n2
    #global result = n1 + n2 #global 전역 변수 설정할때 쓰는 키워드 
    return result

result = Add(23,44)#함수 호출
print(result)



#13
def Calc(price, count) :
    ret = price * count
    return ret

total = 0
n = int(input('진주 개수 : '))
cost = int(input('개당 가격 : '))
total = total + Calc(cost, n)

n = int(input('사파이어 개수 : '))
cost = int(input('개당 가격 : '))
total = total + Calc(cost, n)

n = int(input('목걸이 줄 길이 :'))
cost = int(input('m당 가격 : '))
total = total + Calc(cost, n)

print(total)

#>>>> 공통적으로 반복되는 부분을 def함수화 

def Cal (price, count) :
    ret = price * count
    return ret

List1 = ['진주 개수','사파이어 개수','목걸이 줄 길이(cm)']
List2 = ['개당 가격?','개당 가격?','cm당 가격?']
List3 = []
total = 0
for i in range(3) :
    n = int (input(List1[i] + " : " ))
    cost = int (input(List2[i] + " : " ))
    total = Cal(cost, n)

print(total)

#>>> 반복문을 이용한다면! 



#14
greeting = 'Merry Christmas'
print(greeting[0])
print(greeting[1])
print(greeting[2])
greeting = greeting + ' Everybody'
print(greeting)

#>>> 문자열도 기본적으로 리스트적인 성질을 가지고 있지만, 요소 하나를 바꾸는 것은 어려우므로 리스트를 활용해야 한다 

List = ['a','b','c']
print(List)
List[1] = 'd'
print(List)



#15
strx = '홍길동은' + str(20) + '살' 



#16 문자열 슬라이싱 
word = input('단어 입력 : ')   #abc
first = word[0]                #a
new_word = word[1:] + first + 'ay' #bc + a + ay = bcaay
print(new_word) 

tmp = new_word[-3] + new_word[:-3] #a + bc
print(tmp)



#17 하노이탑 , 강의안 볼 때 같이 보셈 이거 아직 모르겟움 
def hanoi_tower(n, from_pole, to_pole, temp_pole):
    if n>= 1:
        hanoi_tower(n-1,from_pole,temp_pole,to_pole)
        move_disk(from_pole,to_pole)
        hanoi_tower((n-1),temp_pole,to_pole,from_pole)

def move_disk(from_pole,to_pole):
    print(from_pole,"에서",to_pole,"로 디스크를 이동한다")

hanoi_tower(3,'A','B','C')



#18
score = int(input("점수 입력"))
if score > 90 :
    print("A학점")
else :
    if score > 80 :
        print("B학점")
    else :
        if score > 70 :
            print ("C학점")
        else :
            if score > 60 :
                print("D학점")
            else :
                print ("F학점")



#19
sign = "stop"
while sign == "stop":
    sign = input ("신호 입력: ")
 
print ("OK 진행!!! ")



#20 구구단
i = 1
while i< 10 :
    print (2, 'x', i, '=', i*2)
    i = i+1

i = 2
while i < 10 :
    j = 1
    while j < 10 :
        print(i , 'x', j , '=', i*j, end = ' ')
        j += 1
    print()
    i += 1



#21 별찍기 / 이거 다른 사람들한테 소스코드 받아야겠다
i = 0
while i < 5:
    j=0
    while j<7 :
        print('*', end=' ')
        j = j + 1
    print()
    i= i+1



#22 random 함수 
import random

def rollDice () :
    facd = random.randint(1,6)
    return face

i=1
while i < 10 :
    print('주사위 값 : ', rollDice())
    i += 1 




#23 random 함수를 이용한 더하기 게임 
import random

while True :
    n1 = random.randint(1,99)
    n2 = random.randint(1,99)
    print(n1, '+', n2, '=')
    ans = int(input('답은? '))
    if ans == n1 + n2 :
        print('정답~!')
    else :
        print('틀렸음~!')


import random

i = 0
count = 0
while i < 5 :
    n1 = random.randint(1,99)
    n2 = random.randint(1,99)
    n3 = random.randint(1,2)
    if n3 == 1 :
        op = '+'
    else :
        op = '-'
    print(n1, op , n2, '=', end= ' ')
    ans = int(input('답은 ? '))
    if op == '+' :
        if ans == n1+n2 :
            print('정답~@!')
            count += 1
        else :
            print('틀림~!@')
    else :
        if ans == n1 - n2 :
            print('정답~!@')
            count += 1
    i+=1

if count > 3 :
    print('굳')




#24 중첩 선택 구조 
gpa = float(input('학점 평균 : '))
hours = int(input('봉사 평균 : '))
if gpa > 3.0 :
    if hours > 10 :
        print('장학금을 탈 수 있음')
    else :
        print('봉사시간 부족')
else :
    print('학점이 낮음')



#25 논리 연산자 
age = int(input('나이 입력 : '))
height = float(input('키 입력 : '))
if age > 7 and height > 145.0 :
    print('놀이기구 탈 수 있음')
else :
    print('놀이기구 탈 수 없음')
    


#26 팩토리얼 계산 코드 
fac = 1
i = 1

while True :
    num = int(input('양의 정수 입력(0 to quit) : '))
    if num == 0 :
        print('종료')
        break
    while i <= num :
        fac *= i
        i += 1
    print('%d! = %d' % (num,fac))
    fac = 1
    i = 1 



#27 최대공약수 구하는 법
def GCD(x,y) :
    while y != 0 :
        tmp = x
        x = y
        y = tmp % y
    return x

a = int(input('양의 정수 입력 : '))
b = int(input('양의 정수 입력 : '))
c = GCD(a,b)
print(c)



#28 
sum = 0

for x in range (1,11) :
    sum += x

print(sum)

#or 만약 

sum = 0 
for x in range (1, 11 ,2) : # 시작값:1, 증가값:2, 끝값:10 
	sum += x 

print(sum) 

#or 이렇게 변형 가능 
num = int(input('어디까지 계산할까요 '))
sum = 0
for x in range(1,num+1) :
    sum += x

print('1부터', num, '까지의 합은 ', sum)



#29 팩토리얼 계산
num = int(input('어디까지 계산할까요 '))
fac = 1
for x in range(1, num+1) :
    fac *= x
print(fac)



#30 3 6 9 게임  
for i in range (1, 100) :
    if i % 3 == 0 :
        print('짝', end = ' ')
    else :
        print(i, end = ' ')



#31 섭씨 -> 화씨 온도 변환 
for f in range ( 0 , 100 + 1 , 10) :
    print('%d -> %.2f' % (f,(f-32)*5/9))



#32 복권 추첨  
import random

for i in range (6) :
    print (random.randint(1,45) , end = ' ')

#or 중복된 숫자 없는 복권을 만들고 싶다면 

import random

lotto = []
count = 0
while True :
    num = random.randint(1,45)
    if num not in lotto :
        lotto.append(num)
        count += 1
    if count == 6 :
        break

print(lotto)
    
#or 복권을 여러장 사고 싶다면 

import random

piece = int(input('로또 몇장 살거임? '))

for x in range(piece) :
    lotto = []
    count = 0
    while True :
        num = random.randint(1,45)
        if num not in lotto :
            lotto.append(num)
            count += 1
        if count == 6 : break
    print(lotto)
    lotto.clear()
    x += 1 



#33 리스트, 요소에 다가가는 법  
scores = []

for i in range (5) :
    scores.append(int(input('점수 입력 : ')))

print(scores) 
if 20 in scores :
    print('리스트에 20 존재 ')
else :
    print('20 존재하지 않음')
    
#and 

#@아이템에 없는 아이템을 삭제하려는 경우 에러가 뜹니다. 
#그러니까 삭제하고자 하는 아이템이 있는지 if 문으로 확인 해야 합니다 
if 50 in scores :
    scores.remove(50) #아이템 삭제
    print(scores)



#34 내장 함수 max, min, sort() 
scores = []
for x in range(5) :
    scores.append(int(input('점수 입력 : ')))

print(max(scores))
print(min(scores))
scores.sort()
print(scores)



#35 리스트를 이용한 예제 
sum = 0
j=0

for i in range(5) :  #[0,1,2,3,4]
    num = int(input("성적을 입력하시요: "))
    sum = sum + num
    if num >= 80 :
        j+=1

print("성적 평균은 %.1f 입니다." %(sum/5.0))
print("80점 이상 성적을 받은 학생은", j, "명입니다.")



#36 버블정렬 
data = [90,10,23,17,56,39]

def bubbleSort(alist) :
    for p in range (len(alist) - 1 ) :
        for i in range(len(alist) - 1 -p) :
            if alist [i] > alist [i+1] :
                temp = alist[i]
                alist[i] = alist [i+1]
                alist[i+1] = temp

bubbleSort(data)
print(data)



#37 이진탐색 


#38 class 
class Person :
    def __init__ (self, name, phoneNum, age) :
        self.name = name
        self.phoneNum = phoneNum
        self.age = age

p1 = Person ('나','01073308143','20') # 객체 생성 
print(p1.name,p1.phoneNum,p1.age)     # 객체 멤버에 접근 



#39 추가 문법
score = [88,95,70,100,99]
score [0] = 100 
score.append(100) 
print(score) 
## append 함수는 메모리를 추가해서 넣어주는 것, 메모리가 새롭게 추가되면서 할당됨 



#40 리스트를 슬라이싱 하는 법 
nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[2:5])
print(nums[1:7:2])

#and 

nums = [0,1,2,3,4,5,6,7,8,9] 
nums[6:8] = [90,91,92,93,94] # 이상황에서는 에러가 안떨어지고 확장이 됩니다 
print(nums)



#41 중첩 리스트 사용 방법  
lol = [[1,2,3],[4,5],[6,7,8,9]] #리스트안에 리스트가 n개 들어있는 이중 리스트 
print(lol[0])
print(lol[2][1]) # 이중리스트를 읽는 방법과 이중리스트를 만드는 방법 

#lol[1][2] = 100  #이거는 에러
lol[1].append(100) #리스트 끝에 새로운 메모리와 함께 100삽입 
print(lol)

#and 

lol = [[1,2,3],[4,5],[6,7,8]]

for sub in lol :
    for item in sub :
        print(item, end = ' ')
    print() # 이중 리스트 예쁘게 표현하기 



#42 리스트에 삽입 
nums = [1,2,3,4]
nums[2] = [90,91,92]   # 해당 인덱스에 삽입, [1,2,[90,91,92],4] 
nums[2:2] = [90,91,92] # 해당 인덱스에 삽입, [1,2,90,91,92,3,4
print(nums)



#43 .index(), .count(), max(), min(), ... 
score = [88,95,70,100,99,80,78,50]

n =score.index(100)
print('만점자는' + str(n+1) + '번째임')

n = score.count(100)
print('만점자는' + str(n) + '명임')

n = max(score) #global함수
print(n)

n = min(score) #global함수
print(n) 

if 100 in score : #어떤 요소가 리스트에 있는지 if 문으로.. 잇으면 true, 없으면false
    print('만점자가 있음 ... ')
else : 
    print('만점자가 없음 ...')



#44 리스트 관련 함수 
score = [88,95,70,100,99,80,78,50]

#score.sort()
print(score)
score.reverse()
print(score)
aaa = sorted(score) 
print (aaa)
print (score)



#45 튜플 
tu = '이윤희','졸고있음','이윤희 졸고있음'
x,y,z = tu # 왼쪽 변수에 하나하나 대응하여 저장됨
name = tu

print(name[0])
print(name[1])
print(name[2])
print(x)
print(y)
print(z)



#46 튜플과 format 사용법 
def test(tu) :
    n1 = max(tu)
    n2 = min(tu)
    return n1, n2 # 튜플형 (n1, n2) 반환

score = 99,44,77,88,100
num = test(score)        # 튜플형 반환, num = (n1, n2)
print(num[0], num[1])    # 튜플형의 인덱스 

num1, num2 = test(score) # n1, n2 를 num1, num2 에 각각 반환 
print(num1,num2)
print('최댓값 : %d, 최솟값 : %d' % (num1,num2))
print('최댓값 : {0}, 최솟값 : {1}'.format(num1,num2))
# 중괄호 안에 숫자를 넣으면 format 괄호 안에 숫자를 순서대로 출력 가능함 



#47 딕셔너리 자료형 