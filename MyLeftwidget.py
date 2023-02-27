import pendant
from Myglobal import cGlobal
from MyLog import cTime
from Mypath import init

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
    
    
    
    # def update(self):
    #     w = 'Log_Write'
    #     s = 'MyLeftwidget.Left.update'
    #     cTime(Mode=w,Sector=s,Contents =f'x append {self.x_pos}', SavePath=init())
        # left.x.append(self.x_pos)
        # left.y.append(self.y_pos)
        # left.z.append(self.z_pos)
        # self.RobotPos.set_offsets(np.c_[left.x,left.y,left.z])
        
    
if __name__=='__main__':
    left()