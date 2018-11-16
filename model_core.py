from docx import Document
import classes
import re

document = Document('''.\data\[docx]영치프로그램 예문.docx''')
lines = document.paragraphs
regex_problem_number = re.compile("\d.")
regex_gender = re.compile("[WM]:")

for line in lines:
    text = line.text

    # 첫 문자가 문제 번호인 경우
    if regex_problem_number.search(text):
        print("첫 문자가 문제 번호인 경우", text)
        continue

    # 첫 문자가 선지 번호인 경우
    option_number = 0xe291a0
    message = ""
    for i in range(30):
        is_option_number = text.find(bytes.fromhex(str(hex(option_number)[2:])).decode('utf-8'))
        if is_option_number >= 0:
            message = "첫 문자가 선지 번호인 경우  " + text
            break
        option_number += 1
    if message:
        print(message)
        continue

    # 첫 문자가 성별인 경우
    if regex_gender.search(text):
        print("첫 문자가 성별인 경우", text)
        continue

    # # 첫 문자가 한글이나 영어인 경우
    # if len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text)):
    #     print("첫 문자가 한글인 경우", text)
    #     continue

    # 첫 문자가 문제 구분자인 경우 혹은 문장에 문자가 없는 경우
    test = text.find("===")
    test2 = (text == '')
    if test >= 0 or test2 :
        print("첫 문자가 문제 구분자 이거나 아무 문자도 없을 때", text)
        continue

    # 위에 해당하지 않는 경우
    print("첫 문자가 한글이나 영어인 경우", text)

