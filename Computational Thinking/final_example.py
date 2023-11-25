'''
기말고사 방식 _ def 함수 안의 부분 작성 
'''
import random


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


list1 = [3, 5, 7, 9, 11]
list2 = []


def test1(L):  # 리스트의 평균 반환
    return sum(L) / len(L)


def test2():  # 8자리 알파벳과 숫자 조합의 암호 생성 및 반환
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    password = password.join(random.sample(alphabet, 8))
    return password


def test3(s):  # 회문 판단 프로그램... 회문이면 True 반환
    return s[::-1] == s


def test4_insert_student_info(name, age):
    s = Student(name, age)
    list2.append(s)


def test5_search_student_info(s):
    for i in list2:
        if i.name == s:
            print("[" + i.name + ", " + str(i.age) + "]")
            return
    print("리스트에 없음...")


# 프로그램 시작...
print(test1(list1))
print(test2())
msg = input("문자열 입력: ")
if test3(msg):
    print("회문...")
else:
    print("회문이 아님...")
test4_insert_student_info("유관순", 16)
test4_insert_student_info("이완용", 55)
test4_insert_student_info("이순신", 37)
test5_search_student_info("유관순")



'''
다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상의 점수들의 총합을 구하시오.

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]


while문을 이용하여 아래와 같이 별(*)을 표시하는 프로그램을 작성해 보자.

*
**
***
****   
or
*******
 *****
  ***
   *
'''



'''
피보나치 문제 
'''

def fib(n):
    if n == 0 : return 0 
    if n == 1 : return 1  
    return fib(n-2) + fib(n-1)  

for i in range(10):
    print(fib(i))
