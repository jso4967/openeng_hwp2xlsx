from tkinter import *
from tkinter.ttk import *
import controller


class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("HWPConverter")
        self.pack(fill=BOTH, expand=True)

        #TODOLIST : 사진 처럼 다듬기
        photo = PhotoImage(file="left_logo.png")
        lbpng = Label(self, image=photo)
        lbpng.image = photo
        lbpng.pack()

        # 모드 선택
        framemodechoice = Frame(self)
        lblModeChoice = Label(framemodechoice, text="Step 0. Select a mode for convert")
        lblModeChoice.pack(padx=10, side=LEFT, pady=10)

        comboModeChoice = Combobox(framemodechoice, textvariable=str)
        comboModeChoice['values'] = ('KOR2ENG', 'HWP2XLSX')
        comboModeChoice.current(0)
        comboModeChoice.pack(padx=10, side=RIGHT, pady=10)

        framemodechoice.pack(fill=X, pady=(0,30))

        # 변환할 파일 설정
        framelb1 = Frame(self)
        lblFileToConvert = Label(framelb1, text="Step 1. Select a file to convert from your Disk", width=100)
        lblFileToConvert.pack(padx=10, side=LEFT)
        framelb1.pack(fill=X)

        framechoice1 = Frame(self)
        entryFileToConvert = Entry(framechoice1)
        entryFileToConvert.pack(fill=X, side=LEFT, padx=10, expand=True)

        btnBrowse1 = Button(framechoice1, text="Browse", command=lambda:controller.button_pressed(self, entryFileToConvert, "FileBrowse", comboModeChoice.get()))
        btnBrowse1.pack(fill=X, side=RIGHT, padx=10)
        framechoice1.pack(fill=X, pady=(0,30))

        # 저장 폴더 설정
        framelb2 = Frame(self)
        lblFolderToSave = Label(framelb2, text="Step 2. Select a directory to save", width=100)
        lblFolderToSave.pack(padx=10, side=LEFT)
        framelb2.pack(fill=X)

        framechoice2 = Frame(self)
        entryFolderToSave = Entry(framechoice2)
        entryFolderToSave.pack(fill=X, side=LEFT, padx=10, expand=True)

        btnBrowse2 = Button(framechoice2, text="Browse", command=lambda:controller.button_pressed(self, entryFolderToSave, "FolderBrowse", comboModeChoice.get()))
        btnBrowse2.pack(fill=X, side=RIGHT, padx=10)
        framechoice2.pack(fill=X, pady=(0, 30))

        # 상태바
        frameprogressbar = Frame(self)
        progress_bar = Progressbar(frameprogressbar, orient='horizontal', mode='determinate')
        progress_bar.pack(fill=X)
        frameprogressbar.pack(fill=X, padx=10)

        # 변환
        framecontrol = Frame(self)
        btnConvert = Button(framecontrol, text="Convert", command=lambda:controller.button_pressed(self, entryFileToConvert, "Convert", comboModeChoice.get(), entryFolderToSave))
        btnConvert.pack(side=RIGHT, padx=10)
        btnCancel = Button(framecontrol, text="Cancel", command=lambda:Frame.quit(self))
        btnCancel.pack(side=RIGHT, padx=10)
        framecontrol.pack(fill=X, pady=20)


def main():
    root = Tk()
    root.geometry("400x350+1200+100")
    root.resizable(False, True)
    app = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()