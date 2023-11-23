# 키보드 마우스 자동화 
import pyautogui

# 코드 오류로 인한 마우스, 키보드 제어 불가를 대비하여 안전장치 설정 -> x=0, y=0으로 이동할 경우 프로그램 종료 -> 사용하지 않을 경우 False
pyautogui.FAILSAFE = False 
# 명령 사이 간격을 0.1초로 설정  
pyautogui.PAUSE = 0.1 

print(pyautogui.size()) # 1920, 1080
pyautogui.moveTo(500, 500, duration=1) # (500, 500) 위치로 1초 동안 이동
pyautogui.moveTo(-100, -100)

pyautogui.moveTo(400, 500, duration=1)
pyautogui.click() # When no arguments are passed, the primary mouse button is clicked at the mouse cursor's current location
pyautogui.click(400, 500)

pyautogui.moveTo(400, 500, duration=1)
pyautogui.dragTo(600, 900, duration=1)

# 계산기 켜놓고 자동으로 클릭하게 만들기 
buttons = {'1': (40, 320), '2': (90, 320), '3': (140, 230)}
for c in '123':
    x, y = buttons[c]
    pyautogui.click(x, y, duration=1)