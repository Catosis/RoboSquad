#!/usr/bin/env python

import Tkinter
import tkMessageBox
import rospy
from squad.msg import robot_position_msg
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
goalx = goaly = None  
global robot_pos
print "end of init"

def setGoal(event):
    """print "clicked at", event.x, event.y
    text = canvas.create_text(event.x,event.y)
    print text"""
    canvas.coords(text,event.x,event.y)
    goalx = event.x
    goaly = event.y
    print "goal set" + str(goalx) + str(goaly)
    canvas.unbind("<Button-1>")
    step(goalx, goaly)


canvas.bind("<Button-1>", setGoal)
canvas.pack()

def callback(data, robotnum):
	current_coords = canvas.coords(robots[robotnum])
	if current_coords[0] == 0:
		canvas.itemconfigure(robots[robotnum], state = 'normal')
		canvas.coords(robots[robotnum], data.x-10,data.y-10,data.x+10,data.y+10)

def updateRobot(num):
	alarmID = -1 
	if(num <= 3):
		robot_number = "robot" + str(num) + "_pos"
		robot_pos = rospy.Subscriber(robot_number, robot_position_msg, callback, num)
		canvas.pack()
		#print robot_number
		num +=1
		alarmID = root.after(100, updateRobot, num)
	else:
		print "cancelling alarm"
		root.after_cancel(alarmID)

#note: currently only finds the top right and measures, but this will cause problems eventually
#when the robots collide
def step(goalx, goaly):
	for robotID in robots:
		coords = canvas.coords(robotID)
		xfactor = goalx - coords[0]+58 #.2 is an arbitrary factor to increase speed at distance
		yfactor = goaly - coords[3]+58
		distFromGoal = abs(math.sqrt(xfactor**2 + yfactor**2))
		print str(goalx) + " y:" + str(goaly)
		print str(coords[0]) + " coords " + str(coords[1])
		if(distFromGoal < 300):
			print "reached Goal" + str(robotID) + " dist: " + str(distFromGoal)
		else:
			print("moving")
			canvas.move(robotID, xfactor*0.05, yfactor*0.05) 
			canvas.pack()
	canvas.bind("<Button-1>", setGoal)
	root.after(500, step, goalx, goaly)

print "about to call updateRobot"
updateRobot(3)

root.mainloop()