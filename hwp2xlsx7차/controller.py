from tkinter import filedialog
import tkinter as tk
import model_hwp2docx, model_core, model_hwp2xlsx, os

class fileErrorEx(BaseException):pass

def convert_button_pressed(self, input_filepath, mode, folderpath=None):
    '''
    :param self:
    :param filepath: 변환할 파일의 경로
    :param mode: 변환 후 처리는 어떻게 할건지에 관한 모드
    :param folderpath: 변환된 파일의 저장할 경로
    :param filepath2: hwp2xlsx 모드에서 사용 할 docx파일 경로
    :return: 출력 값은 없으나, 파일로 저장한다.
    '''

    filepath_for_convert = input_filepath.get()

    if filepath_for_convert.find("hwp")>=0:
        model_core.convert_hwp2docx(filepath_for_convert)

    if mode == '영치2DOCX':

        '''
        영치2DOCX
        입력 받은 한글 파일을 이용하여 한영, 영한 치환된 파일로 만들어 배포하는 기능
        입력 받은 한글 파일은 영치프로그램 버전이며, 영한, 한영 치환된 파일은 docx버전으로 배포한다.
        '''

        # 파일에서 데이터 추출
        filepath = filepath_for_convert[:filepath_for_convert.find(".") + 1] + "docx"
        problem_set = model_hwp2docx.extract_phrase_set(filepath)

        # 파일에 데이터 입력
        processed_filedata = model_hwp2docx.construct_phrase_data(problem_set)
        print(processed_filedata[0])  # 영한치환 문장 출력
        print(processed_filedata[1])  # 한영치환 문장 출력

        # 파일 형식으로 저장
        if folderpath.get():  # 저장 경로가 존재하는 경우
            model_hwp2docx.save_phrase_file(processed_filedata, filepath, folderpath.get())

        else:  # 저장 경로가 존재하지 않는 경우
            output_path = folderpath.get()
            output_path = output_path[:output_path.rfind('/')]
            model_hwp2docx.save_phrase_file(processed_filedata, filepath, output_path)

        print("!!!!!DONE!!!!!")

    elif mode == '문장2XLSX':
        '''
           HWP2XLSX

           입력받은 영치프로그램형식의 한글 파일을 이용하여 엑셀 파일로 변환하여 저장하는 기능
        '''
        print("!문장2XLSX!")

        # 파일에서 데이터 추출
        filepath = filepath_for_convert[:filepath_for_convert.find(".") + 1] + "docx"
        problem_set_for_sentence = model_hwp2xlsx.extract_problem_set(filepath)

        filename = filepath_for_convert[filepath_for_convert.rfind("/"):]

        # 파일에 데이터 입력 및 저장
        if folderpath.get():
            model_hwp2xlsx.save_as_sentence_xlsx(problem_set_for_sentence, folderpath.get() + filename)
        else:  # 저장 경로가 존재하지 않는 경우
            output_path = folderpath.get()
            output_path = output_path[:output_path.rfind('/')]
            model_hwp2xlsx.save_as_sentence_xlsx(problem_set_for_sentence, output_path + filename)

        print("!!!!!DONE!!!!!")

    elif mode == '영치2XLSX':

        print("START!")

        ## 치환 파일에서 problem_set 추출
        filepath = filepath_for_convert
        filepath = filepath[:filepath.find(".") + 1] + "docx"
        problem_set_for_phrase = model_hwp2docx.extract_phrase_set(filepath)

        filename = filepath[filepath.rfind("/"):]

        # 파일에 데이터 입력 및 저장
        if folderpath.get():
            model_hwp2xlsx.save_as_phrase_xlsx(problem_set_for_phrase, folderpath.get() + filename)
        else:  # 저장 경로가 존재하지 않는 경우
            output_path = folderpath.get()
            output_path = output_path[:output_path.rfind('/')]
            model_hwp2xlsx.save_as_phrase_xlsx(problem_set_for_phrase, output_path + filename)

        print("!!!!!DONE!!!!!")


def browse_button_pressed(self, targetToUpdate, value):
    '''
    convert 이외의 버튼을 눌렀을 때 처리하는 함수
    :param self:
    :param targetToUpdate: 버튼을 통해 바뀐 값을 업데이트 할 대상
    :param value: 어떤 버튼인지에 관한 값
    :return: 출력 값은 없다.
    '''
    print(value, "pressed")
    if value == "FileBrowse":
        input_fileName = filedialog.askopenfilename()
        if input_fileName.find("docx") < 0:

            # 중복 파일 존재 여부 확인
            dirname = input_fileName[:input_fileName.rfind('/')]
            print(dirname)
            test = input_fileName[input_fileName.rfind('/') + 1:input_fileName.rfind('.')+1] + 'docx'
            filenames = os.listdir(dirname)

            for filename in filenames:
                if filename == test  or filename.find(test + "_Phrase_result")>=0 or filename.find(test + "_Sentence_result")>=0:
                    print("Error 입력파일 이름 중복 : " + filename + " 이 파일을 변경하세요")
                    print("===========================")
                    targetToUpdate.delete("0", tk.END)
                    raise fileErrorEx

        # 파일 경로 업데이트
        targetToUpdate.delete("0", tk.END)  # 이미 entry에 있는 경로 삭제
        targetToUpdate.insert("end", input_fileName)

    elif value == "FolderBrowse":
        dirName = filedialog.askdirectory()
        targetToUpdate.delete("0", tk.END)
        targetToUpdate.insert("end", dirName)

