#-*-coding:utf-8
from pywinauto import application

app = application.Application(backend="uia").start(r"C:\Temp\HncTest\Hwp80\Hwp.exe")
print(app)
if app.top_window().window_text():
    print(app.top_window().window_text())
else:
    print("error")

dlg = app.window(title='Frame')
print(dlg.window_text())
dlg.print_control_identifiers()