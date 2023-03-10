from PyQt6.QtCore import QSize, Qt, QPropertyAnimation, QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel
from PyQt6.QtGui import QPainter, QColor, QFont, QPixmap, QPen, QBrush
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
from time import sleep

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Metronome")
        self.resize(800, 700)
        #self.setCentralWidget

        self.label = QLabel()
        canvas = QPixmap(800, 690)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.show()
        self.draw_lines()

        for i in range(7):
            self.draw_ball(i)

    def draw_lines(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(QColor('black'))
        painter.setPen(pen)
        painter.drawLine(50, 200, 400, 550)
        painter.drawLine(400, 550, 750, 200)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_ball(self,i):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('0900ff'))
        D=20
        R=int(D/2)
        painter.drawEllipse(400-R, 150+2*D*i, D, D)
        painter.end()
        self.label.setPixmap(canvas)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()

if __name__ == "__main__" :
    main()