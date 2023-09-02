#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtQuickWidgets import *
from PyQt5.QtCore import *
from ucgen_cizdirme_ui_2 import * 
import rospy
from geometry_msgs.msg import Twist
from math import radians
from ucgen_cizdirme.msg import Length


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
