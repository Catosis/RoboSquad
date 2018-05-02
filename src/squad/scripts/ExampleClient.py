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

def init_socket(is_listener, socket_info):
	try:
		s = SocketWrapper.SocketWrapper(is_listener=is_listener, socket_info=socket_info)
		print "Connected %s" % str(socket_info)
		return s
	except Exception:
		print "No connection to %s" % str(socket_info)
		return None

sock0 = init_socket(is_listener=False, socket_info=('192.168.1.2', 5020))
sock1 = init_socket(is_listener=False, socket_info=('192.168.1.3', 5020))
sock2 = init_socket(is_listener=False, socket_info=('192.168.1.5', 5020))
sock3 = init_socket(is_listener=False, socket_info=('192.168.1.6', 5020))

if not sock0 and not sock1 and not sock2 and not sock3:
	raise ValueError("No input")
	sys.exit()

def callback0(data):
	if not sock0:
		return
	rospy.loginfo("[%5.2f, %5.2f, %5.2f]", data.w1, data.w2, data.w3)
	pwm1 = data.w1
	pwm2 = data.w2
	pwm3 = data.w3
	PWMmsg = "[%5.2f, %5.2f, %5.2f]" % (pwm1, pwm2, pwm3)
	sock0.send_data(PWMmsg)

def callback1(data):
	if not sock1:
		return
	rospy.loginfo("[%5.2f, %5.2f, %5.2f]", data.w1, data.w2, data.w3)
	pwm1 = data.w1
	pwm2 = data.w2
	pwm3 = data.w3
	PWMmsg = "[%5.2f, %5.2f, %5.2f]" % (pwm1, pwm2, pwm3)
	sock1.send_data(PWMmsg)

def callback2(data):
	if not sock2:
		return
	rospy.loginfo("[%5.2f, %5.2f, %5.2f]", data.w1, data.w2, data.w3)
	pwm1 = data.w1
	pwm2 = data.w2
	pwm3 = data.w3
	PWMmsg = "[%5.2f, %5.2f, %5.2f]" % (pwm1, pwm2, pwm3)
	sock2.send_data(PWMmsg)

def callback3(data):
	if not sock3:
		return
	rospy.loginfo("[%5.2f, %5.2f, %5.2f]", data.w1, data.w2, data.w3)
	pwm1 = data.w1
	pwm2 = data.w2
	pwm3 = data.w3
	PWMmsg = "[%5.2f, %5.2f, %5.2f]" % (pwm1, pwm2, pwm3)
	sock3.send_data(PWMmsg)


if __name__ == '__main__':
	rospy.init_node('robotListener', anonymous=True)
	rospy.Subscriber("robot0_kiwi", Kiwi, callback0)
	rospy.Subscriber("robot1_kiwi", Kiwi, callback1)
	rospy.Subscriber("robot2_kiwi", Kiwi, callback2)
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
