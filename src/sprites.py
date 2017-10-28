import pygame
from random import randint, randrange


class Spaceship(pygame.sprite.Sprite):

    currentSprite = 0
    gif = []
    for i in range(0,5):
        print
        gif.append(pygame.image.load("images/spaceship/spaceship_sprite" + str(i) + ".png"))

    still = pygame.image.load("images/spaceship.png")
    moving = False

    def __init__(self):
        super(Spaceship, self).__init__()
        self.image = pygame.transform.scale(self.still, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = randint(0, 100)
        self.rect.y = randint(250, 500)

    def chooseSprite(self):
        if self.moving == False:
            self.image = self.still;
        if self.moving:
            self.image = self.gif[self.currentSprite]
            self.currentSprite = (self.currentSprite + 1) % 5

class Spaceman(pygame.sprite.Sprite):
    #and his name is Mill Burray, the greatest hero mankind has ever known
    def __init__(self):
        super(Spaceman, self).__init__()

        img = pygame.image.load("images/man.png")
        self.image = pygame.transform.scale(img, (80, 150))

        self.rect = self.image.get_rect()
        self.rect.x = randint(900,1000)
        self.rect.y = randint(250,500)

    def moveX(self, speed):
        self.rect.x = self.rect.x + speed

    def moveY(self, speed):
        self.rect.y = self.rect.y + speed

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super(Projectile, self).__init__()

        img = pygame.image.load("images/java.png")
        self.image = pygame.transform.scale(img, (50, 100))

        self.rect = self.image.get_rect()

        self.rect.x = randrange(0, 1100)
        self.rect.y = -100

    def move(self, projectile_speed):
        self.rect.y += projectile_speed

    def checkCollision(self, rect):
        return self.rect.colliderect(rect)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super(Obstacle, self).__init__()

        img = pygame.image.load("images/battery.png")
        self.image = pygame.transform.scale(img, (50, 25))

        self.rect = self.image.get_rect()

        self.rect.x = randrange(0, 1150)
        self.rect.y = randrange(0, 680)