'''
메모장 만들기 
'''


from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

def open() : 
    file = askopenfile(parent=root, mode='r')
    if file != None :
        lines = file.read()
        text.insert('1.0', lines)
        file.close()
    
def save() : 
    file = asksaveasfile(parent=root, mode='w')
    if file != None : 
        
        lines = text.get('1.0', END+'-1.C')
        file.write(lines)
        file.close()

def exit() : 
    # ok 또는 cancle을 선택하도록 물어봄
    if askokcancel("Quit", "종료하시겠습니까?") : # title : Quit, message : 종료하시겠습니까? 
        root.destroy() # 확인,ok -> destroyD

def about() :
    labe = showinfo("About", "메모장 프로그램")
    

root = Tk()
text = Text(root, height=30, width=80)
text.pack()

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
menubar.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label = "열기", command=open)
filemenu.add_command(label = "저장하기", command=save)
filemenu.add_command(label = "종료",command=exit)

helpmenu = Menu(menubar)
menubar.add_cascade(label="도움말", menu=helpmenu)
helpmenu.add_command(labe="프로그램 정보",command=about)

mainloop()