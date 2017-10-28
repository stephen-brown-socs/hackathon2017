import pygame
import random


class Projectile(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Projectile, self).__init__()

        img = pygame.image.load("images/java.png")
        self.image = pygame.transform.scale(img, (width, height))

        self.rect = self.image.get_rect()

    def move(self, projectile_speed):
        self.rect.y += projectile_speed