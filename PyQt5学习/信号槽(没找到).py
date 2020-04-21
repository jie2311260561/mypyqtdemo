import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QVBoxLayout, QApplication)
class Example(QWidget):
        
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        # QtGui.QLCDNumber
        lcd = QLCDNumber(self)
        # QtGui.QSlider
        sld = QSlider(Qt.Horizontal, self)
 
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
#  sender是接收信号的对象
        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display) #slot 插槽 是对信号做出反应的方法
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())