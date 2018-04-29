#!/usr/bin/env python

"""
Description: Example echo client.
Author: Amol Kapoor
"""
#This is the COMPUTER
#it sends

import sys
import SocketWrapper
from std_msgs.msg import String
from squad.msg import Kiwi
import rospy


pwm1=pwm2=pwm3=0
PWMmsg = "no data"
#sock0 = SocketWrapper.SocketWrapper(is_listener=False, socket_info=('192.168.1.2', 5020))
#sock0 = SocketWrapper.SocketWrapper(is_listener=False, socket_info=('192.168.1.2', 5020))
#sock0 = SocketWrapper.SocketWrapper(is_listener=False, socket_info=('192.168.1.2', 5020))
sock3 = SocketWrapper.SocketWrapper(is_listener=False, socket_info=('192.168.1.3', 5020))

"""def callback0(data):
	rospy.loginfo("[%5.2f, %5.2f, %5.2f]", data.w1, data.w2, data.w3)
	pwm1 = data.w1
	pwm2 = data.w2
	pwm3 = data.w3
	PWMmsg = "[%5.2f, %5.2f, %5.2f]" % (pwm1, pwm2, pwm3)
	sock0.send_data(PWMmsg)

def callback1(data):
	rospy.loginfo("[%5.2f, %5.2f, %5.2f]", data.w1, data.w2, data.w3)
	pwm1 = data.w1
	pwm2 = data.w2
	pwm3 = data.w3
	PWMmsg = "[%5.2f, %5.2f, %5.2f]" % (pwm1, pwm2, pwm3)
	sock1.send_data(PWMmsg)

def callback2(data):
	rospy.loginfo("[%5.2f, %5.2f, %5.2f]", data.w1, data.w2, data.w3)
	pwm1 = data.w1
	pwm2 = data.w2
	pwm3 = data.w3
	PWMmsg = "[%5.2f, %5.2f, %5.2f]" % (pwm1, pwm2, pwm3)
	sock2.send_data(PWMmsg)"""

def callback3(data):
	rospy.loginfo("[%5.2f, %5.2f, %5.2f]", data.w1, data.w2, data.w3)
	pwm1 = data.w1
	pwm2 = data.w2
	pwm3 = data.w3
	PWMmsg = "[%5.2f, %5.2f, %5.2f]" % (pwm1, pwm2, pwm3)
	sock3.send_data(PWMmsg)


if __name__ == '__main__':
	rospy.init_node('robotListener', anonymous=True)
	#rospy.Subscriber("robot0_kiwi", Kiwi, callback0)
	#rospy.Subscriber("robot1_kiwi", Kiwi, callback1)
	#rospy.Subscriber("robot2_kiwi", Kiwi, callback2)
	rospy.Subscriber("robot3_kiwi", Kiwi, callback3)
	print "started Client"    
	
	rospy.loginfo("before")
	#s.send_data(PWMmsg)
	rospy.loginfo("after")

	rospy.spin()


	"""try:
		while not rospy.is_shutdown():
			message = raw_input("Input echo info.\n")
			s.send_data(message, ['info 1', 'info 2'])
			PWMout = "%f, %f, %f \n" % (pwm1, pwm2, pwm3)
			s.send_data(PWMout, ['info 1', 'info 2'])
	#except KeyboardInterrupt:
	except rospy.ROSInterruptException:
	    s.close_socket()
	    #sys.exit()"""
