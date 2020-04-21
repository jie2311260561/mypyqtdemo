import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, 
    QPushButton, QApplication)
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        #创建网格按钮
        grid = QGridLayout()
        self.setLayout(grid)
        #创建实例
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        #设置按钮标签
        positions = [(i,j) for i in range(5) for j in range(4)] #产生二维列表
        #创建网格的位置列表
        for position, name in zip(positions, names):
            
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            #创建按钮并使用addWidget()方法添加到布局中

        self.move(300, 150)
        self.setWindowTitle('网格')
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())