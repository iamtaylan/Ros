#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from ucgen_cizdirme.msg import Length

rospy.init_node("publisher_node",anonymous=True)
pub = rospy.Publisher("kenar_topic",Length,queue_size=10)
rate = rospy.Rate(1)
durum = float(input("kenar uzunluğu değeri giriniz(örn: 2.0): "))

while not rospy.is_shutdown():
    rospy.loginfo(durum)
    pub.publish(durum)
    rate.sleep()

