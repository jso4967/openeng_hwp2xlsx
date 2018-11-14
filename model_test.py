import pyautogui
from datetime import datetime
import time

time.sleep(10)
path = 'TEST3'
print(1, datetime.now())
pos = pyautogui.locateOnScreen('BtnSaveAs.png')
print(pos)
print(pos)
posx = pos[0] + pos[2]/2
posy = pos[1] + pos[3]/2
pyautogui.click(posx, posy)
print( 2, datetime.now() )
pyautogui.typewrite(path)
pos = pyautogui.locateOnScreen('BtnSave.png')
print(pos)
posx = pos[0] + pos[2]/2
posy = pos[1] + pos[3]/2
pyautogui.click(posx, posy)
print( 3, datetime.now() )

# screenWidth, screenHeight = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position()
# pyautogui.moveTo(100, 150)
# pyautogui.click()
# pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
# pyautogui.doubleClick()
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
# pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# pyautogui.press('esc')
# pyautogui.keyDown('shift')
# pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')