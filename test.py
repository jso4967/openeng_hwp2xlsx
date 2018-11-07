from tkinter import *
from tkinter.ttk import *


class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("HWPConverter")
        self.pack(fill=BOTH, expand=True)

        framemodechoice = Frame(self)
        lblModeChoice = Label(framemodechoice, text="Step 0. Select a mode for convert")
        lblModeChoice.pack(padx=10)

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()

        c1 = Checkbutton(root, text="", variable=CheckVar1)

        c2 = Checkbutton(root, text="HWP2XLSX", variable=CheckVar2)

        c1.pack()

        c2.pack()
        listbox.pack(padx=10)

        framemodechoice.pack(fill=X)



        # 변환할 파일 설정
        framelb1 = Frame(self)
        lblFileToConvert = Label(framelb1, text="Step 1. Select a file to convert from your Disk", width=100)
        lblFileToConvert.pack(padx=10)
        framelb1.pack(fill=X)

        framechoice1 = Frame(framelb1)
        entryFileToConvert = Entry(framechoice1)
        entryFileToConvert.pack(fill=X, side=LEFT, padx=10, expand=True)

        btnBrowse1 = Button(framechoice1, text="Browse")
        btnBrowse1.pack(fill=X, side=RIGHT, padx=10)
        framechoice1.pack(fill=X)

        # 저장 폴더 설정
        framelb2 = Frame(self)
        lblFolderToSave = Label(framelb2, text="Step 2. Select a directory to save", width=100)
        lblFolderToSave.pack(padx=10)
        framelb2.pack(fill=X, pady=30)

        framechoice2 = Frame(framelb2)
        entryFolderToSave = Entry(framechoice2)
        entryFolderToSave.pack(fill=X, side=LEFT, padx=10, expand=True)

        btnBrowse2 = Button(framechoice2, text="Browse")
        btnBrowse2.pack(fill=X, side=LEFT, padx=10)
        framechoice2.pack(fill=X)

        # 상태바
        frameprogressbar = Frame(self)
        progress_bar = Progressbar(frameprogressbar, orient='horizontal', mode='determinate')
        progress_bar.pack(fill=X)
        frameprogressbar.pack(fill=X, padx=10)

        # 변환
        framecontrol = Frame(self)
        btnConvert = Button(framecontrol, text="변환")
        btnConvert.pack(side=RIGHT, padx=10)
        btnCancel = Button(framecontrol, text="취소")
        btnCancel.pack(side=RIGHT, padx=10)
        framecontrol.pack(fill=X, pady=20)


def main():
    root = Tk()
    root.minsize(400, 250)
    app = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()