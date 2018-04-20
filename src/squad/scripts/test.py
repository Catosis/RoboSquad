#!/usr/bin/env python
import rospy
from squad.msg import robot_position_msg

def talker():
    pub0 = rospy.Publisher('robot0_pos', robot_position_msg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg0 = robot_position_msg()
    msg0.x = 100
    msg0.y = 100
    msg0.angle = 45

    pub1 = rospy.Publisher('robot1_pos', robot_position_msg, queue_size=10)
    msg1 = robot_position_msg()
    msg1.x = 700
    msg1.y = 100
    msg1.angle = 45

    pub2 = rospy.Publisher('robot2_pos', robot_position_msg, queue_size=10)
    msg2 = robot_position_msg()
    msg2.x = 100
    msg2.y = 500
    msg2.angle = 45

    pub3 = rospy.Publisher('robot3_pos', robot_position_msg, queue_size=10)
    msg3 = robot_position_msg()
    msg3.x = 700
    msg3.y = 500
    msg3.angle = 45


    while not rospy.is_shutdown():
        rospy.loginfo(msg0)
        pub0.publish(msg0)
        pub1.publish(msg1)
        pub2.publish(msg2)
        pub3.publish(msg3)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
