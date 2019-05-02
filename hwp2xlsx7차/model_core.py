import pyautogui
from datetime import datetime
import time, ctypes

class RuleErrorEx(BaseException):pass

def errorMsg(text, additional_msg = None):
    msg = "\n\n=============================================================\n"
    msg += "예외 규칙에 맞지 않는 문자 형태! : " + text
    msg += "\n===========================================================\n\n" \
           "아래 사항들을 고려해보세요\n\n"
    # msg += "1. 선지번호가 등장하는 문장은 항상 맨 처음 선지번호, 띄어쓰기, 이후 문장 순으로 적혀있어야 한다.\n"
    msg += "1. 문장의 첫글자는 숫자, 원문자 혹은 알파벳, 한국어이어야 한다.(특수문자 X) 단, 한국어 문장은 상관없다.\n"
    # msg += "2. 영어 문장은 항상 첫 글자가 숫자 혹은 알파벳이어야한다. 한국어 문장은 상관없다.\n"
    msg += "2. '/'의 개수가 한글 영어 동일해야 한다.\n" \
           "3. 문제번호 및 선지번호가 1번부터 순서대로 오름차순인가\n"

    if additional_msg:
        msg = additional_msg

    return msg

def convert_hwp2docx(path):
    __path = path
    #  파일 세팅
    ctypes.windll.Shell32.ShellExecuteW(None, 'open', __path, None, None, 1)
    print(1, datetime.now())
    time.sleep(5)

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
    for i in range(20):
        pyautogui.hotkey('up')

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

    time.sleep(3)
    print("Convert Succeeded")

def delete_empty_space(phrases):
    '''
    :param phrases: phrase의 집합들
    ex) current_eng_phrasess, curren_kor_phrases와 같이

    :return: 각 집합 안에 존재하는 비어있는 공간을 지운다.
    ex) ['ㅁ', 'ㅠ', '', 'ㅊ'] -> ['ㅁ','ㅠ','ㅊ']
    '''

    i = phrases.__len__() - 1
    while i >= 0:
        phrases[i] = phrases[i].strip()
        if phrases[i] == "":
            del phrases[i]
        i -= 1

    return phrases

def does_start_with_circled_number(text, current_option_number):
    '''

    :param text: 첫 글자가 선지번호인지 아닌지 체크하고자 하는 문장
    :param current_option_number: 선지번호의 연속성을 이용하여 값 검증을 하기 위한 값
    :return: None인 경우 선지번호로 시작하지 않음을 뜻함 /
            (message, i)인 경우, 선지번호로 시작함을 뜻함 : 디버깅을 위한 message와,
                current_option_number 업데이트를 위한 i 값 반환
    '''
    option_number = 0xe291a0
    message = ""

    for i in range(50):

        # 헥스코드를 이용하여 선지번호인지 체크

        # 20인 부분에서 21인 부분으로 점프 (1부터 20까지는 연속적인데, 20과 21의 유니코드 값이 불연속적이다.)
        # 관련 링크 : https://unicode-table.com/en/2473/
        if option_number == 14848436:
            option_number += 63453

        # 위와 동일한 이유 : https://unicode-table.com/en/32B1/
        if option_number == 14911904:
            option_number += 273

        is_option_number = text[:2].find(bytes.fromhex(str(hex(option_number)[2:])).decode('utf-8'))
        if is_option_number >= 0 and (current_option_number == 0 or current_option_number + 1 == i):
            message = "첫 문자가 선지 번호인 경우 : " + text
            return (message, i)

        # 올바른 선지번호가 아닌 경우 : 문장에 선지번호는 존재하나, 이전 번호와 순서가 맞지 않음
        elif is_option_number >= 0 and current_option_number + 1 != i:
            return "올바른 선지번호가 아닌 경우 : 문장에 선지번호는 존재하나, 이전 번호와 순서가 맞지 않음", current_option_number

        option_number += 1
    return "선지번호가 존재하지 않는 경우", current_option_number

def find_gender(text):
    text = text.strip()
    sentence_text = ""
    # 성별 찾기
    if text[text.find("M"):].find(":") != -1:
        current_gender = "M"
        sentence_text = text[text.find(":") + 1:]

    elif text[text.find("W"):].find(":") != -1:
        current_gender = "W"
        sentence_text = text[text.find(":") + 1:]

    else:
        # if text[1:].find(" ") != 0:
        #     print(errorMsg( text +" \n 1번 규칙 위반 가능성이 높습니다."))
        #     raise RuleErrorEx
        sentence_text = text[1:].strip()
        current_gender = None

    sentence_text = sentence_text.strip()

    return sentence_text, current_gender

def is_alphabet(text):
    isAlphabet = ord(text.strip()[0])
    if (65 <= isAlphabet and isAlphabet <= 90) or (97 <= isAlphabet and isAlphabet <= 122) :  # or text[0].isdigit()
        return True
    else:
        return False







