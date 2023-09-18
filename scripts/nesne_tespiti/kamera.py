
########################################################
#   TurtleBot3 kamera görüntüsünü PyQt5 ile gösterme   #
########################################################

import sys
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenCV ile Kamera Görüntüsü")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.image_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(100)  # Görüntüyü güncellemek için bir zamanlayıcı başlatın (örneğin, her 100 milisaniyede bir)

    def update_frame(self):
        # Kameradan anlık görüntü alın
        cap = cv2.VideoCapture(0)  # 0, birinci kamera demektir. Birden fazla kamera varsa ayarlarına göre değiştirin.
        ret, frame = cap.read()

        if ret:
            # OpenCV görüntüsünü QImage'e dönüştürün
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # QLabel içinde görüntüyü gösterin
            self.image_label.setPixmap(QPixmap.fromImage(q_img))
        else:
            self.image_label.setText("Kamera bağlantısı yok")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
