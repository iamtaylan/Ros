#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kameraVeri.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtQuickWidgets import *
from PyQt5.QtCore import *
import sys
import cv2
import numpy as np
import rospy
from ucgen_cizdirme.msg import KameraVeri, Rotate, Vector3, Laser
from cv_bridge import CvBridge

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 720)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ustFrame = QtWidgets.QFrame(self.centralwidget)
        self.ustFrame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.ustFrame.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.ustFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ustFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ustFrame.setObjectName("ustFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ustFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ustMenuSolFrame = QtWidgets.QFrame(self.ustFrame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ustMenuSolFrame.setFont(font)
        self.ustMenuSolFrame.setStyleSheet("color:black;\n"
"border:none")
        self.ustMenuSolFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ustMenuSolFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ustMenuSolFrame.setObjectName("ustMenuSolFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ustMenuSolFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.versionLabel = QtWidgets.QLabel(self.ustMenuSolFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.versionLabel.setFont(font)
        self.versionLabel.setObjectName("versionLabel")
        self.gridLayout_4.addWidget(self.versionLabel, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout_3.addWidget(self.ustMenuSolFrame, 0, 0, 1, 1)
        self.ustMenuSagFrame = QtWidgets.QFrame(self.ustFrame)
        self.ustMenuSagFrame.setStyleSheet("border:none;")
        self.ustMenuSagFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ustMenuSagFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ustMenuSagFrame.setObjectName("ustMenuSagFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ustMenuSagFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.indirButon = QtWidgets.QPushButton(self.ustMenuSagFrame)
        self.indirButon.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.indirButon.setFont(font)
        self.indirButon.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 189, 182);\n"
"    color:black;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(52, 52, 52);\n"
"    color:black;\n"
"}\n"
"")
        self.indirButon.setObjectName("indirButon")
        self.horizontalLayout_3.addWidget(self.indirButon)
        self.bkButon = QtWidgets.QPushButton(self.ustMenuSagFrame)
        self.bkButon.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bkButon.setFont(font)
        self.bkButon.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 189, 182);\n"
"    color:black;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(52, 52, 52);\n"
"    color:black;\n"
"}\n"
"")
        self.bkButon.setObjectName("bkButon")
        self.horizontalLayout_3.addWidget(self.bkButon)
        self.kapatButon = QtWidgets.QPushButton(self.ustMenuSagFrame)
        self.kapatButon.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.kapatButon.setFont(font)
        self.kapatButon.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 189, 182);\n"
