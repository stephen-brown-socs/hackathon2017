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
NUM_OBSTACLES = 15
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

# Setup sounds
explosion_sound = pygame.mixer.Sound("music/explosion.wav")
shock_sound = pygame.mixer.Sound("music/shock.wav")

# Start Music
pygame.mixer.music.load("music/ALL STAR.wav")
pygame.mixer.music.play()

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
time = 1
for x in range(0, NUM_OBSTACLES):
    obstacle = sprites.Obstacle()
    obstacle_list.add(obstacle)
    all_sprites.add(obstacle)

projectile_base_chance = 0

while not game_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_done = True
            ending_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_done = True
        #sorry about this one
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_a) or (event.key == pygame.K_d) or (event.key == pygame.K_i) or (event.key == pygame.K_k):
                spaceman.current_animation = "idle"

    # Player 1 Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if spaceship.rect.y >= 0:
            spaceship.rect.y -= 4
    if keys[pygame.K_s]:
        if spaceship.rect.y <= SCREEN_HEIGHT-50:
            spaceship.rect.y += 4
    if keys[pygame.K_a]:
        spaceman.current_animation = "run_left"
        if spaceman.rect.x >= 0:
            spaceman.rect.x -= 4
    if keys[pygame.K_d]:
        spaceman.current_animation = "run_right"
        if spaceman.rect.x <= SCREEN_WIDTH-40:
            spaceman.rect.x += 4

    # Player 2 Controls
    if keys[pygame.K_i]:
        if not keys[pygame.K_a]:
            spaceman.current_animation = "run_right"
        if spaceman.rect.y >= 4:
            spaceman.rect.y -= 4
    if keys[pygame.K_k]:
        if not keys[pygame.K_a]:
            spaceman.current_animation = "run_right"
        if spaceman.rect.y <= SCREEN_HEIGHT-80:
            spaceman.rect.y += 4
    if keys[pygame.K_j]:
        if spaceship.rect.x >= 4:
            spaceship.rect.x -= 4
    if keys[pygame.K_l]:
        if spaceship.rect.x  <= SCREEN_WIDTH-50:
            spaceship.rect.x += 4

    # Obstacle collision
    manObstacleCollision = pygame.sprite.spritecollide(spaceman, obstacle_list, True)
    shipObstacleCollision = pygame.sprite.spritecollide(spaceship, obstacle_list, True)

    if not (len(manObstacleCollision) == 0) or not (len(shipObstacleCollision) == 0):
        shock_sound.play()
        lives.Lives.lives_count -= 1
        if lives.Lives.lives_count == 0:
            game_done = True
            game_failed = True

    #roll to spawn a projectile
    if random.randint(0,130) == 1:
        proj = sprites.Projectile()
        projectile_list.add(proj)
        all_sprites.add(proj)
        projectile_base_chance = 0
    else:
        projectile_base_chance += 1

    #move projectiles
    for p in projectile_list:
        p.move(1)
        if p.rect.y > 720:
            projectile_list.remove(p)
        shipCollision = pygame.sprite.spritecollide(spaceship, projectile_list, True)

        manCollision = pygame.sprite.spritecollide(spaceman, projectile_list, True)
        if not (len(shipCollision) == 0) or not (len(manCollision) == 0):
            explosion_sound.play()
            lives.Lives.lives_count -= 1
            if lives.Lives.lives_count == 0:
                game_done = True
                game_failed = True

    spaceship.chooseSprite()
    time = (time + 1) % 10
    spaceman.chooseSprite(time)

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

pygame.mixer.music.stop()

if not game_failed:
    pygame.mixer.music.load("music/Victory.mp3")
    pygame.mixer.music.play()

shock_sound.stop()
explosion_sound.stop()
pygame.mixer.music.stop()

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

pygame.mixer.music.load("music/failure.mp3")
pygame.mixer.music.play()

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
