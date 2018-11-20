import view
from tkinter import filedialog
import tkinter as tk
import model, model_core
# 라벨의 값을 마음대로 제어 할 수 있는 방안을 찾아야 함.

def button_pressed(self, targetToUpdate, value, mode):
    print(value, "pressed")
    if value == "FileBrowse":
        fileName = filedialog.askopenfilename()
        targetToUpdate.delete("0", tk.END)
        targetToUpdate.insert("end", fileName)

    elif value == "FolderBrowse":
        dirName = filedialog.askdirectory()
        targetToUpdate.delete("0", tk.END)
        targetToUpdate.insert("end", dirName)

    elif value == "Convert":
# TODO : 소스 코드 라인 줄이기 => 다른 파일로?

        if mode == "KOR2ENG":

            # 파일 형식 변환
            path = targetToUpdate.get()
            model.convertfile(path)

            # 파일에서 데이터 추출
            path = path[:path.find(".")+1] + "docx"
            problem_set = model_core.convert_for_kor2eng(path)

            # 파일에 데이터 입력
            data = model_core.make_string(problem_set)
            print(data)

            # data = ""
            # problem_number = 1
            # for problem in problem_set:
            #
            #     # 문제 번호 출력
            #     data += "\n" + str(problem_number) + "\n"
            #
            #     print()
            #     print(problem_number)
            #     print()
            #     problem_number += 1
            #     option_number = 0xe291a0
            #
            #     print("==========영한치환==========")
            #
            #     for sentence in problem.getsentences():
            #
            #         # 문항 번호 출력
            #         data += bytes.fromhex(str(hex(option_number)[2:])).decode('utf-8') + "\n"
            #
            #         print(bytes.fromhex(str(hex(option_number)[2:])).decode('utf-8'))
            #         option_number += 1
            #
            #
            #         phrase = sentence.getphrases()[0]
            #         eng_phrase = phrase.get_eng_phrase()
            #         kor_phrase = phrase.get_kor_phrase()
            #         if len(eng_phrase) == len(kor_phrase):
            #             index = len(eng_phrase)
            #             flag = 1
            #             substituted_sentence = ""
            #
            #             for index in range(index):
            #                 if eng_phrase[index] == "":
            #                     continue
            #                 if flag == 1:
            #                     substituted_sentence += (eng_phrase[index] + " ")
            #                     flag = 0
            #                 else:
            #                     substituted_sentence += (kor_phrase[index] + " ")
            #                     flag = 1
            #
            #             data += substituted_sentence + "\n"
            #             print(substituted_sentence)
            #     option_number = 0xe291a0
            #
            #
            #     print("==========한영치환==========")
            #
            #     for sentence in problem.getsentences():
            #
            #         # 문항 번호 출력
            #
            #         data = bytes.fromhex(str(hex(option_number)[2:])).decode('utf-8') + "\n"
            #         print(bytes.fromhex(str(hex(option_number)[2:])).decode('utf-8'))
            #         option_number += 1
            #
            #         phrase = sentence.getphrases()[0]
            #         eng_phrase = phrase.get_eng_phrase()
            #         kor_phrase = phrase.get_kor_phrase()
            #         if len(eng_phrase) == len(kor_phrase):
            #             index = len(eng_phrase)
            #             flag = 1
            #             substituted_sentence = ""
            #
            #             for index in range(index):
            #                 if flag == 1:
            #                     substituted_sentence += (kor_phrase[index] + " ")
            #                     flag = 0
            #                 else:
            #                     substituted_sentence += (eng_phrase[index] + " ")
            #                     flag = 1
            #             data += substituted_sentence + "\n"
            #             print(substituted_sentence)
            #     option_number = 0xe291a0
        else:
            pass