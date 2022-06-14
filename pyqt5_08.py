#!/usr/bin/python3
# coding:utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QCheckBox, QComboBox,QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Exchange_of_weather_degree_units(QWidget):

 def __init__(self):
  super().__init__()
  self.setting()

 def setting(self):
  self.unit = None

  self.choice = QComboBox(self)
  self.choice.addItem('℃')
  self.choice.addItem('℉')
  self.choice.activated[str].connect(self.choice_)
  self.choice.move(50,15)

  self.number = QLineEdit(self)
  self.number.setPlaceholderText('输入转化的数值')
  self.number.move(15,50)

  self.arrowhead = QLabel(self)
  self.arrowhead.setText('—————>')
  self.arrowhead.setFont(QFont('microsoft Yahei', 20))
  self.arrowhead.move(165,20)

  self.result = QLabel(self)
  self.result.setText('       ')
  self.result.setFont(QFont('microsoft Yahei', 15))
  self.result.move(370, 27.5)

  self.yes = QPushButton('确定',self)
  self.yes.clicked.connect(self.yes_)
  self.yes.move(220,50)

  self.setGeometry(300, 100, 520, 100)
  self.setWindowTitle('摄氏度与华氏度的转换')
  self.show()

 def choice_(self,text):
  self.unit = text

 def yes_(self):
  try:
   if self.unit == '℃':
    result_ = eval(self.number.text()) * 1.8 + 32
    self.result.setText(str(result_) + '℉')

   if self.unit == '℉':
    result_ = round((eval(self.number.text()) - 32) / 1.8,6)
    self.result.setText(str(result_) + '℃')

   else:
    result_ = eval(self.number.text()) * 1.8 + 32
    self.result.setText(str(result_) + '℃')
  except:
   self.result.setText('请输入数字')


if __name__ == '__main__':
 app = QApplication(sys.argv)
 Ex = Exchange_of_weather_degree_units()
 sys.exit(app.exec_())