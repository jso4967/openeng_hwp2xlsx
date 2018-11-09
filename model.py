#-*-coding: utf-8 -*-
from pywinauto import application

def getWindow(app, windowText):
    ws = app.windows()
    for w in ws:
        if w.WindowText() == windowText:
            return w
        return None

app = application.Application().start('''C:\Temp\HncTest\Hwp80\Hwp.exe''')
app.connect(path="C:\Temp\HncTest\Hwp80\Hwp.exe")
ws = app.windows()
for w in ws:

memo = getWindow(app, u"빈 문서 1 - 한컴오피스 한글 ")
if memo:
    print("test succeeded")
else:
    print("test Failed")
