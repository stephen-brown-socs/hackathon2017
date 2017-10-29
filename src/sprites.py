import pygame
from random import randint, randrange


class Spaceship(pygame.sprite.Sprite):

    currentSprite = 0
    gif = []
    for i in range(0,5):
        gif.append(pygame.image.load("images/spaceship/spaceship_sprite" + str(i) + ".png"))

    def __init__(self):
        super(Spaceship, self).__init__()
        self.currentSprite = 0
        self.image = pygame.transform.scale(self.gif[self.currentSprite], (75, 75))
        self.rect = self.image.get_rect()

        self.rect.x = randint(0, 100)
        self.rect.y = randint(250, 500)

    def chooseSprite(self):
        self.currentSprite = (self.currentSprite + 1) % 5
        self.image = self.gif[self.currentSprite]

class Spaceman(pygame.sprite.Sprite):
    #and his name is Mill Burray, the greatest hero mankind has ever known

    #set up sprites]
    current_animation = "idle"
    current_sprite = 0
    run_left = []
    run_right = []
    idle = pygame.image.load("images/hazmat_man/hazmat_man_idle.png")

    for i in range(0,5):
        run_left.append(pygame.image.load("images/hazmat_man/run_left_sprite_" + str(i) + ".png"))
        run_right.append(pygame.image.load("images/hazmat_man/run_right_sprite_" + str(i) + ".png"))

    def __init__(self):
        super(Spaceman, self).__init__()

        img = pygame.image.load("images/man.png")
        self.image = pygame.transform.scale(img, (40, 75))

        self.rect = self.image.get_rect()
        self.rect.x = randint(900,1000)
        self.rect.y = randint(250,500)

    def chooseSprite(self, time):

        if self.current_animation == "run_left":
            self.image = self.run_left[self.current_sprite]
            if time == 0:
                self.current_sprite = (self.current_sprite + 1) % 5
        elif self.current_animation == "run_right":
            self.image = self.run_right[self.current_sprite]
            if time == 0:
                self.current_sprite = (self.current_sprite + 1) % 5
        else:
            self.image = self.idle
            self.current_sprite = 0

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