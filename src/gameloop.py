import pygame

pygame.init()

size = (700, 500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("KEEP TALKING AND NOBODY EXPLODES 2")

done = False
clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill((255,255,255))
	pygame.display.flip()
	clock.tick(60)
	
