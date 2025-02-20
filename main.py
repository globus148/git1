import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor
from ui_form import Ui_MainWindow


class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Загружаем интерфейс из ui_form.py
        self.pushButton.clicked.connect(self.paint_circle)
        self.should_paint = False

    def paint_circle(self):
        self.should_paint = True
        self.update()  # Перерисовываем окно

    def paintEvent(self, event):
        if self.should_paint:
            painter = QPainter(self)

            # Случайный цвет
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            painter.setBrush(color)

            # Случайный размер и позиция окружности
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
