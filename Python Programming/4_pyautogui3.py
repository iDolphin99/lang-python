import pyautogui
from subprocess import Popen
import time     

Popen('calc')   # 계산기 실행
time.sleep(1.0) # 계산기 실행 동안 잠시 대기 
pyautogui.typewrite('123+456=', interval=0.1) # 0.1초 간격으로 '123+456' 입력 

Popen('notepad')
time.sleep(1.0)
pyautogui.press(['hangul']) # 한글 모드로 전환 
pyautogui.typewrite('tpwhdeodhkdvkdlxld', interval=0.1) # 한글 자판 입력하듯이 입력 

pyautogui.alert('확인 창을 보여줍니다')
pyautogui.confirm('확인과 취소 버튼이 있는 창을 보여줍니다')
pyautogui.prompt('사용자 입력을 받을 수 있습니다')