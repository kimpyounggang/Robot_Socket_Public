import pendant,numpy
import pyqtgraph.opengl as gl
import pyqtgraph as pg
from Myglobal import cGlobal
from Mypath import init
from MyLog import cTime
from MyVisual import Visualize
import  socket
from PyQt5 import QtWidgets,QtCore

class Worker(QtCore.QThread):
    btn_ = False
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
                    print(self.btn_)
                    if Worker.btn_ == True:
                        cTime(Mode='Log_Write',
                              Sector='MyToolbar.Worker.socket_try',
                              Contents ='rmove_que True',
                              SavePath=init())
                        res = 'rx,'+pendant.Main.rline_1.text()+','
                        pendant.Main.client_socket.sendall(bytes(res,encoding='utf-8'))
                        echo = pendant.Main.client_socket.recv(1024).decode()
                        if echo==res:
                            cTime(Mode='Log_Write',
                                        Sector='MyLeftToolbar.Left.rmove_x_def',
                                        Contents =f'Socket Send {res}',
                                        SavePath=init())
                            
                    pendant.Main.robot_connect_status(pendant.Main,True,None)
                    pendant.Main.pause(self)
                    cTime(Mode='Log_Write',
                          Sector='MyToolbar.Worker.socket_try',
                          Contents ='Thread Pause',
                          SavePath=init())
                    Worker.socket_recv(self)
                    
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
                        if Worker.btn_ == True:
                            cTime(Mode='Log_Write',
                              Sector='MyToolbar.Worker.socket_try',
                              Contents ='rmove_que True',
                              SavePath=init())
                            res = 'rx,'+pendant.Main.rline_1.text()+','
                            pendant.Main.client_socket.sendall(bytes(res,encoding='utf-8'))
                            echo = pendant.Main.client_socket.recv(1024).decode()
                            if echo==res:
                                cTime(Mode='Log_Write',
                                        Sector='MyLeftToolbar.Left.rmove_x_def',
                                        Contents =f'Socket Send {res}',
                                        SavePath=init())
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
                pendant.Main.resume(self)
                
    def socket_check(self):
        try:
            pendant.Main.client_socket.sendall(b"ping")
            echo = pendant.Main.client_socket.recv(100).decode()
            if echo=="ping":
                return True
            else:
                return False
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
        
    def socket_recv(self):
        w = 'Log_Write'
        s = 'MyThread.Worker.socket_recv'
        cTime(Mode=w ,Sector=s,Contents='Socket Recv Try',SavePath=init())
        try:
            pos = pendant.Main.client_socket.recv(100).decode()
            pendant.Main.client_socket.sendall(bytes(pos,encoding='utf-8'))
            pos = pos.strip('"')
            poss = pos.split(',')
            cTime(Mode=w,Sector=s, Contents =f'Socket RECV {pos}',SavePath=init())
            cTime(Mode=w,Sector=s, Contents =f'Socket RECV {poss}',SavePath=init())
            if 'x_pos' in str(poss[0]):
                cTime(Mode=w,Sector=s, Contents =f'Socket RECV {poss[0]}',SavePath=init())
                self.x_pos = poss[0].replace('x_pos','')
                cTime(Mode=w,Sector=s,Contents =f'Socket Recv x_pos {self.x_pos}',SavePath=init())
                pendant.Main.robot_pos_x.setText(self.x_pos)
                pendant.Main.xs = float(self.x_pos)
            
            if 'y_pos' in str(poss[1]):
                cTime(Mode=w,Sector=s, Contents =f'Socket RECV {poss[1]}',SavePath=init())
                self.y_pos = poss[1].replace('y_pos','')
                cTime(Mode=w,Sector=s,Contents =f'Socket Recv y_pos {self.y_pos}', SavePath=init())
                pendant.Main.robot_pos_y.setText(self.y_pos)
                pendant.Main.ys = float(self.y_pos)
                
            if 'z_pos' in str(poss[2]):
                cTime(Mode=w,Sector=s, Contents =f'Socket RECV {poss[2]}',SavePath=init())
                self.z_pos = poss[2].replace('z_pos','')
                if '"' in self.z_pos:
                    self.z_pos = self.z_pos.split('"')
                    self.z_pos = self.z_pos[0]
                cTime(Mode=w,Sector=s,Contents =f'Socket Recv z_pos {self.z_pos}', SavePath=init())
                pendant.Main.robot_pos_z.setText(self.z_pos)
                pendant.Main.zs = float(self.z_pos)
            
            pendant.Main.resume(self)
        except:
            cTime(Mode=w,Sector=s,Contents ='Socket Recv Failed', SavePath=init())
            pendant.Main.resume(self)
            
class GraphUpdater(QtCore.QThread):
    data_updated = QtCore.pyqtSignal(numpy.ndarray)
    time_read = 0
    def __init__(self):
        super().__init__()
        
    def run(self):
        w = 'Log_Write'
        s = 'MyThread.GraphUpdater.run'
        while True:
            try:
                if hasattr(pendant.Main,'zs'):
                    GraphUpdater.data = numpy.array([[pendant.Main.xs,pendant.Main.ys,pendant.Main.zs]])
                    cTime(Mode=w,Sector=s,Contents ='Pos Load', SavePath=init())
                    self.data_updated.emit(self.data)
                    cTime(Mode=w,Sector=s,Contents ='Pos Update', SavePath=init())
            except:
                cTime(Mode=w,Sector=s,Contents ='Pos Load Failed', SavePath=init())
            QtCore.QThread.sleep(1)                    
                
                
if __name__=='__main__':
    app =  pendant.QtWidgets.QApplication(pendant.sys.argv)
    main = pendant.Main()
    main.show()
    pendant.sys.exit(app.exec_())