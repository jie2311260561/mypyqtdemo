import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from mypyqtdemo.音乐播放器.untitled import Ui_MainWindow


class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(MyWindow,self).__init__(parent)
        self.setupUi(self)
        self.end_Btn.clicked.connect(self.end_event)

    def end_event(self):
        if self.name_Edit.text == "":
            QMessageBox.about(self,"登录","请输入姓名")
        elif self.pass_Edit.text() == "":
            QMessageBox.about(self, '登陆', '请输入密码')
        else:
            QMessageBox.about(self, '登陆', self.name_Edit.text() + ' 欢迎登陆')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())