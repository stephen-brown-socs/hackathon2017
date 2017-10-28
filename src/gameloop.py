import pygame
import random
import intro
import images
import messages
import lives
import win_condition
import sprites

pygame.init()

# Colour Definitions
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# Other Configuration Options
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
NUM_OBSTACLES = 25
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
game_title = "FRIENDSHIP KILLER 2: ELECTRIC BOOGALOO"

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(game_title)

intro_done = False
game_done = False
ending_done = False
game_failed = False
clock = pygame.time.Clock()

#sprites
#all_sprites list there so all sprites can be drawn with a single call
all_sprites = pygame.sprite.Group()
projectile_list = pygame.sprite.Group()

spaceship = sprites.Spaceship()
all_sprites.add(spaceship)

spaceman = sprites.Spaceman()
all_sprites.add(spaceman)

obstacle_list = pygame.sprite.Group()


while not intro_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro_done = True
            game_done = True
            ending_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                intro_done = True

    screen.fill(WHITE)
    images.displayIntroImages(screen)

    intro.playIntroMessages(screen, 250)

    pygame.display.flip()
    clock.tick(60)

# Spawn Obstacles
for x in range(0, 10):
    obstacle = sprites.Obstacle()
    obstacle_list.add(obstacle)
    all_sprites.add(obstacle)

while not game_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_done = True
            ending_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_done = True

    # Player 1 Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if spaceship.rect.y >= 0:
            spaceship.rect.y -= 4
    if keys[pygame.K_s]:
        if spaceship.rect.y <= SCREEN_HEIGHT-150:
            spaceship.rect.y += 4
    if keys[pygame.K_a]:
        if spaceman.rect.x >= 0:
            spaceman.rect.x -= 4
    if keys[pygame.K_d]:
        if spaceman.rect.x <= SCREEN_WIDTH-80:
            spaceman.rect.x += 4

    # Player 2 Controls
    if keys[pygame.K_i]:
        if spaceman.rect.y >= 4:
            spaceman.rect.y -= 4
    if keys[pygame.K_k]:
        if spaceman.rect.y <= SCREEN_HEIGHT-150:
            spaceman.rect.y += 4
    if keys[pygame.K_j]:
        if spaceship.rect.x >= 4:
            spaceship.rect.x -= 4
    if keys[pygame.K_l]:
        if spaceship.rect.x  <= SCREEN_WIDTH-150:
            spaceship.rect.x += 4


    #roll to spawn a projectile
    if random.randint(0,60) == 1:
        proj = sprites.Projectile()
        projectile_list.add(proj)
        all_sprites.add(proj)

    #move projectiles
    for p in projectile_list:
        p.move(1)
        if p.rect.y > 720:
            projectile_list.remove(p)
        shipCollision = pygame.sprite.spritecollide(spaceship, projectile_list, True)

        manCollision = pygame.sprite.spritecollide(spaceman, projectile_list, True)
        if not (len(shipCollision) == 0) or not (len(manCollision) == 0):
            lives.Lives.lives_count -= 1
            if lives.Lives.lives_count == 0:
                game_done = True
                game_failed = True


    # Check if we've won
    has_won = win_condition.checkWinCondition(spaceman, spaceship)
    if has_won:
        game_done = True

    screen.fill(BLACK)

    images.displayMainGameImages(screen)
    lives.displayLives(screen)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)


while not ending_done and not game_failed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ending_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                ending_done = True

    screen.fill(WHITE)
    messages.displayEndingMessage(screen, 250, 250)
    messages.displayQuitMessage(screen,250, 500)
    pygame.display.flip()
    clock.tick(60)

while game_failed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_failed = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                game_failed = False

    screen.fill(WHITE)
    messages.displayGameOverMessage(screen, 250, 250)
    messages.displayQuitMessage(screen, 250, 500)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
