from PyQt6.QtWidgets import QApplication, QMainWindow
from sudoku import *
from sudoko_main import *
import sys
from time import sleep

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window,self).__init__(parent)
        self.ui = Ui_Sudoku()
        self.ui.setupUi(self)
        self.increase = 81 / 100
        self.text = "0"

        self.red = "background-color: rgb(237, 51, 59);"
        self.yellow = "background-color: rgb(249, 240, 107);"
        self.green = "background-color: rgb(66, 154, 53);"
        self.numColor = "background-color: rgb(255, 190, 111);"
        self.blue = "background-color: rgb(98, 160, 234);"

        self.progress = self.numberof() * self.increase
        self.ui.progressBar.setValue(int(self.numberof() * self.increase))
        self.ui.btn_0_0.clicked.connect(self.btn0pressed)
        self.ui.btn_0_1.clicked.connect(self.btn1pressed)
        self.ui.btn_dig_1.clicked.connect(self.num1P)
        self.ui.btn_dig_2.clicked.connect(self.num2P)
        self.ui.btn_dig_3.clicked.connect(self.num3P)
        self.ui.btn_dig_4.clicked.connect(self.num4P)
        self.ui.btn_dig_5.clicked.connect(self.num5P)
        self.ui.btn_dig_6.clicked.connect(self.num6P)
        self.ui.btn_dig_7.clicked.connect(self.num7P)
        self.ui.btn_dig_8.clicked.connect(self.num8P)
        self.ui.btn_dig_9.clicked.connect(self.num9P)


    def num1P(self):
        self.text = self.ui.btn_dig_1.text()

    def num2P(self):
        self.text = self.ui.btn_dig_2.text()

    def num3P(self):
        self.text = self.ui.btn_dig_3.text()

    def num4P(self):
        self.text = self.ui.btn_dig_4.text()

    def num5P(self):
        self.text = self.ui.btn_dig_5.text()

    def num6P(self):
        self.text = self.ui.btn_dig_6.text()

    def num7P(self):
        self.text = self.ui.btn_dig_7.text()

    def num8P(self):
        self.text = self.ui.btn_dig_8.text()

    def num9P(self):
        self.text = self.ui.btn_dig_9.text()


    def increseProgress(self):
        self.progress += self.increase
        self.ui.progressBar.setValue(int(self.progress))

    def isRight(self, son, newqiymat):
        if solved_sudoko[son//9][son%9] == newqiymat:
            unsolve_sudoko[son//9][son%9] = newqiymat
            return True
        return False

    def make_num_color(self, color):
        self.ui.btn_dig_1.setStyleSheet(color)
        self.ui.btn_dig_2.setStyleSheet(color)
        self.ui.btn_dig_3.setStyleSheet(color)
        self.ui.btn_dig_4.setStyleSheet(color)
        self.ui.btn_dig_5.setStyleSheet(color)
        self.ui.btn_dig_6.setStyleSheet(color)
        self.ui.btn_dig_7.setStyleSheet(color)
        self.ui.btn_dig_8.setStyleSheet(color)
        self.ui.btn_dig_9.setStyleSheet(color)

    def btn0pressed(self):
        text = self.ui.btn_0_0.text()
        if text != str(solved_sudoko[0][0]):
            self.make_num_color(self.red)
            self.ui.btn_0_0.setStyleSheet(self.yellow)
            res = self.text
            self.ui.btn_0_0.setText(res)
            if self.ui.btn_0_0.text() == str(solved_sudoko[0][0]):
                unsolve_sudoko[0][0] = int(self.ui.btn_0_0.text())
                self.ui.btn_0_0.setStyleSheet(self.green)
                self.increseProgress()
                self.make_num_color(self.numColor)
            else:
                self.ui.btn_0_0.setStyleSheet(self.red)
        self.make_num_color(self.numColor)


    def btn1pressed(self):
        pass

    def numberof(self):
        t = 0
        for i in range(len(solved_sudoko)):
            for j in range(len(solved_sudoko)):
                if solved_sudoko[i][j] == unsolve_sudoko[i][j]:
                    t += 1
        return t

def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

