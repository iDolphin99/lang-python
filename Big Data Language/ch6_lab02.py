'''
섭씨 -> 화씨, 화씨 -> 섭씨를 이벤트 처리하시오 
'''


from tkinter import *

# 콜백함수 추가 
def process1() : 
    temperature = float(e1.get())  # 읽어드리는 것 .get()
    mytemp=(temperature-32)*(5/9)  # 화씨를 섭씨로 바꾸는 계산식 
    e2.insert(0,str(mytemp))       # e2에 다시 문자열로 바꾸어서 출력 
    
def process2() :
    temperature = float(e2.get())
    mytemp = (temperature*(5/9)) + 32
    e1.insert(0,str(mytemp))

root = Tk()

# grid, 격자, 테이블, 행, 열 
l1 = Label(root, text = "화씨")
l2 = Label(root, text = "섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

# 한줄의 텍스트를 입력받는 필드 
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(root, text = "화씨->섭씨", command=process1)
b2 = Button(root, text = "섭씨->화씨", command=process2)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

root.mainloop()