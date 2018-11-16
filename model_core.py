from docx import Document
import classes
import re

document = Document('''.\data\[docx]영치프로그램 예문.docx''')
lines = document.paragraphs
regex_problem_number = re.compile("\d.")
regex_gender = re.compile("[WM]:")
current_gender = None
current_eng_phrase = []
current_kor_phrase = []
current_option_number = 1
current_problem = classes.Problem(None)

for line in lines:
    text = line.text

    # 첫 문자가 문제 번호인 경우
    if regex_problem_number.search(text):
        print("첫 문자가 문제 번호인 경우", text)
        current_gender = None
        current_eng_phrase = []
        current_kor_phrase = []
        current_problem = classes.Problem(text[0])  # 문제번호가 적힌 문장에서 항상 첫번째 글자는 숫자( = 문제번호) 여야 한다.
        continue

    # 첫 문자가 선지 번호인 경우
    option_number = 0xe291a0
    message = ""
    for i in range(30):
        # 헥스코드를 이용하여 선지번호인지 체크
        is_option_number = text.find(bytes.fromhex(str(hex(option_number)[2:])).decode('utf-8'))
        if is_option_number >= 0:
            message = "첫 문자가 선지 번호인 경우  " + text
            current_option_number = i + 1
            break
        option_number += 1

    if message:
        print(message)
        textforsplit = ""
        # 성별 찾기
        isgender = regex_gender.search(text)
        if isgender:
            print("성별이 존재하는 경우", text)

            if text.find("M:") >= 0:
                current_gender = "M"
                textforsplit = text[text.find("M:") + 3:]   # 성별 3칸 이후부터 문장이 시작되어야 한다.
                print(textforsplit)
            else:
                current_gender = "W"
                textforsplit = text[text.find("W:") + 3:]
                print(textforsplit)

        if textforsplit == "":
            textforsplit = text[2:]  # 선지번호가 등장하는 문장은 항상 맨 처음 선지번호, 띄어쓰기, 이후 문장 순으로 적혀있어야 한다.
        current_eng_phrase = textforsplit.split('/')

        #  각 구에 대하여 공백을 지운다.
        i = current_eng_phrase.__len__() - 1
        while i >= 0:
            current_eng_phrase[i] = current_eng_phrase[i].strip()
            i -= 1

        print(current_eng_phrase)
        continue



    # 첫 문자가 한글이나 영어인 경우
    # if len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text)):
    #     print("첫 문자가 한글인 경우", text)
    #     continue

    # 첫 문자가 문제 구분자인 경우 혹은 문장에 문자가 없는 경우
    if text.find("===") >= 0 or (text == ''):
        print("첫 문자가 문제 구분자 이거나 아무 문자도 없을 때", text)
        continue

    # 위에 해당하지 않는 경우
    print("첫 문자가 한글이나 영어인 경우", text)

