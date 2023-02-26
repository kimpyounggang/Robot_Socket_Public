import sys
from PyQt5 import QtWidgets,QtGui,QtCore

if __name__ == '__main__':
    app =QtWidgets.QApplication(sys.argv)

    form = QtWidgets.QWidget()

    spin = QtWidgets.QSpinBox()
    spin.setRange(0,100)

    slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
    slider.setRange(-180,180)
    
    slider1 = QtWidgets.QSlider(QtCore.Qt.Vertical)
    slider1.setRange(0,100)

    progressBar = QtWidgets.QProgressBar()
    progressBar.setAlignment(QtCore.Qt.AlignCenter)
    progressBar.setRange(0,100)

    spin.valueChanged.connect(slider.setValue)    # valuChanged(int), setValue(int)
    slider.valueChanged.connect(spin.setValue)
    
    spin.valueChanged.connect(progressBar.setValue)

    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(spin)
    layout.addWidget(slider)
    layout.addWidget(slider1)
    layout.addWidget(progressBar)


    form.setLayout(layout)
    form.setWindowTitle('SpinSliderProgressDemo')

    form.show()
    app.exec_()