BLACK = (0,0,0)
RED = (255,0,0)

import pygame

class Lives:
    lives_count = 3
    lives_block_x = 900
    lives_block_y = 600

    livesImg = pygame.image.load("images/life.png")
    livesImg = pygame.transform.scale(livesImg, (100, 100))

def displayLives(screen):

    # Draw each heart
    currentLivesPointer = Lives.lives_block_x
    if Lives.lives_count > 0:
        for x in range(0, Lives.lives_count):
            screen.blit(Lives.livesImg, (currentLivesPointer, Lives.lives_block_y))
            currentLivesPointer += 100
