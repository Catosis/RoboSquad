#!/usr/bin/env python

from __future__ import division
import Tkinter
import tkMessageBox
import rospy
from squad.msg import robot_position_msg, Kiwi
import math
from Robot import Robot
import sys
import rvo2
from PIL import Image, ImageTk 
import numpy as np

R_SIZE = 50 #radius
#starts subscribers
def initializeRobot(num):
	alarmID = -1 
	if(num <= 3):
		robot_number = "robot" + str(num) + "_cvpos"
		robot_pos = rospy.Subscriber(robot_number, robot_position_msg, callback, num)
		num +=1
		alarmID = root.after(100, initializeRobot, num)
		canvas.bind("<Button-1>", setGoal)
		canvas.pack()
	else:
		root.after_cancel(alarmID)

def cleanCloseProgram():
	cleanMsg = Kiwi()
	cleanMsg.w1 = cleanMsg.w2 = cleanMsg.w3 = 0
	robot0.publisher.publish(cleanMsg)
	robot1.publisher.publish(cleanMsg)
	robot2.publisher.publish(cleanMsg)
	robot3.publisher.publish(cleanMsg)
	sys.exit(0)

def setGoal(event):
	root.after_cancel(afterID)
	#print "afterID setGoal: " + str(afterID)
	canvas.coords(text,event.x,event.y)
	goalx = event.x
	goaly = event.y
	print "goal set: " + str(goalx) + ", " + str(goaly)

	#set preferred velocities once
	for index, robot in enumerate(robots):
		if robot.agent != -1:
			coords = canvas.coords(robot.robotShapeID) #SIMULATED perfect position
			x_vec = goalx - (coords[0]) #simulated vector from center
			y_vec = goaly - (coords[1])
			"""x_norm = x_vec/math.sqrt(x_vec**2 + y_vec**2) * 1000
			y_norm = y_vec/math.sqrt(x_vec**2 + y_vec**2) * 1000"""

	step(goalx, goaly)

def callback(data, index):
	currentRobot = robots[index]
	if currentRobot.robotShapeID == -1:
		image_path = "/home/connie/robo_squad/src/squad/scripts/images/Robot" + str(index+1) + ".png"
		image = Image.open(image_path)
		image = image.resize((100, 100), Image.ANTIALIAS)
		image = image.rotate(data.angle-90)
		currentRobot.image = ImageTk.PhotoImage(image)
		string = "robot" + str(index)
		currentRobot.robotShapeID = canvas.create_image(data.x, data.y, tags = "robot3", image = currentRobot.image)
		print image_path + ": " + str(image)

	#note: this will always have the most recently updated location information. 
	#For current simulation position, call "canvas.coords"
	#print "in callback" + str(currentRobot.robotShapeID)"""
	currentRobot.irl_x = data.x
	currentRobot.irl_y = data.y
	currentRobot.irl_angle = 0-data.angle
	currentRobot.frontx = data.frontx
	currentRobot.fronty = data.fronty
	
####GUI INIT####
root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, bg="#371627", height=600, width=800)
text = canvas.create_text(-100, -100, text = "Goal", fill="red")

start_button = Tkinter.Button(root, text="Start", command=lambda: initializeRobot(0))
start_button.pack()
quit_button = Tkinter.Button(root, text="Quit", command=cleanCloseProgram)
quit_button.pack()
canvas.pack()
rospy.init_node('listener', anonymous=True)
#init 4 robots
robot0 = Robot("Robot 1")
robot1 = Robot("Robot 2")
robot2 = Robot("Robot 3")
robot3 = Robot("Robot 4")

"""robot0.robotShapeID = canvas.create_oval(0,0,0,0, state = 'hidden', fill = "#df9f3c")
robot1.robotShapeID = canvas.create_oval(0, 0, 0,0, state = 'hidden', fill = "#df7c18")
robot2.robotShapeID = canvas.create_oval(0, 0, 0,0, state = 'hidden', fill = "#c18080")
robot3.robotShapeID = canvas.create_oval(0, 0, 0,0, state = 'hidden', fill = "#e8bb76")"""
robots = [robot0, robot1, robot2, robot3] # the num refers to the ID of the circle created
global robot_pos
afterID = -1
#turn on robot publishers
robot0.publisher = rospy.Publisher("robot0_kiwi", Kiwi, queue_size = 10)
robot1.publisher = rospy.Publisher("robot1_kiwi", Kiwi, queue_size = 10)
robot2.publisher = rospy.Publisher("robot2_kiwi", Kiwi, queue_size = 10)
robot3.publisher = rospy.Publisher("robot3_kiwi", Kiwi, queue_size = 10)

#ORCA
sim = rvo2.PyRVOSimulator(1/60., 110, 2, 1.5, 50, 100, 100)
#o1 = sim.addObstacle([(0, 0), (800, 0), (800, -5), (0, -5)])
#o2 = sim.addObstacle([(0, 0), (-5, 0), (-5, 600), (0, 600)])
#ssim.processObstacles()

