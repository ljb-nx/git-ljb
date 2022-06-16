import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,  QTextEdit, QGridLayout, QApplication,QPushButton)
class Winform(QWidget):
  def __init__(self,parent=None):
    super(Winform,self).__init__(parent)
    self.initUI()
  def initUI(self):
    titleLabel = QLabel('标题')
    authorLabel = QLabel('提交人')
    contentLabel = QLabel('申告内容')
    titleEdit = QLineEdit()
    authorEdit = QLineEdit()
    contentEdit = QTextEdit()
    button = QPushButton("关  闭")

    grid = QGridLayout()
    grid.setSpacing(10)
    grid.addWidget(titleLabel, 1, 0)
    grid.addWidget(titleEdit, 1, 1)
    grid.addWidget(authorLabel, 2, 0)
    grid.addWidget(authorEdit, 2, 1)
    grid.addWidget(contentLabel, 3, 0)
    grid.addWidget(contentEdit, 3, 1, 5, 1)
    grid.addWidget(button,8,1)
    text2 = contentEdit.toPlainText()
    text1 = str(text2)

    #contentEdit.textChanged(self.show_xx(text1))
    button.clicked.connect(self.show_xx('text1'))

    self.setLayout(grid)
    self.setGeometry(300, 300, 350, 300)
    self.setWindowTitle('故障申告')

  def show_xx(self,text):
    #neirong = winform.contentEdit.toPlainText()
    #biaoti = titleEdit.text()
    #QMessageBox.information(self, biaoti, neirong, QMessageBox.ok)
    print(f'neirong is {text}')
    #print("good connect")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())