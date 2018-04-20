class Robot:
	def __init__(self):
		self.irl_x = -1
		self.irl_y = -1
		self.irl_angle = 0
		self.publisher = None
		self.robotShapeID = 0
		self.collsion_buffer = 0
		self.reachedGoal = False

"""notes: 
1. Needs collision avoidance (currently only works for very specific cases when the robots dont
run into each other)
2. Feedback loop that helps control the robots running around"""
