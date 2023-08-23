#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from ucgen_cizdirme.msg import Angle, Velocity
from nav_msgs.msg import Odometry


def hareket():
    rospy.init_node("triange")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
    velocity_message = Twist()
        
    velocity_message.angular.z = 2.0
    pub.publish(velocity_message)




try:
    hareket()

except rospy.ROSInternalException:
    print("Dugum Sonlandi!!!")