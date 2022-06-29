class Phonebook : # 클래스 정의 
    def __init__(self, _name, _phoneNum, _age):
        self.name = _name
        self.phoneNum = _phoneNum
        self.age = _age

def Add() : # 추가 
    name = input("이름 입력: ")
    phonNum = input("폰번호 입력: ")
    age = input("나이 입력: ")
    pb = Phonebook(name, phonNum, age)
    nList.append(pb)

def Search() : # 탐색 
    Sname = input("탐색할 이름 입력: ")
    for m in nList : 
        if m.name == Sname : 
            print(m.phoneNum)

def Delete() : # 삭제 
    Dname = input("삭제할 이름 입력: ")
    for  m in nList : 
        if m.name == Dname : 
            nList.remove(m)



nList = []
print("전화번호 관리 프로그램 시작...")
while True : 
    print("1: 전화번호 추가, 2: 탐색, 3: 삭제, 4:종료")
    menu = int(input())
    if menu == 1 :
        Add() 
    elif menu == 2 :
        Search()  
    elif menu == 3 : 
        Delete() 
    elif menu == 4 : 
        break 
    print("============================")
    print("전체 데이터 출력")
    for i in range(len(nList)) :
        print(nList[i].name, nList[i].phoneNum, nList[i].age) 
    print("============================")
print("프로그램 종료...")