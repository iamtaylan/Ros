#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from math import radians
from ucgen_cizdirme.msg import VelocityAngular, VelocityBreak, VelocityLineer, Length

class Triangle():
    def __init__(self):
        rospy.init_node('draw_triangle_node', anonymous=True)
        vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber("kenar_uzunluk_node", Length, self.mesafeCallBack)
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

    def mesafeCallBack(self, mesaj):
        self.kenar_uzunlugu = mesaj.kenaruzunluk

try:
    Triangle()
except rospy.ROSInterruptException:
    pass
