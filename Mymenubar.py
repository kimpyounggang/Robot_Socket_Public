import pendant,os,numpy,pickle
from PyQt5 import QtWidgets
from MyToolbar import MainToolbar
def menubar(menubar,widget):
    pendant.Main.menubars = menubar
    pendant.Main.widget_kinds = widget
    pendant.Main.widget(pendant.Main,'Open','Save','Quit',kinds='action',name='파일',difname='file')
    pendant.Main.widget(pendant.Main,'Open','Save','Quit',kinds='action',name='수정',difname='edit')
    pendant.Main.widget(pendant.Main,'Pos','Save','Quit',kinds='action',name='연구소',difname='lab')
    pendant.Main.widget(pendant.Main,'Open','Reset',kinds='action',name='설정',difname='setting')
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

def lab_Pos_def():
    pendant.Main.robot_pos_x.setText('1000')
    pendant.Main.robot_pos_y.setText('1000')
    pendant.Main.robot_pos_z.setText('1000')
    
def lab_Save_def():
    x = pendant.Main.point_name_proc
    y = pendant.Main.point_list
    z = numpy.column_stack((x, y))
    options = pendant.QtWidgets.QFileDialog.Options()
    options |= pendant.QtWidgets.QFileDialog.DontUseNativeDialog  # native 대화상자 사용 안함
    file_path, _ = pendant.QtWidgets.QFileDialog.getSaveFileName(None, "Save file", "", "Data Files (*.data)", options=options)
    with open(f'{file_path}.data','wb') as f:
        pickle.dump(z,f)
    # print(file_path)
    # print(_)

def lab_Quit_def():
    pass

def setting_Open_def():
    os.system('System.ini')
def setting_Reset_def():
    reply = pendant.QtWidgets.QMessageBox.question(None, '경고!', '설정 초기화?', pendant.QtWidgets.QMessageBox.Yes | pendant.QtWidgets.QMessageBox.No, pendant.QtWidgets.QMessageBox.No)
    if reply == pendant.QtWidgets.QMessageBox.Yes:
        print('초기화')
    else:
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