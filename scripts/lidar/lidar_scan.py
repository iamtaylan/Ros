#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from ucgen_cizdirme.msg import Laser, Rotate, Vector3
from sensor_msgs.msg import LaserScan

class LazerVerisi():
    def __init__(self):
        rospy.init_node("lidar")
        self.pub = rospy.Publisher("cmd_vel",Rotate,queue_size = 10)
        rospy.Subscriber("scan",LaserScan,self.lazerCallback)
        rospy.Subscriber("hiz_topic",Vector3 ,self.VelCallBack)
        self.hiz_mesaji = Rotate()

        self.hiz_mesaji.linear.x = 0.0
        rospy.spin()
    
    def lazerCallback(self,mesaj):
        sol_on = list(mesaj.ranges[0:9])
        sag_on = list(mesaj.ranges[350:359])
        on = sol_on + sag_on
        sol = list(mesaj.ranges[80:100])
        sag = list(mesaj.ranges[260:280])
        arka = list(mesaj.ranges[170:190])
        min_on = min(on)
        min_sol = min(sol)
        min_sag = min(sag)
        min_arka = min(arka)
        print(min_on,min_sol,min_sag,min_arka)
        if min_on < (self.hiz_mesaji.linear.x + 0.5):
            self.hiz_mesaji.linear.x = 0.0
            self.pub.publish(self.hiz_mesaji)
        else:
            self.hiz_mesaji.linear.x = self.hiz_mesaji.linear.x
            self.pub.publish(self.hiz_mesaji)
                    

    def VelCallBack(self, hiz_mesaj):
        rospy.loginfo("Hiz: %s" %hiz_mesaj.x)
        self.hiz_mesaji.linear.x = hiz_mesaj.x


nesne = LazerVerisi()