import pygame

class WinCondition:
    frames_win_condition_held = 0
    frames_win_condition_max = 15

def checkWinCondition(spaceman, spaceship):
    winCollision = pygame.sprite.spritecollide(spaceman, [spaceship], False)

    if winCollision:
        WinCondition.frames_win_condition_held += 1

        if WinCondition.frames_win_condition_held >= WinCondition.frames_win_condition_max:
            return True
    else:
        WinCondition.frames_win_condition_held = 0

    return False
