import pygame

class TextButton:
	def __init__(self,p_settings,screen , text, position):
		self.p_settings = p_settings
		self.screen = screen
		self.text = str(text)
		self.position = position
		self.font = pygame.font.SysFont('sans',22)
		self.word_color = self.p_settings.colors[2]
		self.word_color2 = self.p_settings.colors[1]

	def mouse_on_text(self):
		text_render = self.font.render(self.text, True,self.word_color)
		self.text_box = text_render.get_rect()
		self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
		if self.mouse_x > self.position[0] -5 and self.mouse_x < self.position[0] + 5 + self.text_box[2] and self.mouse_y > self.position[1] and self.mouse_y < self.position[1] + self.text_box[3]:
			return True
		else:
			return False

	def draw(self,box,touch):
		text_render = self.font.render(self.text, True,self.word_color)
		if self.mouse_on_text() and touch:
			text_render = self.font.render(self.text, True,self.word_color2)
		text_box = text_render.get_rect()
		before, after = self.position[0]-15,30+text_box[2]
		if box:
			pygame.draw.rect(self.screen,self.word_color,(before,self.position[1],after,text_box[3]),2)
		self.screen.blit(text_render,self.position)
		return before, after