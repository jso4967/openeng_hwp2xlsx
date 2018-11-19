from docx import Document
import classes
import re

# TODO : main 함수로 정의 해야 함
document = Document('''.\data\영치프로그램 예문.docx''')
lines = document.paragraphs
regex_problem_number = re.compile(r'^\d.')
regex_gender = re.compile("[WM]:")
current_gender = None
current_eng_sentence = ""
current_kor_sentence = ""
current_eng_phrase = []
current_kor_phrase = []
current_option_number = 0
current_problem_set = []
current_problem_number = 1

for line in lines:
    text = line.text

    # 첫 문자가 문제 번호인 경우
    if regex_problem_number.search(text):
        print("첫 문자가 문제 번호인 경우", text)
        current_gender = None
        current_eng_phrase = []
        current_kor_phrase = []
        current_problem_number = int(text.strip()[0]) - 1
        current_option_number = 0
        current_problem_set.append(classes.Problem(current_problem_number))  # 문제번호가 적힌 문장에서 항상 첫번째 글자는 숫자( = 문제번호) 여야 한다.

        continue

    # 첫 문자가 선지 번호인 경우
    option_number = 0xe291a0
    message = ""
    for i in range(30):  # 최대 33개 까지 밖에 안되는 듯
        # 헥스코드를 이용하여 선지번호인지 체크
        is_option_number = text.find(bytes.fromhex(str(hex(option_number)[2:])).decode('utf-8'))
        if is_option_number >= 0:
            message = "첫 문자가 선지 번호인 경우  " + text
            current_option_number = i
            break
        option_number += 1

    if message:
        print(message)
        textforsplit = ""
        # 성별 찾기
        # TODO : 성별 찾기 다시 해야 될듯, strip을 이용해서 띄어쓰기를 무시하는 방식으로 다시 짜자
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
        current_eng_sentence = textforsplit
        current_eng_phrase = textforsplit.split('/')

        #  각 구에 대하여 공백을 지운다.
        i = current_eng_phrase.__len__() - 1
        while i >= 0:
            current_eng_phrase[i] = current_eng_phrase[i].strip()
            i -= 1

        print(current_eng_phrase)
        continue

    # 첫 문자가 문제 구분자인 경우 혹은 문장에 문자가 없는 경우
    if text.find("===") >= 0 or (text == ''):
        print("첫 문자가 문제 구분자 이거나 아무 문자도 없을 때", text)
        continue

    # 첫 문자가 한글인 경우
    if len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text)):
        print("첫 문자가 한글인 경우", text)
        current_kor_sentence = text.strip()
        current_kor_phrase = current_kor_sentence.split('/')

        #  각 구에 대하여 공백을 지운다.
        i = current_kor_phrase.__len__() - 1
        while i >= 0:
            current_kor_phrase[i] = current_kor_phrase[i].strip()
            i -= 1

        print(current_kor_phrase)
        #  해당 문제에 문장 추가
        current_problem_set[current_problem_number].addsentence(current_eng_sentence, current_kor_sentence, current_gender)

        if current_eng_phrase.__len__() == current_kor_phrase.__len__():
            print("++++++++++++++++++++++++++동일++++++++++++++++++++++++++")
            #  해당 문장에 구 추가
            (current_problem_set[current_problem_number].getsentences())[current_option_number].addphrase(current_eng_phrase, current_kor_phrase, None)

        if current_problem_set[current_problem_number].getsentences():
            print("현재 문제번호 : " + str(current_problem_number) + " 현재 선지번호 : " + str(current_option_number))
            for entry in (current_problem_set[current_problem_number].getsentences())[current_option_number].getphrases():
                print(entry.getall())
        continue

    # 첫 문자가 영어인 경우
    # TODO :이전 선지 번호와 구를 합치는 작업을 해야함
    print(text.strip()[0], text)
    isAlphabet = ord(text.strip()[0])
    if (65 <= isAlphabet or isAlphabet <= 90) or (97 <= isAlphabet or isAlphabet <= 122):
        print("첫 문자가 영어인 경우")
        current_eng_sentence = text.strip()
        current_eng_phrase = current_eng_sentence.split('/')

        #  각 구에 대하여 공백을 지운다.
        i = current_eng_phrase.__len__() - 1
        while i >= 0:
            current_eng_phrase[i] = current_eng_phrase[i].strip()
            i -= 1

        print(current_eng_phrase)
        continue

    # 위에 해당하지 않는 경우
    # TODO : 규칙 정리해야 함
    print("예외 규칙에 맞지 않는 문자가 맨 처음 존재!", text)
    print("")

