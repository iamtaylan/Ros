#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from ucgen_cizdirme.msg import Angle

def publishMessage():
    rospy.init_node("publisher_node",anonymous=True)
    pub = rospy.Publisher("angle_topic",Angle,queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        durum = 60
        rospy.loginfo(durum)
        pub.publish(durum)
        rate.sleep()

publishMessage()