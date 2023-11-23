'''
마우스를 움직여서 화면에 그림을 그리는 윈도우의 그림판과 비슷한
프로그램을 작성해보자. 캔버스 위젯 아래에 버튼 "빨강색"을 추가하고
이 버튼을 누르면 색상이 빨강색으로 변경되게 하자 
그림의 색상이 아닌 굵기도 바꿔보도록 해보세요
'''


from tkinter import *

mycolor="blue"
 
# 마우스가 지나갈 때마다 작은 원을 그림으로써 그림을 그릴 수 있게 한다
# x0,y0,x1,y1 네 개의 좌표안에 들어가는 최대의 원을 만들 수 있음
# 완벽한 그림판은 아니지만 유사하게 만들 수 있음
# event argument -> 마우스 위치를 얻기 위한 argument
def paint(event) : # event -> 마우스로 한 지점을 클릭했을 때 x,y좌표를 얻을 수 있음 
    x1, y1 = (event.x-1), (event.y-1) 
    x2, y2 = (event.x+1), (event.y+1)
    canvas.create_oval(x1,y1,x2,y2,fill=mycolor)

# Button에 대한 콜백 함수     
def changing_color( ) :
    global mycolor # 동일한 전역 변수를 사용하고 있음을 표현하기 위해 global 키워드를 사용
    mycolor = "red" 

root = Tk()

canvas = Canvas(root)
canvas.pack()
canvas.bind("<B1-Motion>", paint)
# B1-Motion -> 마우스의 왼쪽 버튼누르고 움직일 때 
# B2 -> 마우스의 가운데 버튼, B3 -> 마우스의 오른쪽 버튼
# -> 마우스 왼쪽 버튼을 누르고 움직이면 paint 콜백 함수를 실행하라  

button = Button(root, text="빨강색", command=changing_color)
button.pack()

mainloop()