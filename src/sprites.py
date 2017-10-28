import pygame
from random import randint, randrange


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship, self).__init__()

        spaceshipImg = pygame.image.load("images/spaceship.png")
        spaceshipImg = pygame.transform.scale(spaceshipImg, (150, 150))

        spaceship_x = randint(0, 1000)
        spaceship_y = randint(0, 500)

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
        return pygame.Rect.colliderect(rect)