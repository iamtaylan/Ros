#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from ucgen_cizdirme.msg import Length, Angle

rospy.init_node("publisher_node",anonymous=True)
pub = rospy.Publisher("kenar_topic",Length,queue_size=10)
pub2 = rospy.Publisher("aci_topic",Angle,queue_size=10)

rate = rospy.Rate(1)
kenarUzunluk = float(input("kenar uzunluğu değeri giriniz(örn: 2.0): "))
angle = 120

while not rospy.is_shutdown():
    rospy.loginfo(kenarUzunluk)
    pub.publish(kenarUzunluk)
    pub2.publish(angle)
    rate.sleep()

