#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from scripts.eskenar_ucgen.ucgen_cizdirme_ui_3 import * 
import rospy
from geometry_msgs.msg import Twist
from math import radians
from ucgen_cizdirme.msg import Length, Angle
from nav_msgs.msg import Odometry


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
        self.baslatButon = QtWidgets.QPushButton(self.ustMenuFrame)
        self.baslatButon.setGeometry(QtCore.QRect(320, 150, 151, 41))
        self.baslatButon.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.baslatButon.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.baslatButon.setObjectName("baslatButon")
        self.label = QtWidgets.QLabel(self.ustMenuFrame)
        self.label.setGeometry(QtCore.QRect(150, 60, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
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
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.hizLabel.setFont(font)
        self.hizLabel.setObjectName("hizLabel")
        self.gridLayout.addWidget(self.hizLabel, 0, 0, 1, 1)
        self.hizLineEdit = QtWidgets.QLineEdit(self.altSolFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.hizLineEdit.setFont(font)
        self.hizLineEdit.setReadOnly(True)
        self.hizLineEdit.setObjectName("hizLineEdit")
        self.gridLayout.addWidget(self.hizLineEdit, 0, 1, 1, 1)
        self.KULabel = QtWidgets.QLabel(self.altSolFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.KULabel.setFont(font)
        self.KULabel.setObjectName("KULabel")
        self.gridLayout.addWidget(self.KULabel, 1, 0, 1, 1)
        self.KULineEdit = QtWidgets.QLineEdit(self.altSolFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.KULineEdit.setFont(font)
        self.KULineEdit.setReadOnly(True)
        self.KULineEdit.setObjectName("KULineEdit")
        self.gridLayout.addWidget(self.KULineEdit, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.altSolFrame)
        self.altSagFrame = QtWidgets.QFrame(self.altMenuFrame)
        self.altSagFrame.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.altSagFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.altSagFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.altSagFrame.setObjectName("altSagFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.altSagFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.konumYLabel = QtWidgets.QLabel(self.altSagFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.konumYLabel.setFont(font)
        self.konumYLabel.setObjectName("konumYLabel")
        self.gridLayout_2.addWidget(self.konumYLabel, 1, 0, 1, 1)
        self.konumXLabel = QtWidgets.QLabel(self.altSagFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.konumXLabel.setFont(font)
        self.konumXLabel.setObjectName("konumXLabel")
        self.gridLayout_2.addWidget(self.konumXLabel, 0, 0, 1, 1)
        self.konumXLineEdit = QtWidgets.QLineEdit(self.altSagFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.konumXLineEdit.setFont(font)
        self.konumXLineEdit.setReadOnly(True)
        self.konumXLineEdit.setObjectName("konumXLineEdit")
        self.gridLayout_2.addWidget(self.konumXLineEdit, 0, 1, 1, 1)
        self.konumYLineEdit = QtWidgets.QLineEdit(self.altSagFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.konumYLineEdit.setFont(font)
        self.konumYLineEdit.setReadOnly(True)
        self.konumYLineEdit.setObjectName("konumYLineEdit")
        self.gridLayout_2.addWidget(self.konumYLineEdit, 1, 1, 1, 1)
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
        self.baslatButon.setText(_translate("MainWindow", "Başlat"))
        self.label.setText(_translate("MainWindow", "EŞKANAR ÜÇGEN ÇİZME UYGULAMASI"))
        self.hizLabel.setText(_translate("MainWindow", "HIZ:"))
        self.KULabel.setText(_translate("MainWindow", "KENAR UZUNLUĞU:"))
        self.konumYLabel.setText(_translate("MainWindow", "Konum Y:"))
        self.konumXLabel.setText(_translate("MainWindow", "Konum X: "))

        rospy.init_node('draw_triangle_node', anonymous=True)
        self.vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber("odom",Odometry,self.odomCallback)
        rospy.Subscriber("kenar_topic", Length, self.lengthFunction)
        rospy.Subscriber("aci_topic", Angle, self.angleFunction)
        rate = rospy.Rate(1)  
        self.vel_msg = Twist()
        self.kenar_uzunlugu = 0.0  
        self.angle = 0.0  

        self.baslatButon.clicked.connect(self.Triangle)

        self.konumYLineEdit.setText(str(0.0))
        self.konumXLineEdit.setText(str(0.0))
        self.hizLineEdit.setText(str(0.0))
        self.KULineEdit.setText(str(0.0))
   


    def Triangle(self):
        # for oluşturup kenar sayısı kadar forun dönmesini sağladık böylece üçgen elde edebileceğiz.
        for i in range(3):

            # 120* döndürdük
            self.vel_msg.linear.x = 0.0
            self.vel_msg.angular.z = radians(self.angle) 
            self.vel_publisher.publish(self.vel_msg)
            self.hizLineEdit.setText(str(self.vel_msg.linear.x))
            rospy.sleep(1.0)  

            # dur
            self.vel_msg.angular.z = 0.0
            self.vel_publisher.publish(self.vel_msg)
            self.hizLineEdit.setText(str(self.vel_msg.linear.x))
            rospy.sleep(1.0)  

            # ilerle
            self.vel_msg.linear.x = 0.2  
            self.vel_msg.angular.z = 0.0
            self.vel_publisher.publish(self.vel_msg)
            self.hizLineEdit.setText(str(self.vel_msg.linear.x))
            rospy.sleep(self.kenar_uzunlugu / 0.2)  # T=X/V formülü ile turtlebot3'ün ne kadar süre gitmesi gerektiğini hesapladık ve bu süre bittiği anda durdurduk

            # dur
            self.vel_msg.linear.x = 0.0
            self.vel_publisher.publish(self.vel_msg)
            self.hizLineEdit.setText(str(self.vel_msg.linear.x))
            rospy.sleep(1.0)  

        rospy.spin()

    def odomCallback(self,mesaj):
        self.konumXLineEdit.setText(str(round(mesaj.pose.pose.position.x)))
        self.konumYLineEdit.setText(str(round(mesaj.pose.pose.position.y)))

    def lengthFunction(self, mesaj):
        rospy.loginfo("Triange length: %s"%mesaj.kenaruzunluk)
        self.kenar_uzunlugu = mesaj.kenaruzunluk
        self.KULineEdit.setText(str(self.kenar_uzunlugu))
        
    def angleFunction(self, mesaj):
        rospy.loginfo("Angle: %s"%mesaj.angle)
        self.angle = mesaj.angle


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
