import pygame
from random import randint, randrange


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship, self).__init__()

        img = pygame.image.load("images/spaceship.png")
        self.image = pygame.transform.scale(img, (150, 150))

        self.rect = self.image.get_rect()

        self.rect.x = randint(0, 500)
        self.rect.y = randint(0, 250)

class Spaceman(pygame.sprite.Sprite):
    #and his name is Mill Burray, the greatest hero mankind has ever known
    def __init__(self):
        super(Spaceman, self).__init__()

        img = pygame.image.load("images/man.png")
        self.image = pygame.transform.scale(img, (150, 150))

        self.rect = self.image.get_rect()
        self.rect.x = randint(500,1000)
        self.rect.y = randint(250,500)

    def moveX(self, speed):
        self.rect.x = self.rect.x + speed

    def moveY(self, speed):
        self.rect.y = self.rect.y + speed

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super(Projectile, self).__init__()

        img = pygame.image.load("images/java.png")
        self.image = pygame.transform.scale(img, (100, 100))

        self.rect = self.image.get_rect()

        self.rect.x = randrange(0, 1100)
        self.rect.y = -100

    def move(self, projectile_speed):
        self.rect.y += projectile_speed

    def checkCollision(self, rect):
        return self.rect.colliderect(rect)