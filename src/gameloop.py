import pygame

pygame.init()

size = (700, 500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("KEEP TALKING AND NOBODY EXPLODES 2")

done = False
clock = pygame.time.Clock()

text_location_1_x = 250
text_location_1_y = 250

text_location_2_x = 250
text_location_2_y = 500

text_location_3_x = 250
text_location_3_y = 600

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill((255,255,255))
	
	font = pygame.font.SysFont('Calibri', 25, True, False)
	text1 = font.render("HELLO SHAUNALD. NEVER GIVE UP", True, (0,0,0))
	screen.blit(text1, [text_location_1_x, text_location_1_y])

	text2 = font.render("JEREMY SINGER WILL GUIDE YOU", True, (0,0,0))
	screen.blit(text2, [text_location_2_x, text_location_2_y])

	text3 = font.render("FIND YOUR WAY TO THE TRUE PATH", True, (255,0,0))
	screen.blit(text3, [text_location_3_x, text_location_3_y])

	text_location_1_y -= 1
	text_location_2_y -= 1
	text_location_3_y -= 1

	pygame.display.flip()
	clock.tick(60)
	
pygame.quit()
