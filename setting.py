class Setting():

	def __init__(self):
		#main
		self.WIDTH = 1000
		self.HEIGHT = 500
		self.FPS = 60
		self.TIME_PER_FPS = 1000/self.FPS/1000
		self.colors = [[255,255,255],[120,120,120],[0,0,0],[10,255,100],[10,110,255]]
		#textbutton
		self.MAX_LOOP = 20
		self.MIN_LOOP = 1
		self.MAX_MIN = 50
		self.MIN_MIN = 5
		self.DISTANCE_X = 25
		self.DISTANCE_Y = 30
		self.COMFIRM_X = self.WIDTH - 100
		self.COMFIRM_Y = self.HEIGHT - 50
		self.dynamic_settings()

	def dynamic_settings(self):
		#main
		self.run = True
		self.steps = 0
		self.pomodoro = False
		#loop
		self.loop_number = 0
		self.total_loop = 4
		self.mins = 25
		self.total = 0
		self.total_secs = 0
		self.total_break = 300
		self.total_secs_break = 300
	
	def change_time(self):
		self.total = self.mins*60
		self.total_secs = self.mins*60
	

