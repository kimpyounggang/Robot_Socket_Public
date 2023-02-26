import pendant
from MyLog import cTime
from Mypath import init
import numpy as np
import matplotlib.animation

class left():
    def __init__(self, canvas, main,fontsize,toolbar,widget,bool):
        left.Widget(self, canvas,main,fontsize,toolbar,widget,bool)

    def Widget(self, canvas, main,fontsize,toolbar,widget,bool):
        pendant.Main.canvas = canvas
        pendant.Main.widgets = main
        pendant.Main.fontsizes = fontsize
        pendant.Main.LeftToolBar = toolbar
        pendant.Main.widget_kinds = widget
        pendant.Main.judge_con = bool
        pendant.Main.set_layout(pendant.Main,
                            layout1="QVBoxLayout",layout1_1="QHBoxLayout",layout1_2="QHBoxLayout",layout1_3="QHBoxLayout",
                            layout1_11="QHBoxLayout",layout1_12="QHBoxLayout",layout1_13="QHBoxLayout",
                            layout1_01="QVBoxLayout",layout1_02="QHBoxLayout",
                            layout2="QVBoxLayout")
        pendant.Main.widget(pendant.Main,kinds='label',name='로봇 연결',layout_num='LeftToolBar',stretchs=4,difname='robot_connect')
        pendant.Main.widget(pendant.Main,kinds='label',name='현재 위치',layout_num='layout1_01',difname='robot_pos',stretchs=2)
        
        pendant.Main.widget(pendant.Main,kinds='label',name='X',layout_num='layout1_11',stretchs=2)
        pendant.Main.widget(pendant.Main,kinds='label',name='0000',layout_num='layout1_11',stretchs=2,difname='robot_pos_x')
        pendant.Main.widget(pendant.Main,kinds='label',name='mm',layout_num='layout1_11',stretchs=2)
        
        pendant.Main.widget(pendant.Main,kinds='label',name='Y',layout_num='layout1_12',stretchs=2)
        pendant.Main.widget(pendant.Main,kinds='label',name='0000',layout_num='layout1_12',stretchs=2,difname='robot_pos_y')
        pendant.Main.widget(pendant.Main,kinds='label',name='mm',layout_num='layout1_12',stretchs=2)
        
        pendant.Main.widget(pendant.Main,kinds='label',name='Z',layout_num='layout1_13',stretchs=2)
        pendant.Main.widget(pendant.Main,kinds='label',name='0000',layout_num='layout1_13',stretchs=2,difname='robot_pos_z')
        pendant.Main.widget(pendant.Main,kinds='label',name='mm',layout_num='layout1_13',stretchs=2)
        
        
        pendant.Main.widget(pendant.Main,kinds='label',name='로봇 이동',layout_num='layout1_02',stretchs=2)
        
        pendant.Main.widget(pendant.Main,kinds='label',name='X',layout_num='layout1_1',stretchs=2,difname='move_pos_x')
        pendant.Main.widget(pendant.Main,kinds='lineedit',name='',layout_num='layout1_1',stretchs=1)
        pendant.Main.widget(pendant.Main,kinds='label',name='mm',layout_num='layout1_1')
        pendant.Main.widget(pendant.Main,kinds='btn',name='이동',layout_num='layout1_1',stretchs=2, difname='move_x')
        
        pendant.Main.widget(pendant.Main,kinds='label',name='Y',layout_num='layout1_2',stretchs=2,difname='move_pos_y')
        pendant.Main.widget(pendant.Main,kinds='lineedit',name='',layout_num='layout1_2',stretchs=1)
        pendant.Main.widget(pendant.Main,kinds='label',name='mm',layout_num='layout1_2')
        pendant.Main.widget(pendant.Main,kinds='btn',name='이동',layout_num='layout1_2',stretchs=2, difname='move_y')
        
        pendant.Main.widget(pendant.Main,kinds='label',name='Z',layout_num='layout1_3',stretchs=2,difname='move_pos_z')
        pendant.Main.widget(pendant.Main,kinds='lineedit',name='',layout_num='layout1_3',stretchs=1)
        pendant.Main.widget(pendant.Main,kinds='label',name='mm',layout_num='layout1_3')
        pendant.Main.widget(pendant.Main,kinds='btn',name='이동',layout_num='layout1_3',stretchs=2, difname='move_z')

        pendant.Main.left_layout(pendant.Main)
        pendant.Main.robot_connect_status(pendant.Main,False,False)
        
    def set_leftlayout(self):
        pendant.Main.sets_layout(pendant.Main,'wid1','layout1_01')
        pendant.Main.sets_layout(pendant.Main,'wid2','layout1_11')
        pendant.Main.sets_layout(pendant.Main,'wid3','layout1_12')
        pendant.Main.sets_layout(pendant.Main,'wid4','layout1_13')
        pendant.Main.sets_layout(pendant.Main,'wid5','layout1_02')
        pendant.Main.sets_layout(pendant.Main,'wid6','layout1_1')
        pendant.Main.sets_layout(pendant.Main,'wid7','layout1_2')
        pendant.Main.sets_layout(pendant.Main,'wid8','layout1_3')
        
    def up_def(self):
        pass
    def up1_def(self):
        pass
    def up2_def(self):
        pass
    
    def move_x_def(self):
        pass
    def move_y_def(self):
        pass
    def move_z_def(self):
        pass
    
    def socket_recv(self):
        w = 'Log_Write'
        s = 'MyLeftwidget.Left.socket_recv'
        # pendant.Main.client_socket = socket_pointer
        cTime(Mode=w ,Sector=s,Contents='Socket Recv Try',SavePath=init())
        try:
            pendant.Main.client_socket.sendall(b"Ready_pos_x")
            cTime(Mode=w,Sector=s, Contents ='Socket Ready_pos_x',SavePath=init())
            self.x_pos = pendant.Main.client_socket.recv(1024).decode()
            cTime(Mode=w,Sector=s,Contents =f'Socket Recv self.x_pos {self.x_pos}',SavePath=init())
            pendant.Main.robot_pos_x.setText(self.x_pos)
            
            pendant.Main.client_socket.sendall(b"Ready_pos_y")
            cTime(Mode=w,Sector=s, Contents ='Socket Ready_pos_y',SavePath=init())
            self.y_pos = pendant.Main.client_socket.recv(1024).decode()
            cTime(Mode=w,Sector=s,Contents =f'Socket Recv self.y_pos {self.y_pos}', SavePath=init())
            pendant.Main.robot_pos_y.setText(self.y_pos)
            
            pendant.Main.client_socket.sendall(b"Ready_pos_z")
            cTime(Mode=w,Sector=s,Contents ='Socket Ready_pos_z', SavePath=init())
            self.z_pos = pendant.Main.client_socket.recv(1024).decode()
            cTime(Mode=w,Sector=s,Contents =f'Socket Recv self.z_pos {self.z_pos}', SavePath=init())
            pendant.Main.robot_pos_z.setText(self.z_pos)
            
            if hasattr(self, 'RobotPos'):
                cTime(Mode=w,Sector=s,Contents =f'Robot Pos -> exist', SavePath=init())    
                pendant.Main.x = [float(self.x_pos)]
                pendant.Main.y = [float(self.y_pos)]
                pendant.Main.z = [float(self.z_pos)]            
                self.ani = matplotlib.animation.FuncAnimation(pendant.Main.canvas.axes, left.update,interval=10)
                self.ani.save('aa.gif',fps=24)
                pendant.Main.canvas.draw()
                cTime(Mode=w,Sector=s,Contents =f'Robot Pos -> update', SavePath=init())
            else:
                cTime(Mode=w,Sector=s,Contents =f'Robot Pos -> not exist', SavePath=init())
                self.RobotPos = pendant.Main.canvas.axes.scatter(float(self.x_pos),float(self.y_pos),float(self.z_pos),marker='s',c='red')
                pendant.Main.x = [float(self.x_pos)]
                pendant.Main.y = [float(self.y_pos)]
                pendant.Main.z = [float(self.z_pos)]
                
                cTime(Mode=w,Sector=s,Contents =f'Robot Pos -> New draw', SavePath=init())
            
            pendant.Main.canvas.draw()
            pendant.Main.resume(self)
        except:
            cTime(Mode=w,Sector=s,Contents ='Socket Recv Failed', SavePath=init())
            pendant.Main.resume(self)
    
    def update(self):
        w = 'Log_Write'
        s = 'MyLeftwidget.Left.update'
        cTime(Mode=w,Sector=s,Contents =f'x append {self.x_pos}', SavePath=init())
        # left.x.append(self.x_pos)
        # left.y.append(self.y_pos)
        # left.z.append(self.z_pos)
        # self.RobotPos.set_offsets(np.c_[left.x,left.y,left.z])
        
    
if __name__=='__main__':
    left()