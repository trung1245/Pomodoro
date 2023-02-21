import pygame
import sys

from textbutton import TextButton
from timebar import TimeBar
from setting import Setting
import functions as fc

def main():

	pygame.init()
	p_settings = Setting() 
	screen = pygame.display.set_mode((p_settings.WIDTH,p_settings.HEIGHT))
	pygame.display.set_caption('Pomodoro')
	pygame.display.set_icon(pygame.image.load("E:/2. App/Dropbox/2. Study/1.Code/Pomodoro/icon.ico"))
	sound = pygame.mixer.Sound("E:/2. App/Dropbox/2. Study/1.Code/Pomodoro/ring-ring.wav")
	clock = pygame.time.Clock()
	while p_settings.run:
		screen.fill(p_settings.colors[0])
		clock.tick(p_settings.FPS)

		if p_settings.steps == 0:
			#user input loop
			p_settings.total_loop,p_settings.steps = fc.user_enter(p_settings, screen, "loops",p_settings.MAX_LOOP,p_settings.MIN_LOOP)
		elif p_settings.steps == 1 :
			p_settings.mins,p_settings.steps = fc.user_enter(p_settings, screen, "minutes",p_settings.MAX_MIN,p_settings.MIN_MIN)
			p_settings.change_time()
		else :
			TextButton(f"{p_settings.loop_number+1} loop",(int(p_settings.WIDTH/2)-50,150)).draw(False,False)
			TimeBar(int(p_settings.total_secs),(150,200)).draw(p_settings.colors[3],p_settings.total)
			TimeBar(int(p_settings.total_secs_break),(150,300)).draw(p_settings.colors[4],p_settings.total_break)
			#create start button
			start_button = TextButton("Start",(50,425))
			start_button.draw(True,True)
			#create reset button
			reset_button = TextButton("Reset",(850,425))
			reset_button.draw(True,True)
			if p_settings.pomodoro :
				if p_settings.total_secs > 0:
					p_settings.total_secs -= p_settings.TIME_PER_FPS

					if int(p_settings.total_secs) == 0:	
						fc.reset_loop(p_settings)
						p_settings.total_secs_break = p_settings.total_break
						pygame.mixer.Sound.play(sound)

				elif int(p_settings.total_secs) == 0 and p_settings.total_secs_break > 0:
					p_settings.total_secs_break -= p_settings.TIME_PER_FPS
					if int(p_settings.total_secs_break) == 0:
						p_settings.total_secs = p_settings.total
						pygame.mixer.Sound.play(sound)
						if p_settings.loop_number + 1 >= p_settings.total_loop:
							p_settings.pomodoro = False
						else :
							p_settings.loop_number += 1

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				p_settings.run = False
				sys.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					pygame.mixer.stop()
					if start_button.mouse_on_text():
						p_settings.pomodoro = True
					elif reset_button.mouse_on_text():
						p_settings.pomodoro = False
						loop = 0
						p_settings.total_secs = p_settings.total
						p_settings.total_secs_break = p_settings.total_break

		pygame.display.flip()
	pygame.quit()
main()