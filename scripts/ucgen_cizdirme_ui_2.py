#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ucgen_cizdirme_ui_2 import * 
import rospy
from geometry_msgs.msg import Twist
from math import radians
from ucgen_cizdirme.msg import Length

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"background-color: rgb(48, 48, 48);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ustMenuFrame = QtWidgets.QFrame(self.centralwidget)
        self.ustMenuFrame.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 5px;")
        self.ustMenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ustMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ustMenuFrame.setObjectName("ustMenuFrame")
        self.kenarUzunlukLineEdit = QtWidgets.QLineEdit(self.ustMenuFrame)
        self.kenarUzunlukLineEdit.setGeometry(QtCore.QRect(150, 90, 511, 31))
        self.kenarUzunlukLineEdit.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.kenarUzunlukLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.kenarUzunlukLineEdit.setObjectName("kenarUzunlukLineEdit")
        self.baslatButon = QtWidgets.QPushButton(self.ustMenuFrame)
        self.baslatButon.setGeometry(QtCore.QRect(550, 160, 89, 25))
        self.baslatButon.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.baslatButon.setObjectName("baslatButon")
        self.verticalLayout.addWidget(self.ustMenuFrame)
        self.altMenuFrame = QtWidgets.QFrame(self.centralwidget)
        self.altMenuFrame.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 10px\n"
"")
        self.altMenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.altMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.altMenuFrame.setObjectName("altMenuFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.altMenuFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.altSolFrame = QtWidgets.QFrame(self.altMenuFrame)
        self.altSolFrame.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.altSolFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.altSolFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.altSolFrame.setObjectName("altSolFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.altSolFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.hizLabel = QtWidgets.QLabel(self.altSolFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.hizLabel.setFont(font)
        self.hizLabel.setObjectName("hizLabel")
        self.gridLayout.addWidget(self.hizLabel, 0, 0, 1, 1)
        self.aciLabel = QtWidgets.QLabel(self.altSolFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.aciLabel.setFont(font)
        self.aciLabel.setObjectName("aciLabel")
        self.gridLayout.addWidget(self.aciLabel, 1, 0, 1, 1)
        self.hizGostergeLabel = QtWidgets.QLabel(self.altSolFrame)
        self.hizGostergeLabel.setObjectName("hizGostergeLabel")
        self.gridLayout.addWidget(self.hizGostergeLabel, 0, 1, 1, 1)
        self.aciGostergeLabel = QtWidgets.QLabel(self.altSolFrame)
        self.aciGostergeLabel.setObjectName("aciGostergeLabel")
        self.gridLayout.addWidget(self.aciGostergeLabel, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.altSolFrame)
        self.altSagFrame = QtWidgets.QFrame(self.altMenuFrame)
        self.altSagFrame.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.altSagFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.altSagFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.altSagFrame.setObjectName("altSagFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.altSagFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.altSagFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.altSagFrame)
        self.verticalLayout.addWidget(self.altMenuFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.kenarUzunlukLineEdit.setText(_translate("MainWindow", "Kenar uzunluğu giriniz: (örn: 2, 3)"))
        self.baslatButon.setText(_translate("MainWindow", "Başlat"))
        self.hizLabel.setText(_translate("MainWindow", "HIZ:"))
        self.aciLabel.setText(_translate("MainWindow", "AÇI:"))
        self.hizGostergeLabel.setText(_translate("MainWindow", "N/A"))
        self.aciGostergeLabel.setText(_translate("MainWindow", "N/A"))
        self.label.setText(_translate("MainWindow", "Komut Bekleniyor.."))
        """
        rospy.init_node('draw_triangle_node', anonymous=True)
        vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber("kenar_topic", Length, self.lengthFunction)
        rate = rospy.Rate(10)  

        vel_msg = Twist()

        self.kenar_uzunlugu = 0.0  
        angle = 120.0     


        # for oluşturup kenar sayısı kadar forun dönmesini sağladık böylece üçgen elde edebileceğiz.
        for i in range(3):

            # 120* döndürdük
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = radians(angle) 
            vel_publisher.publish(vel_msg)
            rospy.sleep(1.0)  

            # dur
            vel_msg.angular.z = 0.0
            vel_publisher.publish(vel_msg)
            rospy.sleep(1.0)  

            # ilerle
            vel_msg.linear.x = 0.2  
            vel_msg.angular.z = 0.0
            vel_publisher.publish(vel_msg)
            rospy.sleep(self.kenar_uzunlugu / 0.2)  # T=X/V formülü ile turtlebot3'ün ne kadar süre gitmesi gerektiğini hesapladık ve bu süre bittiği anda durdurduk

            # dur
            vel_msg.linear.x = 0.0
            vel_publisher.publish(vel_msg)
            rospy.sleep(1.0)  

        rospy.spin()

    def lengthFunction(self, mesaj):
        rospy.loginfo("Triange length: %s"%mesaj.kenaruzunluk)
        self.kenar_uzunlugu = mesaj.kenaruzunluk
        """

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
