import pygame
import random
import intro
import images
import messages
import lives
import win_condition
import sprites
import sys
import subprocess
import socket


#local flag checks if game is being played on one machine
#False if being played over a network on two machines
local = True

#Player select
p1 = False
p2 = False

errorstring = "\nInvalid input - please use one of the following commands instead:\npython3 gameloop.py -> launches game locally for both players\npython3 gameloop.py (-n | lan ) (p1 | p2) -> launches game over LAN as player 1 or player 2 respectively\n"

#Check if additional argument is present
try:
    if sys.argv[1] == "lan" or sys.argv[1] == "-n":
        local = False
        try:
            if sys.argv[2] == "p1":
                p1 = True
            elif sys.argv[2] == "p2":
                p2 = True
        except:
            print(errorstring)
            pygame.quit()
    else:
        print(errorstring)
        pygame.quit()
except:
	pass
		
print("Local check: ", local)

#Set up sockets
try:
    #Obtain LAN address
    addr = subprocess.check_output("hostname -I", shell=True)
    print(addr.strip())
    s = socket.socket()
    s.bind((addr.strip(), 11000))
    print(s)
except:
    print("Socket creation failed - try running in local mode.")
    pygame.quit()

#If networked mode and p1 selected, listen for connection from p2
if p1:
    s.listen(1)
    print("Listening for connection from p2...")
    while True:
        c, addr = s.accept()
#If p2, connect to other player on network
elif p2:
    peer_addr = input("Please enter the address of co-op partner (should be displayed on their console)")
    try:
        s.connect((peer_addr, 11000))
    except:
        print("Connection failed - try running in local mode.")
        pygame.quit()
    

#Start the game!
pygame.init()

# Colour Definitions
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# Other Configuration Options
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
NUM_OBSTACLES = 20
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
for x in range(0, NUM_OBSTACLES):
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
    #Player 1 controls only enabled if local mode enabled or p1 selected in networked mode
    #P1 sends to c
    keys = pygame.key.get_pressed()
    if local or p1:
        if keys[pygame.K_w]:
            if spaceship.rect.y >= 0:
                spaceship.rect.y -= 4
                spaceship.moving = True
        if keys[pygame.K_s]:
            if spaceship.rect.y <= SCREEN_HEIGHT-150:
                spaceship.rect.y += 4
                spaceship.moving = True
        if keys[pygame.K_a]:
            if spaceman.rect.x >= 0:
                spaceman.rect.x -= 4
        if keys[pygame.K_d]:
            if spaceman.rect.x <= SCREEN_WIDTH-80:
                spaceman.rect.x += 4
        
    #Player 2 controls in IKJL format only enabled if local mode enabled
    if local:
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
                spaceship.moving = True
        if keys[pygame.K_l]:
            if spaceship.rect.x  <= SCREEN_WIDTH-150:
                spaceship.rect.x += 4
                spaceship.moving = True
    
    #Player 2 controls in WASD format only enabled if network mode enabled and p2 selected
    #P2 sends stuff over s
    if p2:
        if keys[pygame.K_w]:
            if spaceman.rect.y >= 4:
                spaceman.rect.y -= 4
        if keys[pygame.K_s]:
            if spaceman.rect.y <= SCREEN_HEIGHT-150:
                spaceman.rect.y += 4
        if keys[pygame.K_a]:
            if spaceship.rect.x >= 4:
                spaceship.rect.x -= 4
                spaceship.moving = True
        if keys[pygame.K_d]:
            if spaceship.rect.x  <= SCREEN_WIDTH-150:
                spaceship.rect.x += 4
                spaceship.moving = True

    # Obstacle collision
    manObstacleCollision = pygame.sprite.spritecollide(spaceman, obstacle_list, True)
    shipObstacleCollision = pygame.sprite.spritecollide(spaceship, obstacle_list, True)

    if not (len(manObstacleCollision) == 0) or not (len(shipObstacleCollision) == 0):
        lives.Lives.lives_count -= 1
        if lives.Lives.lives_count == 0:
            game_done = True
            game_failed = True

    #roll to spawn a projectile
    if random.randint(0,130) == 1:
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
            explosion_sound.play()
            lives.Lives.lives_count -= 1
            if lives.Lives.lives_count == 0:
                game_done = True
                game_failed = True

    spaceship.chooseSprite()

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

if not local:
    #Close connection
    s.close()

pygame.quit()
