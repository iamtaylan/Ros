#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import rospy
from ucgen_cizdirme.msg import Rotate,Vector3

# Hız mesajımızı yayınlicağımız düğümü oluşturduk.
rospy.init_node("publisher_node",anonymous=True)
pub = rospy.Publisher("hiz_topic",Vector3,queue_size=10)

rate = rospy.Rate(1) # 1 hz

# Hız değerimizi kullanıcıdan istedik 
# istediğimiz aralıkta girene kadar while döndürdük
i = 1
while i:
    hiz = float(input("hiz değeri giriniz(örn: 0.5)(maksimum 1.0 giriniz): \n"))
    if 0.0 < hiz <= 1.0:
        i = 0
    elif hiz == 0:
        print("Lütfen 0'dan büyük bir sayı giriniz.")
        i = 1
    else:
        print("Lütfen 0'dan büyük ve 1.0'dan küçük bir sayı giriniz. ")
        i = 1



while not rospy.is_shutdown():
    rospy.loginfo(hiz)
    pub.publish(hiz, 0, 0)
    rate.sleep()

