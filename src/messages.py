import pygame

BLACK = (0,0,0)
RED = (255,0,0)

pygame.init()
font = pygame.font.SysFont('Calibri', 25, True, False)

def displayIntroMessageOne(screen, x_location, y_location):
	text = font.render("HELLO SHAUNALD, NEVER GIVE UP", True, BLACK)
	screen.blit(text, [x_location, y_location])

def displayIntroMessageTwo(screen, x_location, y_location):
	text = font.render("JEREMY SINGER WILL GUIDE YOU", True, BLACK)
	screen.blit(text, [x_location, y_location])

def displayIntroMessageThree(screen, x_location, y_location):
	text = font.render("FIND YOUR WAY TO THE TRUE PATH", True, RED)
	screen.blit(text, [x_location, y_location])
