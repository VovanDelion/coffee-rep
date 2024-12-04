import sqlite3
import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QApplication, QPushButton, QLineEdit


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 600, 600)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.aaa = self.textEdit = QTextEdit(self)
        self.aaa.setGeometry(100, 100, 400, 400)
        self.but = QPushButton("Отобразить", self)
        self.but.clicked.connect(self.a)

    def a(self):
        self.cur.execute("SELECT * FROM coffee")
        res = ''.join(str(x) + "\n" for x in self.cur.fetchall())
        self.aaa.setText(res)
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_form = MainWin()
    my_form.show()
    sys.exit(app.exec())
