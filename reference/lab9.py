import pyqtgraph.opengl as gl
import numpy as np
from pyqtgraph.Qt import QtCore, QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.plot_widget = gl.GLViewWidget()
        self.setCentralWidget(self.plot_widget)

        # Generate some data
        x = np.random.normal(size=100000)
        y = np.random.normal(size=100000)
        z = np.random.normal(size=100000)
        pos = np.column_stack((x, y, z))

        # Create scatter plot item
        scatter = gl.GLScatterPlotItem(pos=pos, color=(1.0, 1.0, 1.0, 1.0), size=10)

        # Set up the plot widget
        self.plot_widget.addItem(scatter)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