"    color:black;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(52, 52, 52);\n"
"    color:black;\n"
"}\n"
"")
        self.kapatButon.setObjectName("kapatButon")
        self.horizontalLayout_3.addWidget(self.kapatButon)
        self.gridLayout_3.addWidget(self.ustMenuSagFrame, 0, 2, 1, 1)
        self.ustMenuOrtaFrame = QtWidgets.QFrame(self.ustFrame)
        self.ustMenuOrtaFrame.setStyleSheet("border:none;")
        self.ustMenuOrtaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ustMenuOrtaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ustMenuOrtaFrame.setObjectName("ustMenuOrtaFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.ustMenuOrtaFrame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.TetraLabel = QtWidgets.QLabel(self.ustMenuOrtaFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TetraLabel.setFont(font)
        self.TetraLabel.setStyleSheet("color:black")
        self.TetraLabel.setObjectName("TetraLabel")
        self.gridLayout_5.addWidget(self.TetraLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_3.addWidget(self.ustMenuOrtaFrame, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.ustFrame)
        self.ortaFrame = QtWidgets.QFrame(self.centralwidget)
        self.ortaFrame.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(240, 235, 206);")
        self.ortaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ortaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ortaFrame.setObjectName("ortaFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.ortaFrame)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.ortaSagFrame = QtWidgets.QFrame(self.ortaFrame)
        self.ortaSagFrame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ortaSagFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ortaSagFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ortaSagFrame.setObjectName("ortaSagFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ortaSagFrame)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.solUstFrame = QtWidgets.QFrame(self.ortaSagFrame)
        self.solUstFrame.setStyleSheet("border-radius:12px;\n"
"background-color: qlineargradient(spread:pad, x1:0.532801, y1:0.0113636, x2:0.507, y2:0.994, stop:0 rgba(142, 139, 130, 255), stop:1 rgba(52, 52, 52, 255));")
        self.solUstFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.solUstFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.solUstFrame.setObjectName("solUstFrame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.solUstFrame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Kamera1 = QtWidgets.QLabel(self.solUstFrame)
        self.Kamera1.setStyleSheet("background-color:none;")
        self.Kamera1.setText("")
        self.Kamera1.setObjectName("Kamera1")
        self.gridLayout_6.addWidget(self.Kamera1, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.solUstFrame, 0, 0, 1, 1)
        self.ortaUstFrame = QtWidgets.QFrame(self.ortaSagFrame)
        self.ortaUstFrame.setStyleSheet("border-radius:12px;\n"
"background-color: qlineargradient(spread:pad, x1:0.532801, y1:0.0113636, x2:0.507, y2:0.994, stop:0 rgba(142, 139, 130, 255), stop:1 rgba(52, 52, 52, 255));")
        self.ortaUstFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ortaUstFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ortaUstFrame.setObjectName("ortaUstFrame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.ortaUstFrame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Kamera2 = QtWidgets.QLabel(self.ortaUstFrame)
        self.Kamera2.setStyleSheet("background-color:none;")
        self.Kamera2.setText("")
        self.Kamera2.setObjectName("Kamera2")
        self.gridLayout_7.addWidget(self.Kamera2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.ortaUstFrame, 0, 1, 1, 1)
        self.solAltFrame = QtWidgets.QFrame(self.ortaSagFrame)
        self.solAltFrame.setStyleSheet("border-radius:12px;\n"
"background-color: qlineargradient(spread:pad, x1:0.532801, y1:0.0113636, x2:0.507, y2:0.994, stop:0 rgba(142, 139, 130, 255), stop:1 rgba(52, 52, 52, 255));")
        self.solAltFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.solAltFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.solAltFrame.setObjectName("solAltFrame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.solAltFrame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_2.addWidget(self.solAltFrame, 1, 0, 1, 1)
        self.sagUstFrame = QtWidgets.QFrame(self.ortaSagFrame)
        self.sagUstFrame.setStyleSheet("border-radius:12px;\n"
"background-color: qlineargradient(spread:pad, x1:0.532801, y1:0.0113636, x2:0.507, y2:0.994, stop:0 rgba(142, 139, 130, 255), stop:1 rgba(52, 52, 52, 255));")
        self.sagUstFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sagUstFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sagUstFrame.setObjectName("sagUstFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sagUstFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Kamera3 = QtWidgets.QLabel(self.sagUstFrame)
        self.Kamera3.setStyleSheet("background-color:none;")
        self.Kamera3.setText("")
        self.Kamera3.setObjectName("Kamera3")
        self.horizontalLayout.addWidget(self.Kamera3)
        self.gridLayout_2.addWidget(self.sagUstFrame, 0, 2, 1, 1)
        self.sagAltFrame = QtWidgets.QFrame(self.ortaSagFrame)
        self.sagAltFrame.setStyleSheet("border-radius:12px;\n"
"background-color: qlineargradient(spread:pad, x1:0.532801, y1:0.0113636, x2:0.507, y2:0.994, stop:0 rgba(142, 139, 130, 255), stop:1 rgba(52, 52, 52, 255));")
        self.sagAltFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sagAltFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sagAltFrame.setObjectName("sagAltFrame")
        self.gridLayout_2.addWidget(self.sagAltFrame, 1, 2, 1, 1)
        self.ortaAltFrame = QtWidgets.QFrame(self.ortaSagFrame)
        self.ortaAltFrame.setStyleSheet("border-radius:12px;\n"
"background-color: qlineargradient(spread:pad, x1:0.532801, y1:0.0113636, x2:0.507, y2:0.994, stop:0 rgba(142, 139, 130, 255), stop:1 rgba(52, 52, 52, 255));")
        self.ortaAltFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ortaAltFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ortaAltFrame.setObjectName("ortaAltFrame")
        self.gridLayout_2.addWidget(self.ortaAltFrame, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.ortaSagFrame, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.ortaFrame)
        self.altFrame = QtWidgets.QFrame(self.centralwidget)
        self.altFrame.setMinimumSize(QtCore.QSize(0, 70))
        self.altFrame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.altFrame.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.altFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.altFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.altFrame.setObjectName("altFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.altFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.altOrtaFrame = QtWidgets.QFrame(self.altFrame)
        self.altOrtaFrame.setStyleSheet("border-radius:6px;\n"
"background-color: qlineargradient(spread:pad, x1:0.532801, y1:0.0113636, x2:0.507, y2:0.994, stop:0 rgba(142, 139, 130, 255), stop:1 rgba(52, 52, 52, 255));\n"
"color: rgb(211, 215, 207);")
        self.altOrtaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.altOrtaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.altOrtaFrame.setObjectName("altOrtaFrame")
        self.BataryaLabel = QtWidgets.QLabel(self.altOrtaFrame)
        self.BataryaLabel.setGeometry(QtCore.QRect(70, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.BataryaLabel.setFont(font)
        self.BataryaLabel.setStyleSheet("background-color:none;")
        self.BataryaLabel.setObjectName("BataryaLabel")
        self.bataryaLineEdit = QtWidgets.QLineEdit(self.altOrtaFrame)
        self.bataryaLineEdit.setGeometry(QtCore.QRect(200, 10, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bataryaLineEdit.setFont(font)
        self.bataryaLineEdit.setStyleSheet("")
        self.bataryaLineEdit.setObjectName("bataryaLineEdit")
        self.horizontalLayout_2.addWidget(self.altOrtaFrame)
        self.altSagFrame = QtWidgets.QFrame(self.altFrame)
        self.altSagFrame.setStyleSheet("border-radius:6px;\n"
"background-color: qlineargradient(spread:pad, x1:0.532801, y1:0.0113636, x2:0.507, y2:0.994, stop:0 rgba(142, 139, 130, 255), stop:1 rgba(52, 52, 52, 255));\n"
"color: rgb(211, 215, 207);")
        self.altSagFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.altSagFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.altSagFrame.setObjectName("altSagFrame")
        self.ModLabel = QtWidgets.QLabel(self.altSagFrame)
        self.ModLabel.setGeometry(QtCore.QRect(50, 10, 67, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ModLabel.setFont(font)
        self.ModLabel.setStyleSheet("background-color:none;")
        self.ModLabel.setObjectName("ModLabel")
        self.ModLineEdit = QtWidgets.QLineEdit(self.altSagFrame)
        self.ModLineEdit.setGeometry(QtCore.QRect(150, 10, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ModLineEdit.setFont(font)
        self.ModLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ModLineEdit.setObjectName("ModLineEdit")
        self.horizontalLayout_2.addWidget(self.altSagFrame)
        self.frame = QtWidgets.QFrame(self.altFrame)
        self.frame.setMaximumSize(QtCore.QSize(20, 20))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.altFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.versionLabel.setText(_translate("MainWindow", "V1.0.0"))
        self.indirButon.setText(_translate("MainWindow", "İNDİR"))
        self.bkButon.setText(_translate("MainWindow", "B/K"))
        self.kapatButon.setText(_translate("MainWindow", "KAPAT"))
        self.TetraLabel.setText(_translate("MainWindow", "TETRA"))
        self.BataryaLabel.setText(_translate("MainWindow", "BATARYA"))
        self.bataryaLineEdit.setText(_translate("MainWindow", "             N/A"))
        self.ModLabel.setText(_translate("MainWindow", "MOD"))
        self.ModLineEdit.setText(_translate("MainWindow", "N/A"))

        self.kapatButon.clicked.connect(self.close) 
        self.indirButon.clicked.connect(self.minimize)
        self.bkButon.clicked.connect(self.maximize)

        """
        self.timer = QTimer(MainWindow)
        self.timer.timeout.connect(self.cameraCallback)
        self.timer.start(1)  # Görüntüyü güncellemek için bir zamanlayıcı başlattık her 1 milisaniyede bir güncellenicek
        """

        #Pencere Boyutlandırma
        QSizeGrip(self.frame)


        # Düğümüzü oluşturduk ve konularımıza Sub ve Pub olduk
        rospy.init_node("nesne_tespiti") 
        self.pub=rospy.Publisher("cmd_vel",Rotate,queue_size=10)
        rospy.Subscriber("camera/rgb/image_raw",KameraVeri ,self.cameraCallback)
        rospy.Subscriber("scan",Laser,callback=self.laserCallback)
        rospy.Subscriber("hiz_topic",Vector3 ,self.VelCallBack)

        self.hiz_mesaji=Rotate()
        self.cv_bridge=CvBridge()
        
        self.hiz_mesaji.linear.x = 0.0
        self.min_on=0
        rospy.spin()

    # Kameradan görüntü alma, görüntüyü işleme ve robotu hareket ettirme gibi görevleri yaptığımız fonksiyon
    def cameraCallback(self, data):

        image=self.cv_bridge.imgmsg_to_cv2(data,"bgr8")

        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        lower_gray=np.array([30],dtype="uint8")
        upper_gray=np.array([150],dtype="uint8")
        mask=cv2.inRange(gray,lower_gray,upper_gray)
        self.current_image = image

        new_height = 330
        new_width = 330

        # Görüntüyü yeniden boyutlandırdık
        resized_image = cv2.resize(image, (new_width, new_height))
        resized_image2 = cv2.resize(gray, (new_width, new_height))
        resized_image3 = cv2.resize(mask, (new_width, new_height))

        self.camera = KameraVeri()
        self.camera_publisher = rospy.Publisher("qt", KameraVeri, queue_size=100)

        # self.combined_image = cv2.vconcat([resized_image, resized_image2, resized_image3])

        self.camera.height = 330
        self.camera.width = 990
        self.camera.data = resized_image3

        self.camera_publisher.publish(self.camera)

        # Yeniden boyutlandırılmış görüntüyü QImage'e dönüştürdük
        height, width, channel = resized_image.shape
        bytes_per_line = 3 * width
        q_img = QImage(resized_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        height, width = resized_image2.shape
        bytes_per_line = 3 * width
        q_img2 = QImage(resized_image2.data, width, height, bytes_per_line, QImage.Format_RGB888)

        height, width = resized_image3.shape
        bytes_per_line = 3 * width
        q_img3 = QImage(resized_image3.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # QLabel içerisine görüntüleri aktardık
        self.Kamera1.setPixmap(QPixmap.fromImage(q_img))
        self.Kamera2.setPixmap(QPixmap.fromImage(q_img2))
        self.Kamera3.setPixmap(QPixmap.fromImage(q_img3))

        h,w,c=image.shape
        M=cv2.moments(mask)
        
        # Eğer karşısında bir nesne varsa kullanıcıdan aldığımız hızla nesneye doğru yaklaşıcak
        if M['m00']>0:
                M=cv2.moments(mask)
                x=int(M['m10']/M['m00'])
                y=int(M['m01']/M['m00'])
                
                sapma=x-w/2

                if self.min_on>1.0:
                        self.hiz_mesaji.linear.x=0.0
                        self.hiz_mesaji.angular.z=-sapma/100
                        self.pub.publish(self.hiz_mesaji)

                elif self.min_on<1.0:
                        self.hiz_mesaji.linear.x=0.0
                        self.hiz_mesaji.angular.z=0.0
                        self.pub.publish(self.hiz_mesaji)
                
                # Ekrana bir yeşil nokta çizdik bu şeklimizin ağırlık merkezinde oluşucak
                cv2.circle(image,(x,y),5,(0,255,0),-1)

        # Eğer karşısında bir nesne yoksa 0.5lik bir hızla etrafında dönücek                
        elif M['m00']==0 or M['m00']<0:
                self.hiz_mesaji.linear.x=0.0
                self.hiz_mesaji.linear.z=0.0
                self.hiz_mesaji.angular.z=0.5
                self.pub.publish(self.hiz_mesaji)
        
        cv2.imshow("image",image)
        cv2.imshow("gray_image",mask)


        cv2.waitKey(1)

    # Lidardan verilerimizi aldığımız fonksiyon
    def laserCallback(self,request):

        # Lidar sensörümüzün çalışma aralıklarını belirledik
        sol_on = list(request.ranges[0:9])
        sag_on = list(request.ranges[350:359])
        on = sol_on + sag_on
        sol = list(request.ranges[80:100])
        sag = list(request.ranges[260:280])
        arka = list(request.ranges[170:190])

        # Sensör verileini yazdırdık.
        min_on = min(on)
        min_sol = min(sol)
        min_sag = min(sag)
        min_arka = min(arka)
        print(min_on,min_sol,min_sag,min_arka)
        
    # Publisherımızdan gelen hız mesajını aldığımız fonksiyon.
    def VelCallBack(self, hiz_mesaj):
        rospy.loginfo("Hiz: %s" %hiz_mesaj.x)
        self.hiz_mesaji.linear.x = hiz_mesaj.x
        

    #Kapatma fonksiyonu
    def close(self):
        quit()

    #Küçültme fonksiyonu
    def minimize(self):
        MainWindow.showMinimized()

    #Büyültme fonksiyonu
    def maximize(self):
        if MainWindow.isMaximized():
            MainWindow.showNormal()
        else:
            MainWindow.isMaximized()

    #Pencereyi hareket ettirme fonksiyonları
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
