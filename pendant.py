import sys,os,math,numpy
from PyQt5 import QtWidgets,QtGui,QtCore
import numpy
from stl import mesh
import Mymenubar,MyLeftwidget,MyToolbar,MyVisual,MyThread
from MyLog import cTime
from Mypath import init
from Myglobal import cGlobal
import pyqtgraph.opengl as gl


# class MplCanvas():
#     def __init__(self,):
#         Main.axes = gl.GLViewWidget()
#         Main.axes.opts['distance'] = 2000
#         Main.axes.setWindowTitle('Title')

#         _grid = gl.GLGridItem()
#         Main.axes.addItem(_grid)
        
#         # self.axes.axis([-150, 150, -150, 150])
#         # self.axes.grid()   
#         # super(MplCanvas, self).__init__()

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        ####### 이니셜라이즈
        super().__init__()
        self.defined()

        ####### 메뉴바 (File, Edit ...)
        Mymenubar.menubar(Main.menubars,Main.widget_kinds)
        
        ####### 메인 툴바
        MyToolbar.MainToolbar.toolbar(self,Main.rule_icon,Main.toolbarareas)
        
        ####### 왼쪽 툴바 (상태창, 명령줄)  -> 포인터 설정에 시간이 걸리고 직관적이지 않다. main._init_ 에서 선언
        Main.LeftToolBar = QtWidgets.QToolBar("Control Proc", self)
        MyLeftwidget.left(Main.canvas,Main.widgets,cGlobal.get_Fontsizes,Main.LeftToolBar,Main.widget_kinds,Main.judge_con)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, Main.LeftToolBar)
        
        ####### 중앙 위젯
        # Main.VisualToolbar = QtWidgets.QToolBar("Visual Proc",self)
        # Main.toolbar = NavigationToolbar(Main.canvas, self)
        
        MyVisual.Visualize(Main.canvas,Main.widgets,cGlobal.get_Fontsizes,Main.judge_con)
        self.setCentralWidget(Main.canvas) # 이전 -> self.setCentralWidget(Main.widgets)
        
        ####### 스레드 시작(소켓)
        self.socket_thread_start()
    
    
    def defined(self):
        Main.widgets = QtWidgets.QWidget()
        Main.canvas = gl.GLViewWidget()
        self.canvas_grid()
        
        # self.Lab_Mesh()
        # Main.canvas.addItem(ygrid)
        # Main.canvas.addItem(zgrid)
        # Main.canvas.show()
        # gx = gl.GLGridItem(size=QtGui.QVector3D(20000,20000,20000))
        # gx.setSpacing=((100,100,100))
        # # # gx.rotate(90, 0, 1, 0)
        # # # gx.translate(-10, 0, 10)
        # Main.canvas.addItem(gx)
        # gy = gl.GLGridItem(size=QtGui.QVector3D(2000,2000,1))
        # gy.rotate(90, 1, 0, 0)
        # gy.translate(0, -10, 10)
        # Main.canvas.addItem(gy)
        # gz = gl.GLGridItem(size=QtGui.QVector3D(2000,2000,1))
        # gz.translate(0, 0, 0)
        # Main.canvas.addItem(gz)
