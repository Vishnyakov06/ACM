import numpy as np
import matplotlib.pyplot as plt
import math
global_context = {
    'cos': math.cos,
    'sin': math.sin,
    'tan': math.tan,
    'sqrt': math.sqrt,
    'exp': math.exp,
    'log': math.log,
    'pi': math.pi,
    'e': math.e,
}
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 868)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 610, 161, 121))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(125, 123, 121);\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(270, 70, 321, 141))
        self.lineEdit1.setObjectName("lineEdit1")
        self.label1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 20, 261, 261))
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("../Downloads/bpVSvVqzpFY.png"))
        self.label1.setObjectName("label1")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 280, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 0, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 510, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 430, 191, 71))
        self.label_2.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 30, 301, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Downloads/Screenshot_3.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1106, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Вычислить!"))
        self.label_2.setText(_translate("MainWindow", "Epsilon"))

    def add_functions(self):
        #self.pushButton.clicked.connect(lambda:self.chet(self.pushButton.text()))
        self.pushButton.clicked.connect(self.chet)
    def chet(self):
        def left_rectangle_rule(f, a, b, n):
            h = (b - a) / n
            integral = 0.0
            for i in range(n):
                integral += example_function(a + i * h)
            return integral * h

        def right_rectangle_rule(f, a, b, n):
            h = (b - a) / n
            integral = 0.0
            for i in range(n):
                integral += example_function(a + (i + 1) * h)
            return integral * h

        def runge_rule(f, a, b, epsilon, n):
            integral_old = left_rectangle_rule(f, a, b, n)
            while True:
                n *= 2
                integral_new = left_rectangle_rule(f, a, b, n)
                error_estimate = abs(integral_new - integral_old)
                if error_estimate < epsilon:
                    break
                integral_old = integral_new
            return integral_new, n, (b - a) / n

        def example_function(x):
            return eval(self.lineEdit1.text(), {"__builtins__": None, 'x': x}, global_context)

        a = eval(self.lineEdit_2.text())
        b = eval(self.lineEdit_3.text())
        epsilon = eval(self.lineEdit_4.text())
        eps = math.sqrt(math.sqrt(epsilon))
        n = math.ceil((b - a) / eps)
        integral_value, num_partitions, h = runge_rule(example_function, a, b, epsilon, n)
        print(f"Значение интеграла: {integral_value:.6f}")
        print(f"Количество разбиений: {num_partitions}")
        print(f"Шаг: {h:.6f}")
        x_values = np.linspace(a, b, num_partitions)
        y_values = [example_function(x) for x in x_values]
        fig, ax = plt.subplots()
        ax.plot(x_values, y_values, label=f'f(x) = {self.lineEdit1.text()}')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('График функции')
        ax.legend()
        plt.grid()
        plt.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
