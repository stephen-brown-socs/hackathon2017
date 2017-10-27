import pygame
import intro

pygame.init()

# Colour Definitions
WHITE = (255, 255, 255)
BLACK = (0,0,0)

screen_size = (1200, 720)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("KEEP TALKING AND NOBODY EXPLODES 2")

intro_done = False
game_done = False
clock = pygame.time.Clock()

jeremy_location_x = 100
jeremy_location_y = 100
bg_x = 600
bg_y = 360

jeremyImage = pygame.image.load("jeremy.jpg")
bgImage = pygame.image.load("circuitboard.jpg")
bgImage = pygame.transform.scale(bgImage,(1200,720))

while not intro_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro_done = True
            game_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                intro_done = True
             

    screen.fill(WHITE)

    screen.blit(jeremyImage, (jeremy_location_x, jeremy_location_y))
    intro.playIntroMessages(screen, 250)

    jeremy_location_x += 3
    jeremy_location_y += 3

    pygame.display.flip()
    clock.tick(60)

while not game_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                game_done = True   

    screen.fill(BLACK)

    screen.blit(bgImage, (0,0))
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()