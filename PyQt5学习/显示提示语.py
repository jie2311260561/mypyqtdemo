import sys
from PyQt5.QtWidgets import (QWidget,QToolTip,QPushButton,QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self, ):
        super().__init__()

        self.initUI()

    def initUI(self):
        #这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('sansSerif',10))

        #创建一个提示 我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a <b> QPushButton</b> widget')

        #创建一个pushbutton 为它设置一个 tooltip
        btn = QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        #bth.sizeHint(设设置默认尺寸)
        btn.resize(btn.sizeHint())

        #移动窗口的位置
        btn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())