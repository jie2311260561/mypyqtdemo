import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
 
 
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        #添加事件的实例
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')            #访问的快捷方式
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit) #点后调用quit退出程序

        exitTools = QAction(QIcon('exit.png'),'&hello',self)
        exitTools.setShortcut('Ctrl+W')
        exitTools.setStatusTip('Exit application')
        exitTools.triggered.connect(qApp.quit)
 
        self.statusBar()
 
        #创建一个菜单栏
        menubar = self.menuBar()
        #添加菜单
        fileMenu = menubar.addMenu('&File')
        toolMeny = menubar.addMenu('&tools')
        #添加事件
        fileMenu.addAction(exitAction) 
        toolMeny.addAction(exitTools)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  