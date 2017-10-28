import pygame
import random
import intro
import images
import messages
import lives
import sprites

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
ending_done = False
clock = pygame.time.Clock()

projectile_list = pygame.sprite.Group()

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
        if images.Images.spaceship_y >= 4:
            images.Images.spaceship_y -= 4
    if keys[pygame.K_s]:
    	#Limiting to SCREEN_HEIGHT - 4 still allows image to go offscreen for some reason
    	#Artifical limit set
        if images.Images.spaceship_y <= 550:
            images.Images.spaceship_y += 4
            print(images.Images.spaceship_y)
    if keys[pygame.K_a]:
        if images.Images.man_x >= -32:
            images.Images.man_x -= 4
            print(images.Images.man_x)
    if keys[pygame.K_d]:
    	#Limiting to SCREEN_WIDTH - 4 still allows image to go offscreen for some reason
    	#Artificial limit set
        if images.Images.man_x <= 1080:
            images.Images.man_x += 4
            print(images.Images.man_x)

    # Player 2 Controls
    if keys[pygame.K_i]:
        if images.Images.man_y >= 4:
            images.Images.man_y -= 4
    if keys[pygame.K_k]:
    	#Limiting to SCREEN_HEIGHT - 4 still allows image to go offscreen for some reason
    	#Artifical limit set
        if images.Images.man_y <= 550:
            images.Images.man_y += 4
    if keys[pygame.K_j]:
        if images.Images.spaceship_x >= -32:
            images.Images.spaceship_x -= 4
    if keys[pygame.K_l]:
    	#Limiting to SCREEN_WIDTH - 4 still allows image to go offscreen for some reason
    	#Artificial limit set
        if images.Images.spaceship_x <= 1080:
            images.Images.spaceship_x += 4


    #roll to spawn a projectile
    if random.randint(0,130) == 1:
        projectile_list.add(sprites.Projectile())

    #move projectiles
    for p in projectile_list:
        p.move(1)
        if p.rect.y > 720:
            projectile_list.remove(p)
        #collisionMan = p.checkCollision(images.Images.manImg)
        #collisionShip = p.checkCollision(images.Images.spaceshipImg)
        #if collisionMan or collisionShip:
        #    print "Collision!"



    #TODO decrement Lives.lives_count when hit

    screen.fill(BLACK)


    images.displayMainGameImages(screen)
    lives.displayLives(screen)
    projectile_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)


while not ending_done:
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

pygame.quit()
