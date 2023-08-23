#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import rospy
from ucgen_cizdirme.msg import Angle

def angleFunction(mesaj):
    rospy.loginfo("Triange angle: %s"%mesaj.angle)

def listenMessage():
    rospy.init_node("subscriber_node")
    rospy.Subscriber("angle_topic",Angle,angleFunction)
    rospy.spin()

listenMessage()