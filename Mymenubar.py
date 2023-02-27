import pendant
from PyQt5 import QtWidgets
from MyToolbar import MainToolbar
def menubar(menubar,widget):
    pendant.Main.menubars = menubar
    pendant.Main.widget_kinds = widget
    pendant.Main.widget(pendant.Main,'Open','Save','Quit',kinds='action',name='파일',difname='file')
    pendant.Main.widget(pendant.Main,'Open','Save','Quit',kinds='action',name='수정',difname='edit')
    pendant.Main.widget(pendant.Main,'Open','Save','Quit',kinds='action',name='폼',difname='form')
    pendant.Main.widget(pendant.Main,'Open','Save','Quit',kinds='action',name='설정',difname='setting')
    pendant.Main.widget(pendant.Main,'Open','Save','Quit',kinds='action',name='윈도우',difname='window')
    pendant.Main.widget(pendant.Main,'Open','Save','Quit',kinds='action',name='Help')
def file_Open_def(self):
    MainToolbar.Load_def(self)
def file_Save_def():
    pass
def file_Quit_def():
    pass

def edit_Open_def():
    print('1')
def edit_Save_def():
    pass
def edit_Quit_def():
    pass

def form_Open_def():
    pass
def form_Save_def():
    pass
def form_Quit_def():
    pass

def setting_Open_def():
    pass
def setting_Save_def():
    pass
def setting_Quit_def():
    pass

def window_Open_def():
    pass
def window_Save_def():
    pass
def window_Quit_def():
    pass

def Help_Open_def():
    pass
def Help_Save_def():
    pass
def Help_Quit_def():
    pass

if __name__=='__main__':
    app =  pendant.QtWidgets.QApplication(pendant.sys.argv)
    main = pendant.Main()
    main.show()
    pendant.sys.exit(app.exec_())