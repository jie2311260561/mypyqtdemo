import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()#界面绘制交给InitUI方法

    def initUI(self):
        #设置窗口大小和位置
        self.setGeometry(300,300,300,220)
        #设置窗口标题
        self.setWindowTitle("Icon")
        #设置窗口图标
        self.setWindowIcon(QIcon('web.png'))

        #显示窗口
        self.show()

if __name__ == '__main__':
    #创建应用程熙类
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())