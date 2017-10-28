import pygame
import intro
import images

pygame.init()

# Colour Definitions
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# Other Configuration Options
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
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

    # Player 1 Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if images.Images.battery_y >= 0:
            images.Images.battery_y -= 4
    if keys[pygame.K_s]:
        if images.Images.battery_y <= SCREEN_HEIGHT-4:
            images.Images.battery_y += 4
    if keys[pygame.K_a]:
        if images.Images.lightning_x >= 4:
            images.Images.lightning_x -= 4
    if keys[pygame.K_d]:
        if images.Images.lightning_x <= SCREEN_WIDTH-4:
            images.Images.lightning_x += 4

    # Player 2 Controls
    if keys[pygame.K_i]:
        if images.Images.lightning_y >= 4:
            images.Images.lightning_y -= 4
    if keys[pygame.K_k]:
        if images.Images.lightning_y <= SCREEN_HEIGHT-4:
            images.Images.lightning_y += 4
    if keys[pygame.K_j]:
        if images.Images.battery_x >= 4:
            images.Images.battery_x -= 4
    if keys[pygame.K_l]:
        if images.Images.battery_x <= SCREEN_WIDTH-4:
            images.Images.battery_x += 4


    screen.fill(BLACK)

    images.displayMainGameImages(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()