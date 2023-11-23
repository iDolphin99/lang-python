import pyautogui
import pyperclip
import time 
from subprocess import Popen

# pyautogui 기본 설정
pyautogui.FAILSAFE = False       
pyautogui.PAUSE = 0.3 

# 어떤 환경에서도 동일하게 동작하기 위해 현재 동작중인 환경의 스크린 사이즈를 가져옴
width, height = pyautogui.size() 

# 알림창과 함께 자동화 시작 
pyautogui.alert('자동화 시작합니다...', timeout=1000)

# win + tab 단축키를 통해 열려있는 모든 창들 중 Chrome browser icon 이미지를 이용하여 접근 
pyautogui.hotkey('win', 'tab')
time.sleep(3)
coordinate = pyautogui.locateOnScreen('./Python Programming/chromeicon.png')
pyautogui.moveTo(coordinate, duration=1)
pyautogui.click()

# 활성화된 첫 번째 tab부터 접근 
pyautogui.hotkey('ctrl', '1')
pyautogui.moveTo(width/10, height/20, duration=1)

# 첫 번째 tab을 시작으로 마지막 tab의 링크까지 모두 복사하여 links list에 저장 
# 첫 번째 tab의 주소를 다시 만나면 반복문 탈출 
links = []
while True:    
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    link = pyperclip.paste() # pyperclip을 사용해야 ctrl+c를 통해 클립보드에 저장된 링크 값을 가져올 수 있음 
    if len(links) > 0 and link==links[0] : 
        break
    links.append(link)
    pyautogui.hotkey('ctrl', 'tab')
pyautogui.hotkey('altleft', 'f4') # 모두 복사 후 chrome 창 자동 종료

# tab창의 링크를 몇 개 저장하였는지 확인하기 위한 print문
print(len(links), "개의 tab 링크를 저장함")

# 사용자로부터 tab 링크들을 저장할 파일 이름을 입력 받기 
fname = pyautogui.prompt('저장할 파일 이름을 입력하세요')

# 메모장을 자동으로 킨 후 복사한 링크들을(links) 메모장에 입력 
Popen('notepad')
time.sleep(1.0)
pyautogui.typewrite('\n'.join(links), interval=0.01)

# 앞서 입력 받은 파일 이름으로 메모장 저장 후 종료 
pyautogui.hotkey('ctrl', 's')
pyautogui.typewrite(fname)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'f4')
