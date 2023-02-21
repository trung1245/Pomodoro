import pygame
from textbutton import TextButton

def user_enter(p_settings,screen,user_enter,maxs,mins):
	next_step = lambda x : x + 1

	TextButton(p_settings, screen,f"enter your {user_enter} :",between(p_settings,0,-p_settings.DISTANCE_Y)).draw(False,False)
	loop_numbers = TextButton(p_settings, screen,p_settings.loop_number,between(p_settings))
	before, after = loop_numbers.draw(True,False)
	plus_button = TextButton(p_settings,screen,"+",between(p_settings,after))
	subtract_button = TextButton(p_settings,screen,"-",between(p_settings,before))
	print(after,before)
	plus_button.draw(True,True)
	subtract_button.draw(True,True)
	confirm_loop = TextButton(p_settings,screen,"confirm",(p_settings.COMFIRM_X,p_settings.COMFIRM_Y))
	confirm_loop.draw(True,True)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.display.quit()
			exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if plus_button.mouse_on_text() and p_settings.loop_number < maxs:
					p_settings.loop_number += 1
				elif subtract_button.mouse_on_text() and p_settings.loop_number > mins:
					p_settings.loop_number -= 1
				elif confirm_loop.mouse_on_text() :
					return p_settings.loop_number,next_step(p_settings.steps)+1
	return p_settings.loop_number,p_settings.steps

def reset_loop(p_settings):
	if (p_settings.loop_number + 1) % 4 == 0:
		p_settings.total_break = p_settings.total_break*4
		p_settings.total_secs_break = p_settings.total_break
	else :
		p_settings.total_break = 300

def between(p_settings,distance_x = 0,distance_y = 0):
	return (p_settings.WIDTH/2 +distance_x, p_settings.HEIGHT/2 + distance_y)