#####END OF GUI SETUP#####
#####
#note: currently only finds the top right and measures, but this will cause problems eventually
#when the robots collide
#note2: Need to fix initialization process to consistently run using OpenCV because of the error
#note3: should create a class or struct called robot that contains simulation location,
#real location, whether it's reached it's goal,
#######
def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return math.atan2(b.y,b.x) - math.atan2(a.y,a.x)
    #return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

#publish to real world
def step(goalx, goaly):
	print "in step"
	for index, robot in enumerate(robots):
		if robot.frontx != -1 and robot.fronty != -1:
			imageID = "robot"+str(index)
			print imageID
			coords = canvas.coords("robot3")
			#switched axis from simulation to robot axis, which is 90 dgrees off
			velx = goalx - robot.frontx
			vely = goaly - robot.fronty
			orientation_x = robot.frontx - robot.irl_x
			orientation_y = robot.fronty - robot.irl_y
			#angle = angle_between((velx, vely), (orientation_x, orientation_y))
			angle = math.atan2(vely,velx) - math.atan2(orientation_y,orientation_x)
			print "ANGLE: " + str(math.degrees(-angle))
			kiwi = Kiwi()
			distFromGoal = abs(math.sqrt((velx)**2 + (vely)**2))

			"""print "initial velocity:" + str(velx) + ", " + str(vely)
			print "Simulation Position: " + str(coords[0]) + " : " +  str(coords[1]) 

			kiwi = Kiwi()
			(vx, vy) = (robot.frontx - robot.irl_x, robot.fronty - robot.irl_y)
			(ux, uy) = (goalx - robot.irl_x, goaly - robot.irl_y)
			mag1 = math.sqrt(vx**2 + vy**2)
			mag2 = math.sqrt(ux**2 + uy**2)
			#Need to determine quadrants for the angle
			angle = math.degrees(math.acos(((vx * ux) + (vy * uy))/(mag1 * mag2)))
			#angle = math.degrees(math.atan2(float(velx), float(vely))); #Angle between desired velocity and robot if robot is facing in the zero direction
			if math. vely < 0:
				angle = -angle


			#total_y = orientation_x + velx
			#total_x = orientation_y + vely
			#angle = math.degrees(math.atan2(float(total_x), float(total_y)))

			print "CALC ANGLE: " + str(angle)"""

			#convert to holonomic
			dutyCycles = convertToDutyCycles(velx, vely, math.degrees(-angle))
			kiwi.w1 = dutyCycles[0]
			kiwi.w2 = dutyCycles[1]
			kiwi.w3 = dutyCycles[2]

			#print "Velocity to kiwi duty cycle: " + str(kiwi.w1) + ", " + str(kiwi.w2) + ", " + str(kiwi.w3)
			robot.publisher.publish(kiwi)

			if(distFromGoal < 50):
				print "reached Goal: " + str(index)

			else:
				x_dist = goalx - robot.irl_x #getAgentPosition(robot.agent)[0]
				y_dist = goaly - robot.irl_y #getAgentPosition(robot.agent)[1]
				canvas.coords("robot3", robot.irl_x, robot.irl_y)
				print "ROBOT IRL: "+ str(robot.irl_x) + ", " + str(robot.irl_y)
				canvas.pack()
	global afterID 
	afterID = root.after(50, step, goalx, goaly)
	#print "afterID step: " + str(afterID)

def convertToDutyCycles(vx, vy, angle):
	MAX_MAGNITUDE = 121.0
	DUTY_RANGE = 255.0
	x_max = math.cos(math.radians(angle)) * MAX_MAGNITUDE
	y_max = math.sin(math.radians(angle)) * MAX_MAGNITUDE
	magnitude = math.sqrt(vx**2 + vy**2)
	#print "first vx: " + str(vx) + " vy: " + str(vy)
	vx = -math.sin(math.radians(angle)) * magnitude #* #sign(vx)
	vy = math.cos(math.radians(angle)) * magnitude #* #sign(vy)
	#print "second vx: " + str(vx) + " vy: " + str(vy)
	w1 = -vx;
	w2 = (0.5 * vx - math.sqrt(1.5) * vy);
	w3 = (0.5 * vx + math.sqrt(1.5) * vy);
	duty_w1 = w1 / 140 * DUTY_RANGE
	duty_w2 = w2 / 140 * DUTY_RANGE
	duty_w3 = w3 / 140 * DUTY_RANGE
	print "PRE-DUTY: " + str(w1) + ", " + str(w2) + ", " + str(w3)
	print "DUTY: " + str(duty_w1) + ", " + str(duty_w2) + ", " + str(duty_w3)
	#return (duty_w1, duty_w2, duty_w3)
	return (w1, w2, w3)



print "about to call updateRobot"
#initializeRobot(0)

root.mainloop()