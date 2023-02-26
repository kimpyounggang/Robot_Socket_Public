from pyqtgraph import QtCore,QtGui
import pyqtgraph.opengl as gl
import numpy as np
import sys

app = QtGui.QApplication([])
w = gl.GLViewWidget()
# w.opts['distance']=20
w.show()
w.setWindowTitle('pyqtgraph')
g = gl.GLGridItem()
w.addItem(g)
spl = gl.GLScatterPlotItem(pos = (1,1,1))
w.addItem(spl)

QtGui.QApplication.instance().exec_()