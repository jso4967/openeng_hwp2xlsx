import pyautogui
from datetime import datetime
import time
import ctypes


hwp = r'C:\Users\IS119\Documents\GitHub_JeonSeOk\openeng_hwp2xlsx\data\영치프로그램 예문.hwp'
def setfilepath(path):
    hwp = path

def convertfile():
    #  파일 세팅
    ctypes.windll.Shell32.ShellExecuteW(None, 'open', hwp, None, None, 1)
    print(1, datetime.now())
    time.sleep(3)

    # 다른 이름으로 파일 저장하기 전 단계
    pyautogui.hotkey('alt', 'f')
    print(2, datetime.now())

    # 다른 이름으로 파일 저장하기
    pyautogui.hotkey('alt', 'v')
    print(3, datetime.now())

    # 파일 형식 지정하기
    pyautogui.hotkey('alt', 't')
    print(4, datetime.now())

    # 파일 형식 지정하기2
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    print(5, datetime.now())

    # 파일 저장하기
    pyautogui.hotkey('alt', 'd')
    print(6, datetime.now())

    # 파일 저장 확인
    pyautogui.hotkey('c')

    # 열었던 프로그램 종료
    pyautogui.hotkey('alt', 'f4')

    print("Convert Succeeded")


