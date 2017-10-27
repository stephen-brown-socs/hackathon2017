import pygame
import messages

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

jeremy_location_x = 100
jeremy_location_y = 100

jeremyImage = pygame.image.load("jeremy.jpg")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill((255,255,255))

	screen.blit(jeremyImage, (jeremy_location_x, jeremy_location_y))
	
	messages.displayIntroMessageOne(screen, 250, text_location_1_y)
	messages.displayIntroMessageTwo(screen, 250, text_location_2_y)
	messages.displayIntroMessageThree(screen, 250, text_location_3_y)

	text_location_1_y -= 1
	text_location_2_y -= 1
	text_location_3_y -= 1
	jeremy_location_x += 3
	jeremy_location_y =+ 3

	pygame.display.flip()
	clock.tick(60)
	
pygame.quit()
