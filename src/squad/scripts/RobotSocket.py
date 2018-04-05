#!/usr/bin/env python

"""
Description: Example echo server.
Author: Amol Kapoor
"""

#This is the ROBOT SERVER
#it LISTENS

import sys
import SocketWrapper
import pigpio

if __name__ == '__main__':
	s = SocketWrapper.SocketWrapper(is_listener=True, socket_info=('localhost', 5000))

	try:
	    while True:
	        message = s.get_message()
	        print message
	        s.send_data(message[-1])
	except KeyboardInterrupt:
	    s.close_socket()
	    sys.exit()
