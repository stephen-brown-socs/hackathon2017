import pygame

BLACK = (0,0,0)
RED = (255,0,0)

pygame.init()
font = pygame.font.SysFont('Calibri', 25, True, False)
ending_font = pygame.font.SysFont('Calibri', 50, True, False)

def displayIntroMessageOne(screen, x_location, y_location):
	text = font.render("HELLO SHAUNALD, NEVER GIVE UP", True, BLACK)
	screen.blit(text, [x_location, y_location])

def displayIntroMessageTwo(screen, x_location, y_location):
	text = font.render("THE SPACESHIP WILL GUIDE YOU", True, BLACK)
	screen.blit(text, [x_location, y_location])

def displayIntroMessageThree(screen, x_location, y_location):
	text = font.render("FIND YOUR WAY TO THE TRUE PATH", True, RED)
	screen.blit(text, [x_location, y_location])

def displayIntroMessageFour(screen, x_location, y_location):
	text = font.render("PRESS Z TO BEGIN", True, BLACK)
	screen.blit(text, [x_location, y_location])
	
#Bind this to somewhere on the game screen with white font, maybe top right corner	
def displayEndingMessage(screen, x_location, y_location):
	text = ending_font.render("YOU ARE WINNER", True, RED)
	screen.blit(text, [x_location, y_location])

def displayQuitMessage(screen, x_location, y_location):
	text = ending_font.render("PRESS Z TO QUIT", True, BLACK)
	screen.blit(text, [x_location, y_location])