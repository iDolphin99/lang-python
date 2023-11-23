'''
스톱워치 만들기 
레이블을 사용하여 간단한 스톱워치를 작성하여 보자.
시작 버튼을 누르면 시작되고 중지 버튼을 누르면 스톱워치가 중지된다. 
'''

 
from tkinter import *
# Import tkinter as tk

def startTimer() : 
    if(running) : 
        global timer
        timer += 1 
        timeText.configure(text=str(timer))
    root.after(10, startTimer)
    # after() : 주기적으로 특정한 함수를 호출, 인자는 ms단위 (10dlaus 0.01초 지연)
    
def start() :
    global running 
    running = True

def stop() :
    global running 
    running = False

running = False
timer = 0
root = Tk()

timeText = Label(root, text="0", font=("Helvetica",80))
timeText.pack()

startButton = Button(root, text="시작", bg="yellow", command=start)
startButton.pack(fill=BOTH) # fill = BOTH, 양 옆에 넓게 채우다
stopButton = Button(root, text="중지", bg="yellow", command=stop)
stopButton.pack(fill=BOTH)

# 함수를 호출하면 0.01 초마다 호출됨, 중지 버튼을 누르면 +=1 은 적용되지 않음
startTimer()
mainloop()