# size=QtGui.QVector3D(2000,2000,2000)
        

        Main.public_int('robot_now_row_director','remote_now_dir','camera_axis_x','camera_axis_y','camera_axis_z')
        Main.public_list('robot_nowrow','robot_list','base_list','remote_now_row','axes_list')
        Main.setWindowTitle(self, '로봇 조작 프로그램')
        Main.setGeometry(self, 300, 300, 1400, 1200) #창의크기 3번째 가로  4번째 세로
        Main.widget_kinds = {"btn" : "QPushButton",
                             "lineedit" : "QLineEdit",
                             "listWd" : "QListWidget",
                             "label" : "QLabel",
                             "action" : "QAction"}
        Main.rule_icon = {"undertext":"ToolButtonTextUnderIcon"}
        Main.toolbarareas = {"top":"TopToolBarArea","right":"RightToolBarArea","bottom":"BottomToolBarArea"}
        
        
        
        Main.menubars = self.menuBar()
        Main.menubars.setNativeMenuBar(False)
        Main.judge_con = False
        

    
        
    def widget(self, *args, **kwargs):
        name = kwargs['name']
        name = name.replace(' ','')
        if 'difname' in kwargs: 
            difname = kwargs['difname']
            defname = difname
        else: 
            defname = name
        if 'kinds' in kwargs: 
            kinds = kwargs['kinds']
            if kinds=='action':
                addwidget = 'addAction'
                # self.file = self.menubar.adddMenu('파일')
                # getattr(self, getattr(menubar, addmenu))
                setattr(self, defname, getattr(Main.menubars,'addMenu')(name))
            else:
                addwidget = 'addWidget'
        if 'layout_num' in kwargs: layout_num = kwargs['layout_num']
        if 'stretchs' in kwargs: stretchs = kwargs['stretchs']
        else: stretchs = 1
        if len(args)<1:
            setattr(self,defname, getattr(QtWidgets,Main.widget_kinds[kinds])(name))
            getattr(getattr(Main, layout_num),addwidget)(getattr(self,defname))
            getattr(getattr(self,defname),'setFont')(QtGui.QFont("",stretchs*cGlobal.get_Fontsizes(self)))
        else:
            for i in args:
                setattr(self,f'{defname}_{i}', getattr(QtWidgets,Main.widget_kinds[kinds])(i))
                getattr(getattr(self, defname),addwidget)(getattr(self,f'{defname}_{i}'))
                if kinds=='action':
                    getattr(self,f'{defname}_{i}').triggered.connect(getattr(Mymenubar,f'{defname}_{i}_def'))
        if kinds=='btn':
            getattr(self,defname).clicked.connect(getattr(MyLeftwidget.left,f'{defname}_def'))
        if kinds=='label':
            getattr(getattr(self,defname),'setAlignment')(QtCore.Qt.AlignCenter)
    
    def add_toolbar(self, *args, **kwargs):
        if 'toolbarname' in kwargs:toolbarname = kwargs['toolbarname']
        if 'area' in kwargs: area = kwargs['area']
        setattr(Main,toolbarname, QtWidgets.QToolBar(toolbarname))
        if 'rule' in kwargs:
            rule = kwargs['rule']
            getattr(Main,toolbarname).setToolButtonStyle(getattr(getattr(QtCore,'Qt'),Main.rule_icon[rule]))
        if len(args)>1:
            for i in args:
                setattr(Main,i,QtWidgets.QAction(QtGui.QIcon(f"./icon/{i}.png"), i))
                getattr(getattr(Main, toolbarname),'addAction')(getattr(Main,i))
                getattr(Main,i).triggered.connect(getattr(MyToolbar.MainToolbar,f'{i}_def'))
        else:
            getattr(Main,toolbarname).addWidget(args[0])
        getattr(self,'addToolBar')( getattr(getattr(QtCore,'Qt'),Main.toolbarareas[area]), getattr(Main,toolbarname))

    
    
    def set_layout(self, **kwargs):
        for i,i1 in kwargs.items():
            setattr(Main, i, getattr(QtWidgets, i1)(Main.widgets))

    def add_widget(self,pLayout,name):
        getattr(getattr(Main, pLayout),'addWidget')(name)
    
    def add_layout(self,pTarget, pLayout, stretch):
        getattr(getattr(Main, pTarget),'addLayout')(getattr(Main, pLayout), stretch)
    
    def sets_layout(self,pTarget, pLayout):
        getattr(getattr(Main, pTarget),'setLayout')(getattr(Main, pLayout))
        
    def public_list(self,*argument):
        for i in argument:setattr(Main,f'{i}',[])
    def public_int(self,*argument):
        for i in argument:setattr(Main,f'{i}',0)
    def _private_list(self,mode,*argument):
        if mode == 'Delete':
            for i in argument: 
                if hasattr(Main,f'{i}'):delattr(Main,f'{i}')
        elif mode == 'Create':
            for i in argument: setattr(Main,f'{i}',[])
    def _private_int(self,mode,*argument):
        if mode == 'Delete':
            for i in argument: 
                if hasattr(Main,f'{i}'): delattr(Main,f'{i}')
        elif mode == 'Create':
            for i in argument: setattr(Main,f'{i}',0)
        
        
    def left_layout(self):
        Main.wid1 = QtWidgets.QGroupBox()
        Main.wid2 = QtWidgets.QGroupBox()
        Main.wid3 = QtWidgets.QGroupBox()
        Main.wid4 = QtWidgets.QGroupBox()
        Main.wid5 = QtWidgets.QGroupBox()
        Main.wid6 = QtWidgets.QGroupBox()
        Main.wid7 = QtWidgets.QGroupBox()
        Main.wid8 = QtWidgets.QGroupBox()
        MyLeftwidget.left.set_leftlayout(Main)
        Main.LeftToolBar.addWidget(Main.wid1)
        Main.LeftToolBar.addWidget(Main.wid2)
        Main.LeftToolBar.addWidget(Main.wid3)
        Main.LeftToolBar.addWidget(Main.wid4)
        Main.LeftToolBar.addWidget(Main.wid5)
        Main.LeftToolBar.addWidget(Main.wid6)
        Main.LeftToolBar.addWidget(Main.wid7)
        Main.LeftToolBar.addWidget(Main.wid8)
        
    def visual_layout(self):
        Main.wid = QtWidgets.QGroupBox()
        Main.wcontrol = QtWidgets.QGroupBox()
        MyVisual.Visualize.set_vislayout(Main)
        # Main.VisualToolbar.addWidget(Main.wid)
        # Main.VisualToolbar.addWidget(Main.wcontrol)
 
        
    
    
    def robot_connect_status(self,bool,judg):
        if judg != None:
            Main.judge_con = judg
        if Main.judge_con == False:
            if bool==True:
                Main.LogBrowser.append(f'Connected')
                self.green_connect(self)
                Main.judge_con=True
            if bool==False:
                Main.judge_con=False
        if Main.judge_con == True:
            if bool==True:
                Main.judge_con=True
            if bool==False:
                Main.LogBrowser.append(f'Connect Failed')
                self.red_connect(self)
                Main.judge_con=False
    
    def green_connect(self):
        cTime(Mode='Log_Write',
                              Sector='pendant.Main.green_connect',
                              Contents ='Turn On GreenLight',
                              SavePath=init())
        Main.robot_connect.setStyleSheet("color: Green;"
                               "background-color: #e0f2c9;"
                               "border-style: dashed;"
                               "border-width: 3px;"
                               "border-color: #a2ff30")
    def red_connect(self):
        cTime(Mode='Log_Write',
                              Sector='pendant.Main.red_connect',
                              Contents ='Turn On RedLight',
                              SavePath=init())
        Main.robot_connect.setStyleSheet("color: red;"
                                    "background-color: #f2c9c9;"
                                    "border-style: dashed;"
                                    "border-width: 3px;"
                                    "border-color: #d62727")
    
    def socket_thread_start(self):
        Main.worker = MyThread.Worker()
        Main.worker.finished.connect(Main.worker.deleteLater)
        Main.worker.start()
        # Main.worker.WatitThread.connect(self.WaitThread)
        Main.updater = MyThread.GraphUpdater()
        Main.updater.data_updated.connect(self.update_data)
        Main.updater.finished.connect(Main.updater.deleteLater)
        Main.updater.start()
    
    @QtCore.pyqtSlot(numpy.ndarray)
    def update_data(self, data):
        Main.scatter.setData(pos=data)
        Main.quad.resetTransform()
        Main.quad.translate(data[0][0]-75,data[0][1]-75,data[0][2]-75)
        
    # @pyqtSlot(bool)
    # def WaitThread(self, bools):
        
    def resume(self):
        cTime(Mode='Log_Write',
                              Sector='pendant.Main.resume',
                              Contents ='Running True',
                              SavePath=init())
        Main.running = True
    
    def pause(self):
        cTime(Mode='Log_Write',
                              Sector='pendant.Main.pause',
                              Contents ='Running False',
                              SavePath=init())
        Main.running = False
    
    def Lab_Mesh(self):
        stl_mesh = mesh.Mesh.from_file('./icon/probe.stl')
        points = stl_mesh.points.reshape(-1,3)
        faces = numpy.arange(points.shape[0]).reshape(-1,3)
        mesh_data = gl.MeshData(vertexes=points,faces=faces)
        Main.meshs = gl.GLMeshItem(meshdata=mesh_data,smooth=True,drawFaces=False,drawEdges=True,edgeColor=(0,1,0,1))
        Main.canvas.addItem(Main.meshs)
        
    def canvas_grid(self):
        Main.canvas.opts['distance'] = 10000
        Main.canvas.setWindowTitle('Title')
        Main.scatter = gl.GLScatterPlotItem(color = (255, 0, 0, 255) )
        Main.quad = gl.GLBoxItem(color = (255,255,255,255))
        Main.quad.setSize(150, 150, 150)
        Main.canvas.addItem(Main.quad)
        Main.canvas.addItem(Main.scatter)
        
        ### grid
        pts1 = numpy.array([[-10000, 0, 0], [10000, 0, 0]])
        xgrid = gl.GLLinePlotItem(pos=pts1, color=(10, 0.0, 0.0, 1.0), width=3, antialias=True)
        pts2 = numpy.array([[0, -10000, 0], [0, 10000, 0]])
        ygrid = gl.GLLinePlotItem(pos=pts2, color=(0, 1.0, 0.0, 1.0), width=3, antialias=True)
        pts3 = numpy.array([[0, 0, 0], [0, 0, 10000]])
        zgrid = gl.GLLinePlotItem(pos=pts3, color=(0, 0.0, 1.0, 1.0), width=3, antialias=True)
        Main.canvas.addItem(xgrid)
        Main.canvas.addItem(ygrid)
        Main.canvas.addItem(zgrid)
        
        ### safety
        Main.safety_quad = gl.GLBoxItem(color = (0,255,0,120))
        Main.safety_quad.setSize(4000, 4000, 3000)
        Main.canvas.addItem(Main.safety_quad)
        Main.safety_quad.translate(0,-2000,0)
        
        
    
if __name__=="__main__":
    app =  QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())