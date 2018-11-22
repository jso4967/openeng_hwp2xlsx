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
            model_core.make_final_file(data, path)


        else:
            pass