from random import randint
import pygame

RANDOM_X_MIN = 0
RANDOM_X_MAX = 1000

RANDOM_Y_MIN = 0
RANDOM_Y_MAX = 500

def random_x():
    return randint(RANDOM_X_MIN, RANDOM_X_MAX)

def random_y():
    return randint(RANDOM_Y_MIN, RANDOM_Y_MAX)

class Images:

    # Intro Images
    jeremyImage = pygame.image.load("images/jeremy.jpg")
    jeremy_x = 100
    jeremy_y = 100

    # Main Game Images
    spaceshipImg = pygame.image.load("images/spaceship.png")
    spaceshipImg = pygame.transform.scale(spaceshipImg, (150, 150))
    spaceship_x = randint(0, 1000)
    spaceship_y = randint(0, 500)

    batteryImg = pygame.image.load("images/battery.png")
    battery_x = randint(0,1000)
    battery_y = randint(0, 500)

    sightsImg = pygame.image.load("images/sights.png")
    #sightsImg = pygame.transform.scale(sightsImg, (150, 150))
    sights_x = randint(0, 1000)
    sights_y = randint(0, 500)

    pillImg = pygame.image.load("images/pill.png")
    pillImg = pygame.transform.scale(pillImg, (150, 120))
    pill_x = randint(0, 1000)
    pill_y = randint(0, 500)

    gateImg = pygame.image.load("images/gate.png")
    gateImg = pygame.transform.scale(gateImg, (150, 70))
    gate_x = randint(0, 1000)
    gate_y = randint(0, 500)

    lightningImg = pygame.image.load("images/lightning.png")
    #lightningImg = pygame.transform.scale(lightningImg, (150, 150))
    lightning_x = randint(0, 1000)
    lightning_y = randint(0, 500)

    manImg = pygame.image.load("images/man.png")
    manImg = pygame.transform.scale(manImg, (150, 150))
    man_x = randint(0, 1000)
    man_y = randint(0, 500)

    bgImage = pygame.image.load("images/circuitboard.jpg")
    bgImage = pygame.transform.scale(bgImage, (1200, 720))
    bg_x = 0
    bg_y = 0

def displayIntroImages(screen):
    Images.jeremy_x += 3
    Images.jeremy_y += 3

    screen.blit(Images.jeremyImage, (Images.jeremy_x, Images.jeremy_y))

def displayMainGameImages(screen):
    screen.blit(Images.bgImage, (Images.bg_x, Images.bg_y))
    screen.blit(Images.spaceshipImg, (Images.spaceship_x, Images.spaceship_y))
    screen.blit(Images.batteryImg, (Images.battery_x, Images.battery_y))
    screen.blit(Images.pillImg, (Images.pill_x, Images.pill_y))
    screen.blit(Images.manImg, (Images.man_x, Images.man_y))
    screen.blit(Images.sightsImg, (Images.sights_x, Images.sights_y))
    screen.blit(Images.gateImg, (Images.gate_x, Images.gate_y))