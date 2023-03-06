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
        _stop_event = QtCore.QWaitCondition()
        _mutex = QtCore.QMutex()
        pendant.Main.running_thread = True
    
    def run(self):
        temp = 0
        if temp == 0:
            pendant.Main.robot_connect_status(pendant.Main,False,True)
        while pendant.Main.running_thread:
            # self._mutex.lock()
            # self._stop_event.wait(self._mutex)
            # self._mutex.unlock()
            QtCore.QThread.sleep(1)
            temp +=1
            try:
                cTime.Log_Write(self,f'Time Tracker {temp}')
                if self.socket_check():
                    cTime.Log_Write(self,'Socket Still Connect')
                    pendant.Main.robot_connect_status(pendant.Main,True,None)
                    # Worker.pause(self)
                    cTime.Log_Write(self,'Thread Pause')
                    Worker.socket_recv(self)
                else:
                    cTime.Log_Write(self,'Socket Coonnect Failed')
                    if self.socket_try():
                        # Worker.socket_check(self)
                        cTime.Log_Write(self,'Socket Coonnected')
                        pendant.Main.robot_connect_status(pendant.Main,True,None)
                    else:
                        cTime.Log_Write(self,'Socket Coonnect Failed')
                        pendant.Main.robot_connect_status(pendant.Main,False,None)
            except:
                cTime.Log_Write(self,'Socket Coonnect Failed')
                pendant.Main.robot_connect_status(pendant.Main,False,None)
                self.socket_try()
                # pendant.Main.resume(self)
    
    def lab_stop(self):
        pendant.Main.running_thread = False
        
    def lab_run(self):
        pendant.Main.running_thread = True
    
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
            cTime.Log_Write(self,'Socket Coonnect Try')
            pendant.Main.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            pendant.Main.client_socket.connect((host,port))
            return True
        except:
            return False
        
    def socket_recv(self):
        cTime.Log_Write(self,'Socket Recv Try')
        try:
            pos = pendant.Main.client_socket.recv(100).decode()
            pos = pos.strip('"')
            poss = pos.split(',')
            cTime.Log_Write(self,f'Socket RECV {pos}')
            cTime.Log_Write(self,f'Socket RECV {poss}')
            if 'x_pos' in str(poss[0]):
                cTime.Log_Write(self,f'Socket RECV {poss[0]}')
                self.x_pos = poss[0].replace('x_pos','')
                cTime.Log_Write(self,f'Socket Recv x_pos {self.x_pos}')
                pendant.Main.robot_pos_x.setText(self.x_pos)
                pendant.Main.xs = float(self.x_pos)
            
            if 'y_pos' in str(poss[1]):
                cTime.Log_Write(self,f'Socket RECV {poss[1]}')
                self.y_pos = poss[1].replace('y_pos','')
                cTime.Log_Write(self,f'Socket Recv y_pos {self.y_pos}')
                pendant.Main.robot_pos_y.setText(self.y_pos)
                pendant.Main.ys = float(self.y_pos)
                
            if 'z_pos' in str(poss[2]):
                cTime.Log_Write(self,f'Socket RECV {poss[2]}')
                self.z_pos = poss[2].replace('z_pos','')
                if '"' in self.z_pos:
                    self.z_pos = self.z_pos.split('"')
                    self.z_pos = self.z_pos[0]
                cTime.Log_Write(self,f'Socket Recv z_pos {self.z_pos}')
                pendant.Main.robot_pos_z.setText(self.z_pos)
                pendant.Main.zs = float(self.z_pos)

        except:
            cTime.Log_Write(self,'Socket Recv Failed')
            pendant.Main.resume(self)
            
class GraphUpdater(QtCore.QThread):
    data_updated = QtCore.pyqtSignal(numpy.ndarray)
    time_read = 0
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
                pass
            QtCore.QThread.sleep(1)
                
                
if __name__=='__main__':
    app =  pendant.QtWidgets.QApplication(pendant.sys.argv)
    main = pendant.Main()
    main.show()
    pendant.sys.exit(app.exec_())