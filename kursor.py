import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint_circle)
        self.should_paint = False

    def paint_circle(self):
        self.should_paint = True
        self.update()

    def paintEvent(self, event):
        if self.should_paint:
            painter = QPainter(self)
            painter.setBrush(QColor("yellow"))
            diameter = random.randint(30, 150)
            x = random.randint(50, self.width() - diameter - 50)
            y = random.randint(100, self.height() - diameter - 50)
            painter.drawEllipse(x, y, diameter, diameter)
            self.should_paint = False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
