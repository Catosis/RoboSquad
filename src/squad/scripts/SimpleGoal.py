#!/usr/bin/env python

import Tkinter
import tkMessageBox
import rospy
from squad.msg import robot_position_msg, Kiwi
import math

root = Tkinter.Tk()
close_button = Tkinter.Button(root, text="Close", command=root.quit)
close_button.pack()
#start_button = Tkinter.Button(root, text="Close", command=initRobots)
#start_button.pack()
canvas = Tkinter.Canvas(root, bg="#371627", height=600, width=800)
rospy.init_node('listener', anonymous=True)
#init 4 robots
rshapeID0 = canvas.create_oval(0,0,0,0, state = 'hidden', fill = "#df9f3c")
rshapeID1 = canvas.create_oval(0, 0, 0,0, state = 'hidden', fill = "#df7c18")
rshapeID2 = canvas.create_oval(0, 0, 0,0, state = 'hidden', fill = "#c18080")
rshapeID3 = canvas.create_oval(0, 0, 0,0, state = 'hidden', fill = "#e8bb76")
text = canvas.create_text(-100, -100, text = "Goal", fill="red")
robots = [rshapeID0, rshapeID1, rshapeID2, rshapeID3] # the num refers to the ID of the circle created
#stores the MOST UPDATED version of the robot's position from opencv
robot_data = {
	"0_x": 0,
	"0_y":0,
	"0_angle":0,
	"1_x":0,
	"1_y:": 0,
	"1_angle":0,
	"2_x":0,
	"2_y":0,
	"2_angle": 0,
	"3_x": 0,
	"3_y": 0,
	"3_angle":0
}
goalx = goaly = None  
global robot_pos

#turn on robot publishers
robot0_pub = rospy.Publisher("robot0_pub", Kiwi, queue_size = 10)
robot1_pub = rospy.Publisher("robot1_pub", Kiwi, queue_size = 10)
robot2_pub = rospy.Publisher("robot2_pub", Kiwi, queue_size = 10)
robot3_pub = rospy.Publisher("robot3_pub", Kiwi, queue_size = 10)
publishers=[robot0_pub, robot1_pub, robot2_pub, robot3_pub]
print "end of init"

def setGoal(event):
    canvas.coords(text,event.x,event.y)
    goalx = event.x
    goaly = event.y
    print "goal set: " + str(goalx) + ", " + str(goaly)
    canvas.unbind("<Button-1>")
    step(goalx, goaly)


canvas.bind("<Button-1>", setGoal)
canvas.pack()

def callback(data, robotnum):
	current_coords = canvas.coords(robots[robotnum])
	if current_coords[0] == 0:
		canvas.itemconfigure(robots[robotnum], state = 'normal')
		canvas.coords(robots[robotnum], data.x-58,data.y-58,data.x+58,data.y+58)
	#note: this will always have the most recently updated location information. 
	#For current simulation position, call "canvas.coords"
	cur_x = str(robotnum) + "_x"
	cur_y = str(robotnum) + "_y"
	cur_angle = str(robotnum) + "_angle"
	robot_data[cur_x] = data.x
	robot_data[cur_y] = data.y
	robot_data[cur_angle] = data.angle

def initializeRobot(num):
	alarmID = -1 
	if(num <= 3):
		robot_number = "robot" + str(num) + "_pos"
		robot_pos = rospy.Subscriber(robot_number, robot_position_msg, callback, num)
		canvas.pack()
		#print robot_number
		num +=1
		alarmID = root.after(100, initializeRobot, num)
	else:
		print "cancelling alarm"
		root.after_cancel(alarmID)
#####
#note: currently only finds the top right and measures, but this will cause problems eventually
#when the robots collide
#note2: Need to fix initialization process to consistently run using OpenCV because of the error
#note3: should create a class or struct called robot that contains simulation location,
#real location, whether it's reached it's goal,
#######

#publish to real world
def step(goalx, goaly):

	for index, robotID in enumerate(robots):
		coords = canvas.coords(robotID) #SIMULATED perfect position
		vectorx = goalx - ((coords[2] - coords[0])/2 + coords[0]) #simulated vector from center
		vectory = goaly - ((coords[3] - coords[1])/2 + coords[1])
		distFromGoal = abs(math.sqrt((vectorx)**2 + (vectory)**2))
		#print "vector" + str(vectorx) + ", " + str(vectory)

		kiwi = Kiwi()
		angle = robot_data[str(index) + "_angle"]
		vx = math.cos(angle)*distFromGoal
		vy = math.sin(angle)*distFromGoal

		#get porportion
		vx = vx / 800
		vy = vy / 600

		kiwi.w1 = vx * 100; #number is the duty cycle %. 100% when vx > 
		kiwi.w2 = -0.5 * vx - math.sqrt(1.5) * vy * 100;
		kiwi.w3 = -0.5 * vx + math.sqrt(1.5) * vy * 100;
		#print "kiwi---" + str(kiwi.w1) + ", " + str(kiwi.w2) + ", " + str(kiwi.w3)
		publishers[index].publish(kiwi)

		if(distFromGoal < 100):
			print "reached Goal: " + str(robotID)
		else:
			#initial draw for simulated step 
			canvas.move(robotID, vectorx*.01, vectory*.01) 
			cur_x = robot_data[str(index) + "_x"]
			cur_y = robot_data[str(index) + "_y"]
			#canvas redraws what opencv sees, COMMENT IF NO CAMERA ATTACHED
			#canvas.coords(robotID, cur_x-10, cur_y-10, cur_x+10, cur_y+10)
			canvas.pack()
	root.after(200, step, goalx, goaly)

print "about to call updateRobot"
initializeRobot(0)

root.mainloop()