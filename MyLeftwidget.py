import pendant
from Myglobal import cGlobal
from MyLog import cTime
from Mypath import init
import socket,MyThread,time

class left():
    def __init__(self, canvas,main,fontsize,toolbar,widget,bool):
        pendant.Main.canvas = canvas
        pendant.Main.widgets = main
        pendant.Main.fontsizes = fontsize
        pendant.Main.LeftToolBar = toolbar
        pendant.Main.widget_kinds = widget
        pendant.Main.judge_con = bool
        left.Widget(self)
        

    def Widget(self):
        
        pendant.Main.set_layout(pendant.Main,
                            layout1="QVBoxLayout",layout1_1="QHBoxLayout",layout1_2="QHBoxLayout",layout1_3="QHBoxLayout",
                            layout1_11="QHBoxLayout",layout1_12="QHBoxLayout",layout1_13="QHBoxLayout",
                            layout1_01="QVBoxLayout",layout1_02="QHBoxLayout",layout1_03="QHBoxLayout",
                            layout1_21="QHBoxLayout",layout1_22="QHBoxLayout",layout1_23="QHBoxLayout",
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
        
        
        pendant.Main.widget(pendant.Main,kinds='label',name='로봇 툴좌표 이동',layout_num='layout1_02',stretchs=2)
        
        pendant.Main.widget(pendant.Main,kinds='label',name='X',layout_num='layout1_1',stretchs=2)
        pendant.Main.widget(pendant.Main,kinds='lineedit',name='',layout_num='layout1_1',stretchs=1,difname='rline_1')
        pendant.Main.widget(pendant.Main,kinds='label',name='+ mm',layout_num='layout1_1')
        pendant.Main.widget(pendant.Main,kinds='btn',name='이동',layout_num='layout1_1',stretchs=2, difname='rmove_x')
        
        pendant.Main.widget(pendant.Main,kinds='label',name='Y',layout_num='layout1_2',stretchs=2)
        pendant.Main.widget(pendant.Main,kinds='lineedit',name='',layout_num='layout1_2',stretchs=1,difname='rline_2')
        pendant.Main.widget(pendant.Main,kinds='label',name='+ mm',layout_num='layout1_2')
        pendant.Main.widget(pendant.Main,kinds='btn',name='이동',layout_num='layout1_2',stretchs=2, difname='rmove_y')
        
        pendant.Main.widget(pendant.Main,kinds='label',name='Z',layout_num='layout1_3',stretchs=2)
        pendant.Main.widget(pendant.Main,kinds='lineedit',name='',layout_num='layout1_3',stretchs=1,difname='rline_3')
        pendant.Main.widget(pendant.Main,kinds='label',name='+ mm',layout_num='layout1_3')
        pendant.Main.widget(pendant.Main,kinds='btn',name='이동',layout_num='layout1_3',stretchs=2, difname='rmove_z')
        
        pendant.Main.widget(pendant.Main,kinds='label',name='로봇 베이스 이동',layout_num='layout1_03',stretchs=2)
        
        pendant.Main.widget(pendant.Main,kinds='label',name='X',layout_num='layout1_21',stretchs=2)
        pendant.Main.widget(pendant.Main,kinds='lineedit',name='',layout_num='layout1_21',stretchs=1,difname='iline_1')
        pendant.Main.widget(pendant.Main,kinds='label',name='mm',layout_num='layout1_21')
        pendant.Main.widget(pendant.Main,kinds='btn',name='이동',layout_num='layout1_21',stretchs=2, difname='imove_x')
        
        pendant.Main.widget(pendant.Main,kinds='label',name='Y',layout_num='layout1_22',stretchs=2)
        pendant.Main.widget(pendant.Main,kinds='lineedit',name='',layout_num='layout1_22',stretchs=1,difname='iiline_1')
        pendant.Main.widget(pendant.Main,kinds='label',name='mm',layout_num='layout1_22')
        pendant.Main.widget(pendant.Main,kinds='btn',name='이동',layout_num='layout1_22',stretchs=2, difname='imove_y')
        
        pendant.Main.widget(pendant.Main,kinds='label',name='Z',layout_num='layout1_23',stretchs=2)
        pendant.Main.widget(pendant.Main,kinds='lineedit',name='',layout_num='layout1_23',stretchs=1,difname='iline_1')
        pendant.Main.widget(pendant.Main,kinds='label',name='mm',layout_num='layout1_23')
        pendant.Main.widget(pendant.Main,kinds='btn',name='이동',layout_num='layout1_23',stretchs=2, difname='imove_z')

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
        pendant.Main.sets_layout(pendant.Main,'wid9','layout1_03')
        pendant.Main.sets_layout(pendant.Main,'wid10','layout1_21')
        pendant.Main.sets_layout(pendant.Main,'wid11','layout1_22')
        pendant.Main.sets_layout(pendant.Main,'wid12','layout1_23')
        
    def up_def(self):
        pass
    def up1_def(self):
        pass
    def up2_def(self):
        pass

    def rmove_x_def(self):
        # MyThread.Worker.lab_stop(self)
        cTime.Log_Write(self,'rmove_que True')
        print(pendant.Main.rline_1.text())
        res = 'part,'+pendant.Main.rline_1.text()+','+'0,'+'0,'
        pendant.Main.client_socket.sendall(bytes(res,encoding='utf-8'))
        cTime.Log_Write(self,f'Socket Send {res}')
        # MyThread.Worker.lab_run(self)
       
    
    def rmove_y_def(self):
        # MyThread.Worker.lab_stop(self)
        cTime.Log_Write(self,'rmove_que True')
        print(pendant.Main.rline_1.text())
        res = 'part,'+'0,'+pendant.Main.rline_2.text()+','+'0,'
        pendant.Main.client_socket.sendall(bytes(res,encoding='utf-8'))
        cTime.Log_Write(self,f'Socket Send {res}')
        # MyThread.Worker.lab_run(self)
        
    def rmove_z_def(self):
        # MyThread.Worker.lab_stop(self)
        cTime.Log_Write(self,'rmove_que True')
        print(pendant.Main.rline_1.text())
        res = 'part,'+'0,'+'0,'+pendant.Main.rline_3.text()+','
        pendant.Main.client_socket.sendall(bytes(res,encoding='utf-8'))
        cTime.Log_Write(self,f'Socket Send {res}')
        # MyThread.Worker.lab_run(self)
    
    def imove_x_def(self):
        # MyThread.Worker.lab_stop(self)
        cTime.Log_Write(self,'rmove_que True')
        res = 'base,'+pendant.Main.iline_1.text()+','+'0,'+'0,'
        pendant.Main.client_socket.sendall(bytes(res,encoding='utf-8'))
        cTime.Log_Write(self,f'Socket Send {res}')
        # MyThread.Worker.lab_run(self)
        
    def imove_y_def(self):
        # MyThread.Worker.lab_stop(self)
        cTime.Log_Write(self,'rmove_que True')
        res = 'base,'+'0,'+pendant.Main.iline_2.text()+','+'0,'
        pendant.Main.client_socket.sendall(bytes(res,encoding='utf-8'))
        cTime.Log_Write(self,f'Socket Send {res}')
        # MyThread.Worker.lab_run(self)
        
    def imove_z_def(self):
        # MyThread.Worker.lab_stop(self)
        cTime.Log_Write(self,'rmove_que True')
        res = 'base,'+'0,'+'0,'+pendant.Main.iline_3.text()+','
        pendant.Main.client_socket.sendall(bytes(res,encoding='utf-8'))
        cTime.Log_Write(self,f'Socket Send {res}')
        # MyThread.Worker.lab_run(self)
    
    
    
    # def update(self):
    #     w = 'Log_Write'
    #     s = 'MyLeftwidget.Left.update'
    #     cTime(Mode=w,Sector=s,Contents =f'x append {self.x_pos}', SavePath=init())
        # left.x.append(self.x_pos)
        # left.y.append(self.y_pos)
        # left.z.append(self.z_pos)
        # self.RobotPos.set_offsets(np.c_[left.x,left.y,left.z])
        
    
if __name__=='__main__':
    app =  pendant.QtWidgets.QApplication(pendant.sys.argv)
    main = pendant.Main()
    main.show()
    pendant.sys.exit(app.exec_())