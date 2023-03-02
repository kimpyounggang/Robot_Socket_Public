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
    # WatitThread = QtCore.pyqtSignal(bool)
    # progress = QtCore.pyqtSignal(int)
    def __init__(self):
        super().__init__()
        cTime.Log_Write(self,'Running True')
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
                    cTime.Log_Write(self,'Socket Still Connect')
                    pendant.Main.robot_connect_status(pendant.Main,True,None)
                    pendant.Main.pause(self)
                    cTime.Log_Write(self,'Thread Pause')
                    Worker.socket_recv(self)
                    
                    # self.bools = True
                    # self.WatitThread.emit(self.bools)
                else:
                    cTime.Log_Write(self,'Socket Coonnect Failed')
                    if self.socket_try():
                        cTime.Log_Write(self,'Socket Coonnected')
                        pendant.Main.robot_connect_status(pendant.Main,True,None)
                    else:
                        cTime.Log_Write(self,'Socket Coonnect Failed')
                        pendant.Main.robot_connect_status(pendant.Main,False,None)
            except:
                cTime.Log_Write(self,'Socket Coonnect Failed')
                pendant.Main.robot_connect_status(pendant.Main,False,None)
                pendant.Main.resume(self)
                
    
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
            cTime.Log_Write(self,'Socket Coonnect Try')
            pendant.Main.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            pendant.Main.client_socket.connect((host,port))
            return True
        except:
            return False
        
    def socket_recv(self):
        w = w
        # pendant.Main.canvas = pendant.Main.canvas
        # pendant.Main.client_socket = socket_pointer
        cTime(Mode=w,Contents='Socket Recv Try')
        try:
            pendant.Main.client_socket.sendall(b"Ready_pos_x")
            cTime.Log_Write(self,'Socket Ready_pos_x')
            self.x_pos = pendant.Main.client_socket.recv(1024).decode()
            cTime.Log_Write(self,f'Socket Recv self.x_pos {self.x_pos}')
            pendant.Main.robot_pos_x.setText(self.x_pos)
            
            pendant.Main.client_socket.sendall(b"Ready_pos_y")
            cTime.Log_Write(self,'Socket Ready_pos_y')
            self.y_pos = pendant.Main.client_socket.recv(1024).decode()
            cTime.Log_Write(self,f'Socket Recv self.y_pos {self.y_pos}')
            pendant.Main.robot_pos_y.setText(self.y_pos)
            
            pendant.Main.client_socket.sendall(b"Ready_pos_z")
            cTime.Log_Write(self,'Socket Ready_pos_z')
            self.z_pos = pendant.Main.client_socket.recv(1024).decode()
            cTime.Log_Write(self,f'Socket Recv self.z_pos {self.z_pos}')
            pendant.Main.robot_pos_z.setText(self.z_pos)
            
            pendant.Main.xs = float(self.x_pos)
            pendant.Main.ys = float(self.y_pos)
            pendant.Main.zs = float(self.z_pos)
            cTime.Log_Write(self,f'Robot Pos -> data Load')
            pendant.Main.resume(self)
        except:
            cTime.Log_Write(self,'Socket Recv Failed')
            pendant.Main.resume(self)
            
class GraphUpdater(QtCore.QThread):
    data_updated = QtCore.pyqtSignal(numpy.ndarray)
    
    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            try:
                if hasattr(pendant.Main,'zs'):
                    GraphUpdater.data = numpy.array([[pendant.Main.xs,pendant.Main.ys,pendant.Main.zs]])
                    cTime.Log_Write(self,'Pos Load')
                    self.data_updated.emit(self.data)
                    cTime.Log_Write(self,'Pos Update')
            except:
                cTime.Log_Write(self,'Pos Load Failed')
            QtCore.QThread.sleep(1)
                
if __name__=='__main__':
    app =  pendant.QtWidgets.QApplication(pendant.sys.argv)
    main = pendant.Main()
    main.show()
    pendant.sys.exit(app.exec_())