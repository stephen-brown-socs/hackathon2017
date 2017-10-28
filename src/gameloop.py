import pygame
import intro
import images

pygame.init()

# Colour Definitions
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# Other Configuration Options
screen_size = (1200, 720)
game_title = "KEEP TALKING AND NOBODY EXPLODES 2"


screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(game_title)

intro_done = False
game_done = False
clock = pygame.time.Clock()



while not intro_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro_done = True
            game_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                intro_done = True
             

    screen.fill(WHITE)
    images.displayIntroImages(screen)
    intro.playIntroMessages(screen, 250)

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

    images.displayMainGameImages(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()