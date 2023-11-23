import pyautogui
import time

# 화면 전환 
pyautogui.keyDown('altleft')
pyautogui.press(['tab'])
time.sleep(1.0)
pyautogui.keyUp('altleft')

for i in range(10): # 저장할 페이지 수 설정 
    screen = pyautogui.screenshot()
    page = screen.crop((687, 130, 1310, 985)) # 좌, 상, 우, 하 좌표 수정 
    page.save(f'page{i:03d}.png')
    pyautogui.press(['right'])

