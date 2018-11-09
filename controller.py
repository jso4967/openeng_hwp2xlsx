import view
from tkinter import filedialog
import tkinter as tk
import model
# 라벨의 값을 마음대로 제어 할 수 있는 방안을 찾아야 함.

def button_pressed(self, targetToUpdate, value):
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
        model.main()