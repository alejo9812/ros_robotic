#!/usr/bin/python

import rospy
from class_lecture_key import LECTURE_KEY

# Init of program
if __name__ == '__main__':

    rospy.init_node('key_press', anonymous=True)

    rospy.loginfo("Node init")

    LECTURE_KEY()

    rospy.spin()