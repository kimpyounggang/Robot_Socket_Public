import pendant,numpy
from PyQt5 import QtWidgets,QtCore
from Myglobal import cGlobal
from Mypath import init
from MyLog import cTime
from MyVisual import Visualize
import pyqtgraph.opengl as gl
import  socket

class MainToolbar():
    def __init__(self):
        pass

    def toolbar(self, rule,area):
        pendant.Main.rule_icon = rule
        pendant.Main.toolbarareas = area
        
        pendant.Main.add_toolbar(self,'Connect','Create','Load','AutoPoints', 'StepBack','Pause','Run','StepGo','RunWay' ,'WaySetting', 'CycleTime', 'SafetyZone', toolbarname='MenuProc',rule='undertext',area='top')
        
        pendant.Main.Right_listwidget = QtWidgets.QListWidget()
        pendant.Main.add_toolbar(self,pendant.Main.Right_listwidget,toolbarname='TeachingList',area='right')
        
        pendant.Main.LogBrowser = QtWidgets.QTextBrowser()
        pendant.Main.add_toolbar(self,pendant.Main.LogBrowser,toolbarname='Log',area='bottom')

    def Connect_def(self):
        cTime.Log_Write(self,Contents ='Host / Port Edit Init')
        
        if hasattr(pendant.Main,'Bool_Connect')==False:
            setattr(pendant.Main,'Bool_Connect',0)
            insert_host_port().exec_()
        else:
            if getattr(pendant.Main,'Bool_Connect')==0:
                insert_host_port().show()
            else:
                insert_host_port().exec_()
                setattr(pendant.Main,'Bool_Connect',1)
            
    
    def AutoPoints_def(self):
        pass
    def RunWay_def(self):
        obj = pendant.Main.canvas.axes
        if hasattr(pendant.Main, 'point_list'):
            point = pendant.Main.point_list
            for i in range(len(pendant.Main.point_list)-1):    
                x = numpy.linspace(point[i][0], point[i+1][0],10)
                y = numpy.linspace(point[i][1], point[i+1][1],10)
                z = numpy.linspace(point[i][2], point[i+1][2],10)
                obj.plot(x,y,z)
                    # obj.plot3D(pendant.Main.point_list[][0])
            pendant.Main.canvas.draw()
        
    def WaySetting_def(self):
        MyRobot_pos = gl.GLScatterPlotItem(pos = numpy.array([[pendant.Main.x,pendant.Main.y,pendant.Main.z]]))
        pendant.Main.canvas.addItem(MyRobot_pos)  
        
    def Create_def(self):
        pass
    def Load_def(self):
        # pendant.Main.canvas.axes.cla()
        # pendant.Main.canvas.clear()
        pendant.Main.Right_listwidget.clear()
        # pendant.Main.canvas_grid(self)
        file = QtWidgets.QFileDialog.getOpenFileName()
        if file[0] == '':
            pass
        else: Visualize.create_obj(pendant.Main,file[0])

    def StepBack_def(self):
        print('1')
    def Pause_def(self):
        pass
    def Run_def(self):
        pass

    def StepGo_def(self):
        pass
    
    def CycleTime_def(self):
        pass
    
    def SafetyZone_def(self):
        pass

class insert_host_port(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupui()
        self.show()
    
    def __delattr__(self):
        setattr(pendant.Main,'Bool_Connect',0)
        
    def setupui(self):
        host,port = cGlobal.get_HostPort(self)
        label1 = QtWidgets.QLabel("HOST : ")
        label2 = QtWidgets.QLabel("PORT : ")
        self.edit1 = QtWidgets.QLineEdit()
        self.edit1.setText(str(host))
        self.edit2 = QtWidgets.QLineEdit()
        self.edit2.setText(str(port))
        layout = QtWidgets.QVBoxLayout()
        layout1 = QtWidgets.QHBoxLayout()
        layout2 = QtWidgets.QHBoxLayout()
        btn = QtWidgets.QPushButton('Enter')
        btn.clicked.connect(self.btn_def)
        layout1.addWidget(label1)
        layout1.addWidget(self.edit1)
        layout2.addWidget(label2)
        layout2.addWidget(self.edit2)
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addWidget(btn)
        self.setLayout(layout)
        # insert_host_port().exec_()
    
    def btn_def(self):
        host = self.edit1.text()
        port = self.edit2.text()
        cGlobal.Set_HostPort(self,host,port)
        self.close()
        setattr(pendant.Main,'Bool_Connect',1)
        

            
if __name__=='__main__':
    app =  pendant.QtWidgets.QApplication(pendant.sys.argv)
    main = pendant.Main()
    main.show()
    pendant.sys.exit(app.exec_())