import view
from tkinter import filedialog
import tkinter as tk
import model, model_core, os

class fileErrorEx(BaseException):pass
def button_pressed(self, targetToUpdate, value, mode, targetToUpdate2=None):
    print(value, "pressed")
    if value == "FileBrowse":
        fileName = filedialog.askopenfilename()

        # 중복 파일 존재 여부 확인
        dirname = fileName[:fileName.rfind('/')]
        print(dirname)
        filenames = os.listdir(dirname)
        for filename in filenames:
            test = fileName[fileName.rfind('/') + 1:fileName.find('.') + 1] + "docx"
            if filename == test:
                print("Error 입력파일 이름 중복 해당 이름의 docx 파일을 지우거나 새로운 이름으로 바꿔서 재시도 해주세요")
                print("===========================")
                targetToUpdate.delete("0", tk.END)
                raise fileErrorEx

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
            data_eng_kor, data_kor_eng = model_core.make_string(problem_set)
            print(data_eng_kor)
            print(data_kor_eng)

            if targetToUpdate2.get():
                model_core.make_final_file(data_eng_kor, data_kor_eng, path, targetToUpdate2.get())
            else:
                output_path = targetToUpdate.get()
                output_path = output_path[:output_path.rfind('/')]
                model_core.make_final_file(data_eng_kor, data_kor_eng, path, output_path)

        else:
            pass