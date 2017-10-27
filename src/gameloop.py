import pygame
import intro
from random import randint

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

batteryImg = pygame.image.load("battery.png")
batteryImg = pygame.transform.scale(batteryImg,(150,150))
battery_x = randint(0, 1000)
battery_y = randint(0, 500)

sightsImg = pygame.image.load("sights.png")
sightsImg = pygame.transform.scale(sightsImg,(150,150))
sights_x = randint(0, 1000)
sights_y = randint(0, 500)

pillImg = pygame.image.load("pill.png")
pillImg = pygame.transform.scale(pillImg,(150,150))
pill_x = randint(0, 1000)
pill_y = randint(0, 500)

gateImg = pygame.image.load("gate.png")
gateImg = pygame.transform.scale(gateImg,(150,150))
gate_x = randint(0, 1000)
gate_y = randint(0, 500)

lightningImg = pygame.image.load("lightning.png")
lightningImg = pygame.transform.scale(lightningImg,(150,150))
lightning_x = randint(0, 1000)
lightning_y = randint(0, 500)

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
    screen.blit(batteryImg, (battery_x, battery_y))
    screen.blit(pillImg, (pill_x, pill_y))
    screen.blit(lightningImg, (lightning_x, lightning_y))
    screen.blit(sightsImg, (sights_x, sights_y))
    screen.blit(gateImg, (gate_x, gate_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()