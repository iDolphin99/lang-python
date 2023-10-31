import pyautogui
import time

pyautogui.locateOnScreen('./Python Programming/bear.jpg')

im = pyautogui.screenshot()
print(type(im))

im = pyautogui.screenshot('screenshot.png')
print(im.getpixel((100, 100)))

for i in range(10):
    fname = 'screen_{:04d}.png'.format(i)
    print(fname)
    # pyautogui.screenshot(fname)
    time.sleep(1)