#!/usr/bin/env python

import Tkinter
import tkMessageBox
import rospy
from squad.msg import robot_position_msg, Kiwi
import math
from Robot import Robot
import sys

#starts subscribers
def initializeRobot(num):
	alarmID = -1 
	if(num <= 3):
		robot_number = "robot" + str(num) + "_cvpos"
		robot_pos = rospy.Subscriber(robot_number, robot_position_msg, callback, num)
		canvas.pack()
		#print robot_number
		num +=1
		alarmID = root.after(100, initializeRobot, num)
	else:
		print "cancelling alarm"
		root.after_cancel(alarmID)

def cleanCloseProgram():
	cleanMsg = Kiwi()
	cleanMsg.w1 = cleanMsg.w2 = cleanMsg.w3 = 0
	robot0.publisher.publish(cleanMsg)
	robot1.publisher.publish(cleanMsg)
	robot2.publisher.publish(cleanMsg)
	robot3.publisher.publish(cleanMsg)
	sys.exit(0)

####GUI INIT####
root = Tkinter.Tk()
start_button = Tkinter.Button(root, text="Start", command=lambda: initializeRobot(0))
start_button.pack()
canvas = Tkinter.Canvas(root, bg="#371627", height=600, width=800)
text = canvas.create_text(-100, -100, text = "Goal", fill="red")
quit_button = Tkinter.Button(root, text="Quit", command=cleanCloseProgram)
quit_button.pack()
rospy.init_node('listener', anonymous=True)
#init 4 robots
robot0 = Robot()
robot1 = Robot()
robot2 = Robot()
robot3 = Robot()
robot0.robotShapeID = canvas.create_oval(0,0,0,0, state = 'hidden', fill = "#df9f3c")
robot1.robotShapeID = canvas.create_oval(0, 0, 0,0, state = 'hidden', fill = "#df7c18")
robot2.robotShapeID = canvas.create_oval(0, 0, 0,0, state = 'hidden', fill = "#c18080")
robot3.robotShapeID = canvas.create_oval(0, 0, 0,0, state = 'hidden', fill = "#e8bb76")
robots = [robot0, robot1, robot2, robot3] # the num refers to the ID of the circle created
global robot_pos
afterID = -1
#turn on robot publishers
robot0.publisher = rospy.Publisher("robot0_kiwi", Kiwi, queue_size = 10)
robot1.publisher = rospy.Publisher("robot1_kiwi", Kiwi, queue_size = 10)
robot2.publisher = rospy.Publisher("robot2_kiwi", Kiwi, queue_size = 10)
robot3.publisher = rospy.Publisher("robot3_kiwi", Kiwi, queue_size = 10)

#####END OF GUI SETUP#####
def callback(data, index):
	currentRobot = robots[index]
	current_coords = canvas.coords(currentRobot.robotShapeID)
	if current_coords[0] == 0:
		canvas.itemconfigure(currentRobot.robotShapeID, state = 'normal')
		canvas.coords(currentRobot.robotShapeID, data.x-58,data.y-58,data.x+58,data.y+58)
	#note: this will always have the most recently updated location information. 
	#For current simulation position, call "canvas.coords"
	
	currentRobot.irl_x = data.x
	currentRobot.irl_y = data.y
	currentRobot.irl_angle = data.angle

#####
#note: currently only finds the top right and measures, but this will cause problems eventually
#when the robots collide
#note2: Need to fix initialization process to consistently run using OpenCV because of the error
#note3: should create a class or struct called robot that contains simulation location,
#real location, whether it's reached it's goal,
#######

#publish to real world
def step(goalx, goaly):
	#print "in step: " + str(goalstepx) + ", " + str(goalstepy)
	for index, robot in enumerate(robots):
		coords = canvas.coords(robot.robotShapeID) #SIMULATED perfect position
		vectorx = goalx - ((coords[2] - coords[0])/2 + coords[0]) #simulated vector from center
		vectory = goaly - ((coords[3] - coords[1])/2 + coords[1])
		distFromGoal = abs(math.sqrt((vectorx)**2 + (vectory)**2))
		#print "goal in step:" + str(goalx) + ", " + str(goaly)

		kiwi = Kiwi()
		angle = math.radians(robot.irl_angle)
		vx = math.cos(angle)*distFromGoal
		vy = math.sin(angle)*distFromGoal

		#get porportion
		vx = vx / 300
		vy = vy / 200
		kiwi.w1 = -vx * 255; #number is the duty cycle %. 100% when vx > 
		kiwi.w2 = 0.5 * vx - math.sqrt(1.5) * vy * 255;
		kiwi.w3 = 0.5 * vx + math.sqrt(1.5) * vy * 255;
		if(kiwi.w1 > 255):
			kiwi.w1 = 100
		elif(kiwi.w1 < -255):
			kiwi.w1 = 100
		if(kiwi.w2 > 255):
			kiwi.w2 = 100
		elif(kiwi.w2 < -255):
			kiwi.w2 = 100
		if(kiwi.w3 > 255):
			kiwi.w3 = 100
		elif(kiwi.w3 < -255):
			kiwi.w3 = 100
		#print "kiwi---" + str(kiwi.w1) + ", " + str(kiwi.w2) + ", " + str(kiwi.w3)
		robot.publisher.publish(kiwi)

		if(distFromGoal < 100):
			print "reached Goal: " + str(index)
		else:
			#initial draw for simulated step 
			canvas.move(robot.robotShapeID, vectorx*.005, vectory*.005) 
			#canvas redraws what opencv sees, COMMENT IF NO CAMERA ATTACHED
			#canvas.coords(robot.robotShapeID, robot.irl_x-10, robot.irl_y-10, robot.irl_x+10, robot.irl_y+10)
			canvas.pack()
	global afterID 
	afterID = root.after(100, step, goalx, goaly)
	#print "afterID step: " + str(afterID)

def setGoal(event):
	root.after_cancel(afterID)
	#print "afterID setGoal: " + str(afterID)
	canvas.coords(text,event.x,event.y)
	goalx = event.x
	goaly = event.y
	print "goal set: " + str(goalx) + ", " + str(goaly)
	start_button.update_idletasks()
	#canvas.unbind("<Button-1>")
	step(goalx, goaly)
	#root.after(500, step, goalx, goaly)


canvas.bind("<Button-1>", setGoal)
canvas.pack()

print "about to call updateRobot"
#initializeRobot(0)

root.mainloop()