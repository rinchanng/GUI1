from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('打开文件对话框')
        layout = QVBoxLayout()
        self.button1 = QPushButton('加载图片')
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)

        # 将图片显示到一个label上
        self.imagelabel = QLabel()
        layout.addWidget(self.imagelabel)

        self.button2 = QPushButton('加载文本文件')
        self.button2.clicked.connect(self.loadFile)
        layout.addWidget(self.button2)
        # 使用QTextEdit控件显示文本
        self.te = QTextEdit()
        layout.addWidget(self.te)

        self.setLayout(layout)

    def loadImage(self):
        # 这种打开方式只能打开一个文件。第三个参数为路径，第四个选择打开文件类型。
        # 返回值有两个，第一个为文件名
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件 (*.jpg *.png)')
        # 给label设置打开的图片
        self.imagelabel.setPixmap(QPixmap(fname))

    def loadFile(self):
        # 使用另外一种方法打开
        dialog = QFileDialog()
        # 设置打开文件格式
        dialog.setFileMode(QFileDialog.AnyFile)  # anyfile可以打开任意文件
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            f = open(filenames[0], encoding='utf-8', mode='r')
            with f:
                data = f.read()
                self.te.setText(data)
        # 这样也可以！！！！！！！！！！！！！！！！
        # fname, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '文本 (*.py )')
        # f = open(fname, encoding='utf-8', mode='r')
        # with f:
        #     data = f.read()
        #     self.te.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())

