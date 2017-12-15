# Day_05_07_image_timer.py

import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow, QPushButton)

import numpy as np
import threading

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        self.label = QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        button = QPushButton('누르세요')
        button.clicked.connect(self.start)

        self.vbox = QVBoxLayout(self.widget)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(button)

        self.widget.setLayout(self.vbox)

    def draw(self):
        values = np.random.rand(100, 100)
        img = Image.fromarray(values, 'RGB')

        self.img = ImageQt(img)
        pixmap = QtGui.QPixmap.fromImage(self.img)
        self.label.setPixmap(pixmap)

        threading.Timer(0.1, ImageViewer.draw, args=[self]).start()

    def start(self):
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    viewer = ImageViewer()
    viewer.show()

    app.exec_()