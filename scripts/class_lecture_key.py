#!/usr/bin/python

import getch
import rospy
from std_msgs.msg import String #String message 
from std_msgs.msg import Int8
from std_msgs.msg import Float64
import sys, select, termios, tty

class LECTURE_KEY:
    def __init__(self):
        self.nameTopicSub = "key"
        self.nameTopicPub1 = "/right_wheel_ctrl/command"
        self.nameTopicPub2 = "/left_wheel_ctrl/command"

        rospy.Subscriber(self.nameTopicSub,self.Lidar_Callback,queue_size=10)
        self.pub1 = rospy.Publisher(self.nameTopicPub1,Float64,queue_size=10)
        self.pub2 = rospy.Publisher(self.nameTopicPub2,Float64,queue_size=10)

        rate = rospy.Rate(10)

        key_pressed = False

        while (not rospy.is_shutdown()):
            if (key_pressed):
                self.pub1.publish(5)
                key_pressed = False


    def Lidar_Callback(self, lidar_scan):
        k=ord(getch.getch())
        rospy.loginfo(str(k))
        key_pressed = True

    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key
