import pendant, socket, MyLeftwidget ,numpy
from PyQt5 import QtWidgets,QtCore
from Myglobal import cGlobal
from Mypath import init
from MyLog import cTime
from MyVisual import Visualize

class MainToolbar():
    def __init__(self):
        pass

    def toolbar(self, rule,area):
        pendant.Main.rule_icon = rule
        pendant.Main.toolbarareas = area
        
        pendant.Main.add_toolbar(self,'Connect','Create','Load','AutoPoints', 'StepBack','Pause','Run','StepGo','RunWay' ,'WaySetting', 'CycleTime',toolbarname='MenuProc',rule='undertext',area='top')
        
        pendant.Main.Right_listwidget = QtWidgets.QListWidget()
        pendant.Main.add_toolbar(self,pendant.Main.Right_listwidget,toolbarname='TeachingList',area='right')
        
        pendant.Main.LogBrowser = QtWidgets.QTextBrowser()
        pendant.Main.add_toolbar(self,pendant.Main.LogBrowser,toolbarname='Log',area='bottom')

    def Connect_def(self):
        cTime(Mode='Log_Write',
                          Sector='MyToolbar.OtherToolbar.Connect_def',
                          Contents ='Host / Port Edit Init',
                          SavePath=init())
        if insert_host_port().exec_():
            pass
        else: pass
    
    def AutoPoints_def(self):
        pass
    def RunWay_def(self):
        obj = pendant.Main.canvas.axes
        point = pendant.Main.point_list
        for i in range(len(pendant.Main.point_list)-1):    
            x = numpy.linspace(point[i][0], point[i+1][0],10)
            y = numpy.linspace(point[i][1], point[i+1][1],10)
            z = numpy.linspace(point[i][2], point[i+1][2],10)
            obj.plot(x,y,z)
                # obj.plot3D(pendant.Main.point_list[][0])
        pendant.Main.canvas.draw()
        
    def WaySetting_def(self):
        pass    
        
    def Create_def(self):
        pass
    def Load_def(self):
        pendant.Main.canvas.axes.cla()
        pendant.Main.canvas.draw()
        pendant.Main.Right_listwidget.clear()
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

class insert_host_port(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupui()
        
        self.show()
        
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
    
    def btn_def(self):
        host = self.edit1.text()
        port = self.edit2.text()
        cGlobal.Set_HostPort(self,host,port)
        self.close()
        
class Worker(QtCore.QThread):
    # WatitThread = QtCore.pyqtSignal(bool)
    # progress = QtCore.pyqtSignal(int)
    def __init__(self):
        super().__init__()
        cTime(Mode='Log_Write',
                              Sector='MyToolbar.Worker.__init__',
                              Contents ='Running True',
                              SavePath=init())
        pendant.Main.running = True
        # self.bools = False
    def run(self):
        temp = 0
        if temp == 0:
            pendant.Main.robot_connect_status(pendant.Main,False,True)
        while pendant.Main.running:
            QtCore.QThread.sleep(1)
            temp +=1
            try:
                if self.socket_check():
                    cTime(Mode='Log_Write',
                          Sector='MyToolbar.Worker.socket_try',
                          Contents ='Socket Still Connect',
                          SavePath=init())
                    pendant.Main.robot_connect_status(pendant.Main,True,None)
                    pendant.Main.pause(self)
                    MyLeftwidget.left.socket_recv(self)
                    # self.bools = True
                    # self.WatitThread.emit(self.bools)
                else:
                    cTime(Mode='Log_Write',
                          Sector='MyToolbar.Worker.socket_try',
                          Contents ='Socket Coonnect Failed',
                          SavePath=init())
                    if self.socket_try():
                        cTime(Mode='Log_Write',
                              Sector='MyToolbar.Worker.socket_try',
                              Contents ='Socket Coonnected',
                              SavePath=init())
                        pendant.Main.robot_connect_status(pendant.Main,True,None)
                    else:
                        cTime(Mode='Log_Write',
                              Sector='MyToolbar.Worker.socket_try',
                              Contents ='Socket Coonnect Failed',
                              SavePath=init())
                        pendant.Main.robot_connect_status(pendant.Main,False,None)
            except:
                cTime(Mode='Log_Write',
                      Sector='MyToolbar.Worker.socket_try',
                      Contents ='Socket Coonnect Failed',
                      SavePath=init())
                pendant.Main.robot_connect_status(pendant.Main,False,None)
                
    
    def socket_check(self):
        try:
            pendant.Main.client_socket.sendall(b"ping")
            return True
        except:
            return False
              
    def socket_try(self):
        try:
            host,port = cGlobal.get_HostPort(self)
            port = int(port)
            # host = '127.0.0.1'
            # port = 8080
            cTime(Mode='Log_Write'
                  ,Sector='MyToolbar.Worker.socket_try',
                  Contents ='Socket Coonnect Try',
                  SavePath=init())
            pendant.Main.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            pendant.Main.client_socket.connect((host,port))
            return True
        except:
            return False
    
    
            
if __name__=="__main__":
    MainToolbar()