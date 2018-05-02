class Robot:
	def __init__(self, name):
		self.name = name
		self.irl_x = -1
		self.irl_y = -1
		self.irl_angle = 0
		self.frontx = -1
		self.fronty = -1
		self.publisher = None
		self.robotShapeID = -1
		self.collsion_buffer = 0
		self.reachedGoal = False
		self.agent = -1
		self.image = None
		self.button = None
		self.group = -1 #currently not used bc groups are kept track of locally
		self.toggled = False
		self.goalx = None
		self.goaly = None
		self.rotationimage = None


"""notes: 
1. Needs collision avoidance (currently only works for very specific cases when the robots dont
run into each other)
2. Feedback loop that helps control the robots running around"""
