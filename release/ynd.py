import sqlite3
import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QApplication, QPushButton, QLineEdit, QWidget, QLabel
from PyQt6.uic.uiparser import QtWidgets


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 600, 600)
        self.con = sqlite3.connect('data/coffee.sqlite')
        self.cur = self.con.cursor()
        self.aaa = self.textEdit = QTextEdit(self)
        self.aaa.setGeometry(100, 100, 400, 400)
        self.but = QPushButton("Отобразить", self)
        self.but.clicked.connect(self.a)
        self.but1 = QPushButton("Добавить или изменить", self)
        self.but1.clicked.connect(self.aa)
        self.but1.setGeometry(100, 0, 200, 50)

    def a(self):
        self.cur.execute("SELECT * FROM coffee")
        res = ''.join(str(x) + "\n" for x in self.cur.fetchall())
        self.aaa.setText(res)
        self.con.close()

    def aa(self):
        self.ex = Remake()
        self.ex.show()
        self.close()

class Remake(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 600, 600)
        self.l = QLabel(self)
        self.l.setText("Внесите изменения:\n(напишете на языке sqlite3)")
        self.l.move(10, 10)
        self.inp = self.textEdit = QTextEdit(self)
        self.inp.setGeometry(100, 100, 400, 200)
        self.but2 = QPushButton("Изменить", self)
        self.but2.setGeometry(0, 300, 200, 50)
        self.but2.clicked.connect(self.rem)


    def rem(self):
        self.con = sqlite3.connect("data/coffee.sqlite")
        self.cur = self.con.cursor()
        self.cur.execute(self.inp.toPlainText())
        self.con.commit()
        self.con.close()
        self.ex = MainWin()
        self.ex.show()
        self.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_form = MainWin()
    my_form.show()
    sys.exit(app.exec())
