from PyQt6 import QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Случайные окружности")
        MainWindow.resize(600, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Кнопка для рисования окружностей
        self.pushButton = QtWidgets.QPushButton("Нарисовать", self.centralwidget)
        self.pushButton.setGeometry(250, 20, 100, 40)
