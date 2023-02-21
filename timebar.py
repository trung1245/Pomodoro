class TimeBar():
	def __init__(self,total_secs,position):
		self.total_secs = total_secs
		self.position = position
		self.font = pygame.font.SysFont("sans",22)

	def draw(self,color,total):
		ranges = 2
		rect_width = width - self.position[0]*2
		count_down = rect_width-ranges
		pygame.draw.rect(screen,colors[2],(self.position[0],self.position[1],rect_width,25),ranges)
		pygame.draw.rect(screen,color,(self.position[0]+ranges,self.position[1]+ranges,int(count_down*(self.total_secs/total)),24-ranges))
		mins = int(self.total_secs/60)
		secs = self.total_secs - mins*60
		text_render = f"{mins}:0{secs}"
		if secs > 9:
			text_render = f"{mins}:{secs}"
		text_time = self.font.render(text_render, True,colors[2])
		screen.blit(text_time,(int((width - self.position[0]/2)/2),self.position[1]))