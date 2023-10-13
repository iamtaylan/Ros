#!/usr/lib python3
# -*- coding: utf-8 -*-


import sys
import time
from PyQt5.QtCore import QProcess
from PyQt5.QtWidgets import QApplication, QWidget

class Example(QWidget):

    def _init_(self):
        super().__init__()

        # Terminalde bir komut çalıştır
        self.process = QProcess()
        self.process.start("rviz")

        # Komutun çıktısını oku
        self.process.readyReadStandardOutput.connect(self.on_output)

        # Komutun tamamlanmasını bekle
        self.process.waitForFinished()

    def on_output(self):
        output = self.process.readAllStandardOutput().data().decode()
        print(output)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())