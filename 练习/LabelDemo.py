import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5.QtGui import QPixmap,QPalette
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow> 这是一个文本本标签</fount>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        # label1
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用python  GUI程序</a>")
        label2.setAlignment(Qt.AlignCenter)

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("./ima"))

        label4.setText("<a href = 'https://www.bilibili.com/'>哔哩哔哩</a>")
     #   label4.setAlignment(Qt.AlignCenter)
        label4.setToolTip('这是一个超级链接')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered())
        label4.linkActivated.connect(self.linkClicked())

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')


    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标滑过label4时，触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())