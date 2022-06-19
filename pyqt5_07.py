#!/usr/bin/python3
#  coding:utf-8


'''
color = QColorDialog.getColor() # 颜色对话框（十六进制的值会保存在color变量中）
if color.isValid(): # 判断color是否有效
	self.text_edit.setTextColor(color)

font, ok = QFontDialog.getFont() # 字体对话框
if ok:
	self.text_edit.setFont(font)
'''
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QMessageBox, QInputDialog,QApplication, QHBoxLayout
import sys


class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("信号和槽传递额外参数例子")
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')

        button1.clicked.connect(lambda: self.onButtonClick(1))
        button2.clicked.connect(lambda: self.onButtonClick(2))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self, n):
        #print('Button {0} 被按下了'.format(n))

        print(f'Button {n}被按下了')
        #QMessageBox.information(self, "信息提示框", 'Button {0} clicked'.format(n))
        content, ok = QInputDialog.getText(self, 'title', '')
        if ok:
            #print(f'content is {content}')
            QMessageBox.information(self, "信息提示框", f'content is {content}')
        else:
            #print('没有输入内容！')
             QMessageBox.information(self, "信息提示框", '没有输入内容！')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
