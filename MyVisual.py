import pendant
from MyLog import cTime
from Mypath import init
from Myglobal import cGlobal
import pyqtgraph.opengl as gl
import numpy as np
class Visualize():
    def __init__(self, canvas, main,fontsize,bool):
        pendant.Main.canvas = canvas
        pendant.Main.widgets = main
        pendant.Main.fontsizes = fontsize
        pendant.Main.judge_con = bool
        Visualize.Widget(self)

    def Widget(self):
        

        pendant.Main.Hslider = pendant.QtWidgets.QSlider(pendant.QtCore.Qt.Horizontal)
        pendant.Main.Hslider.setRange(-180,180)
        pendant.Main.Hslider.valueChanged.connect(Visualize.slider_set)
        pendant.Main.Vslider = pendant.QtWidgets.QSlider(pendant.QtCore.Qt.Vertical)
        pendant.Main.Vslider.setRange(-180,180)
        pendant.Main.Vslider.valueChanged.connect(Visualize.slider_set)
    
        pendant.Main.set_layout(pendant.Main,vis_layout="QVBoxLayout",vis_tool='QHBoxLayout')
        # pendant.Main.vis_layout.addWidget(pendant.Main.toolbar)
        pendant.Main.vis_layout.addWidget(pendant.Main.canvas)
        pendant.Main.vis_layout.addWidget(pendant.Main.Hslider)
        pendant.Main.vis_tool.addWidget(pendant.Main.Vslider)
        
        pendant.Main.visual_layout(pendant.Main)
        
        
        
        
    def set_vislayout(self):
        pendant.Main.sets_layout(pendant.Main,'wid','vis_layout')
        pendant.Main.sets_layout(pendant.Main,'wcontrol','vis_tool')
        
    def slider_set(self):
        # pendant.Main.canvas.axes.view_init(pendant.Main.Vslider.value(),pendant.Main.Hslider.value())
        # pendant.Main.canvas.draw()
        pass
    def log_read_line(self,path,read_index):
        read_data = ''
        with open(path,'r') as read_txt:
            txtlist = read_txt.readlines()
            for i, txt in enumerate(txtlist,start=0):
                if i == read_index:
                    read_data = txt.replace('\n','')
        return read_data
    
    def create_obj(self,path):
        Visualize._private_val_initail(self)
        save = False
        save1 = False
        save2 = False

        with open(path,'r') as read_txt:
            txtlength = read_txt.readlines()
        for i1 in range(0,len(txtlength)):
            parc = ''
            str_num_start = 0
            str_num_end = 0
            for i,str_ in enumerate(Visualize.log_read_line(self,path,i1),start=0):
                if 'robtarget' in parc :
                    str_num_start = i
                    parc = ''
                    save = True
                if save == True and ':=[[' in parc:
                    str_num_end = i
                    self.point_bef_name_proc.append(Visualize.log_read_line(self,path,i1)[str_num_start:str_num_end-4])
                    parc = ''
                    save = False
                    save1 = True
                    str_num_start=str_num_end
                    str_num_end=0
                if save1 == True and '],[' in parc:
                    parc = ''
                    str_num_end = i
                    self.point_bef_proc.append(Visualize.log_read_line(self,path,i1)[str_num_start:str_num_end-3])
                    str_num_start=str_num_end
                    save1 = False
                    save2 = True
                    next
                if save2 == True and '],[' in parc:
                    parc = ''
                    str_num_end = i
                    self.point_axis_bef_proc.append(Visualize.log_read_line(self,path,i1)[str_num_start:str_num_end-3])
                    save2 = False
                    break
                parc=parc+str_
        
        points_num = len(self.point_bef_name_proc)
        [self.point_name_proc.append(str(i1).strip(' ')) for i1 in self.point_bef_name_proc]
        for i1 in range(points_num):
            self.point_pos.append(self.point_bef_proc[i1].split(','))
            self.point_axis_quaternion.append(self.point_axis_bef_proc[i1].split(','))
            # self.point_axis_euler.append(robot.sub.euler_from_quaternion(self,
            #     float(self.point_axis_quaternion[i1][0]),float(self.point_axis_quaternion[i1][1]),
            #     float(self.point_axis_quaternion[i1][2]),float(self.point_axis_quaternion[i1][3])))

        for i1 in range(points_num):
            self.point_list.append([float(self.point_pos[i1][0])/cGlobal.get_Resizes(self),
                                   float(self.point_pos[i1][1])/cGlobal.get_Resizes(self),
                                   float(self.point_pos[i1][2])/cGlobal.get_Resizes(self)])
            
            spl = gl.GLScatterPlotItem(pos = np.array([[self.point_list[i1][0],
                                              self.point_list[i1][1],
                                              self.point_list[i1][2]]]))
            pendant.Main.canvas.addItem(spl)
            pendant.Main.Right_listwidget.addItem(f'{self.point_name_proc[i1]}')
            
    
    # def Widget(self):
    #     
    #     pendant.Main.visual_pos = pendant.QtWidgets.QVBoxLayout()
            # pendant.Main._toolbar = pendant.NavigationToolbar(pendant.Main.canvas, pendant.Main)
    #     pendant.Main.visual_pos.addWidget(pendant.Main._toolbar)
    #     pendant.Main.visual_pos.addWidget(pendant.Main.canvas)
    #     _visualGroup = pendant.QtWidgets.QGroupBox()
    #     _visualGroup.setLayout(pendant.Main.visual_pos)
    #     pendant.Main.visual_Toolbar.addWidget(_visualGroup)
    
    def _private_val_initail(self):
        pendant.Main._private_int(self,'Delete','touch_click_num','r_u_search','point_now_row_director')
        pendant.Main._private_list(self,'Delete','obj_path_list','point_list','point_nowrow','arrow_list','touch_list',
                        'point_bef_name_proc','point_name_proc','point_bef_proc','point_pos','point_axis_bef_proc',
                        'point_axis_quaternion','point_axis_euler','tcpcon_list')
        pendant.Main._private_int(self,'Create','touch_click_num','r_u_search','point_now_row_director')
        pendant.Main._private_list(self,'Create','obj_path_list','point_list','point_nowrow','arrow_list','touch_list',
                        'point_bef_name_proc','point_name_proc','point_bef_proc','point_pos','point_axis_bef_proc',
                        'point_axis_quaternion','point_axis_euler','tcpcon_list')
    
if __name__=='__main__':
    Visualize()