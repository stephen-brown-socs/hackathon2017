import pygame

pygame.init()

size = (700, 500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("KEEP TALKING AND NOBODY EXPLODES 2")

done = False
clock = pygame.time.Clock()

text_location_x = 250
text_location_y = 250

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill((255,255,255))
	
	font = pygame.font.SysFont('Calibri', 25, True, False)
	text = font.render("HELLO SHAUNALD. NEVER GIVE UP\n\n\n\n\n\n\n\n\n\n", True, (0,0,0))
	screen.blit(text, [text_location_x, text_location_y])
	text_location_y -= 1

	pygame.display.flip()
	clock.tick(60)
	
pygame.quit()
