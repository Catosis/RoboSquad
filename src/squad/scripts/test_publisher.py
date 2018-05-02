#!/usr/bin/env python
import rospy
from squad.msg import robot_position_msg
import random

def talker():

    pub1 = rospy.Publisher('robot1_cvpos', robot_position_msg, queue_size=10)
    pub0 = rospy.Publisher('robot0_cvpos', robot_position_msg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    x = y = 50
    X2 = Y2 = 600
    while not rospy.is_shutdown():
        msg0 = robot_position_msg()
        if x < 500:
            x = x + 10
            y = y + 10
            msg0.x = x
            msg0.y = y
            msg0.angle = 45
        else:
            x = y = 50
            msg0.x = x
            msg0.y = y
            msg0.angle = 0

        """msg1 = robot_position_msg()
        if x2 < 500:
            x2 = x2- 10
            y2 = y2 - 10
            msg1.x = x2
            msg1.y = y2
            msg1.angle = 270
        else:
            x2 = y2 = 600
            msg1.x2 = x2
            msg1.y2 = y2
            msg1.angle = 0"""

        """pub2 = rospy.Publisher('robot2_cvpos', robot_position_msg, queue_size=10)
        msg2 = robot_position_msg()
        msg2.x = 100
        msg2.y = 500
        msg2.angle = 45

        pub3 = rospy.Publisher('robot3_cvpos', robot_position_msg, queue_size=10)
        msg3 = robot_position_msg()
        msg3.x = 700
        msg3.y = 500
        msg3.angle = 45"""


        rospy.loginfo(msg0)
        pub0.publish(msg0)
        #pub1.publish(msg1)
        #pub2.publish(msg2)
        #pub3.publish(msg3)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
