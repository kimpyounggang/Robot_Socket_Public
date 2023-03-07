import pyqtgraph as pg
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)

        # Generate some data
        x = np.random.normal(size=100000)
        y = np.random.normal(size=100000)
        pos = np.column_stack((x, y))

        # Create scatter plot item
        scatter = pg.ScatterPlotItem(pos=pos, brush=pg.mkBrush(255, 255, 255, 120),
                                     pen=pg.mkPen(None), size=10, pxMode=True)

        # Set up the plot widget
        self.plot_widget.setRenderHint(QtGui.QPainter.Antialiasing)
        self.plot_widget.setAntialiasing(True)
        self.plot_widget.addItem(scatter)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
