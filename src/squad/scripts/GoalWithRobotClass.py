#!/usr/bin/env python

import Tkinter
import tkMessageBox
import rospy
from squad.msg import robot_position_msg, Kiwi
import math
from Robot import Robot
import sys
import rvo2

#starts subscribers
def initializeRobot(num):
	alarmID = -1 
	if(num <= 3):
		robot_number = "robot" + str(num) + "_cvpos"
		robot_pos = rospy.Subscriber(robot_number, robot_position_msg, callback, num)
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

def setGoal(event):
	root.after_cancel(afterID)
	#print "afterID setGoal: " + str(afterID)
	canvas.coords(text,event.x,event.y)
	goalx = event.x
	goaly = event.y
	print "goal set: " + str(goalx) + ", " + str(goaly)

	#set preferred velocities once
	for index, robot in enumerate(robots):
		coords = canvas.coords(robot.robotShapeID) #SIMULATED perfect position

	step(goalx, goaly)

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


#####END OF GUI SETUP#####
#####
#note: currently only finds the top right and measures, but this will cause problems eventually
#when the robots collide
#note2: Need to fix initialization process to consistently run using OpenCV because of the error
#note3: should create a class or struct called robot that contains simulation location,
#real location, whether it's reached it's goal,
#######
#####END OF GUI SETUP#####
def rotate(self, robotID, angle=0):
    '''Animation loop to rotate the line by 10 degrees every 100 ms'''
    a = math.radians(angle)
    r = 50
    x0, y0 = (200,200)
    x1 = x0 + r*math.cos(a)
    y1 = y0 + r*math.sin(a)
    x2 = x0 + -r*math.cos(a)
    y2 = y0 + -r*math.sin(a)
    canvas.coords("line", x1,y1,x2,y2)
    root.after(100, lambda angle=angle+10: self.rotate(angle))


def callback(data, index):
	currentRobot = robots[index]
	if currentRobot.robotShapeID == -1:
		#canvas.itemconfigure(currentRobot.robotShapeID, state = 'normal')
		#canvas.coords(currentRobot.robotShapeID, data.x-40,data.y-30,data.x+30,data.y+30)
		image_path = "/home/connie/robo_squad/src/squad/scripts/images/Robot" + str(index+1) + ".png"
		image = Image.open(image_path)
		image = image.resize((100, 100), Image.ANTIALIAS)
		image = image.rotate(data.angle-90)
		currentRobot.image = ImageTk.PhotoImage(image)
		currentRobot.robotShapeID = canvas.create_image(data.x, data.y, image = currentRobot.image)
		print image_path + ": " + str(image)
        #currentRobot.robotShapeID = Tkinter.Canvas.create_image(250, 250, image=image1)

	#note: this will always have the most recently updated location information. 
	#For current simulation position, call "canvas.coords"
	#print "in callback" + str(currentRobot.robotShapeID)"""
	currentRobot.irl_x = data.x
	currentRobot.irl_y = data.y
	currentRobot.irl_angle = 0-data.angle
	currentRobot.frontx = data.frontx
	currentRobot.front = data.fronty

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
		if robot.frontx != -1 and robot.fronty != -1:
			coords = canvas.coords(robot.robotShapeID) #SIMULATED perfect position
			velx = goalx - ((coords[2] - coords[0])/2 + coords[0]) #simulated vector from center
			vely = goaly - ((coords[3] - coords[1])/2 + coords[1])
			velx = math.degrees(math.cos((velx / 600) * 150))
			vely = math.degrees(math.sin((vely / 400) * 150))
			print "vel:" + str(velx) + ", " + str(vely)
			distFromGoal = abs(math.sqrt((velx)**2 + (vely)**2))

			kiwi = Kiwi()
			(vx, vy) = (robot.frontx - robot.irl_x, robot.fronty - robot.irl_y)
			(ux, uy) = (goalx - robot.irl_x, goaly - robot.irl_y)
			mag1 = math.sqrt(vx**2 + vy**2)
			mag2 = math.sqrt(ux**2 + uy**2)
			print str(robot.frontx) + ", " + str(robot.fronty)
			angle = math.degrees(math.acos(((vx * ux) + (vy * uy))/(mag1 * mag2)))
			print "ANGLE: " + str(angle)
			#convert to holonomic
			dutyCycles = convertToDutyCycles(velx, vely, angle)
			kiwi.w1 = dutyCycles[0]
			kiwi.w2 = dutyCycles[1]
			kiwi.w3 = dutyCycles[2]
			robot.publisher.publish(kiwi)

			if(distFromGoal < 20):
				print "reached Goal: " + str(index)
			else:
				rotate(robot.robotShapeID, robot.irl_angle)
				canvas.coords(robot.robotShapeID, robot.irl_x, robot.irl_y, robot.irl_x, robot.irl_y)
				print "ROBOT IRL: "+ str(robot.irl_x) + ", " + str(robot.irl_y)

	global afterID 
	afterID = root.after(100, step, goalx, goaly)
	#print "afterID step: " + str(afterID)

def convertToDutyCycles(vx, vy, angle):
	MAX_MAGNITUDE = 121.0
	DUTY_RANGE = 255.0
	x_max = math.cos(math.radians(angle)) * MAX_MAGNITUDE
	y_max = math.cos(math.radians(angle)) * MAX_MAGNITUDE
	magnitude = math.sqrt(vx**2 + vy**2)
	#print "first vx: " + str(vx) + " vy: " + str(vy)
	sign = lambda x: (1, -1)[x < 0]
	vx = math.cos(math.radians(angle)) * magnitude * sign(vx)
	vy = math.sin(math.radians(angle)) * magnitude * sign(vy)
	#print "second vx: " + str(vx) + " vy: " + str(vy)
	w1 = -vx;
	w2 = (0.5 * vx - math.sqrt(1.5) * vy);
	w3 = (0.5 * vx + math.sqrt(1.5) * vy);
	duty_w1 = w1 / 140 * DUTY_RANGE
	duty_w2 = w2 / 140 * DUTY_RANGE
	duty_w3 = w3 / 140 * DUTY_RANGE
	#print "PRE-DUTY: " + str(w1) + ", " + str(w2) + ", " + str(w3)
	print "DUTY: " + str(duty_w1) + ", " + str(duty_w2) + ", " + str(duty_w3)
	return (duty_w1, duty_w2, duty_w3)

print "about to call updateRobot"
#initializeRobot(0)

root.mainloop()