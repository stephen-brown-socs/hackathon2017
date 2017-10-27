import pygame
import messages

pygame.init()

# Colour Definitions
WHITE = (255, 255, 255)

screen_size = (700, 500)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("KEEP TALKING AND NOBODY EXPLODES 2")

done = False
clock = pygame.time.Clock()

intro_message_1_location_y = 250
intro_message_2_location_y = 500
intro_message_3_location_y = 600
intro_message_4_location_y = 800

jeremy_location_x = 100
jeremy_location_y = 100

jeremyImage = pygame.image.load("jeremy.jpg")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    screen.blit(jeremyImage, (jeremy_location_x, jeremy_location_y))

    messages.displayIntroMessageOne(screen, 250, intro_message_1_location_y)
    messages.displayIntroMessageTwo(screen, 250, intro_message_2_location_y)
    messages.displayIntroMessageThree(screen, 250, intro_message_3_location_y)
    messages.displayIntroMessageFour(screen, 250, intro_message_4_location_y)

    intro_message_1_location_y -= 1
    intro_message_2_location_y -= 1
    intro_message_3_location_y -= 1

    if intro_message_4_location_y > 250:
        intro_message_4_location_y -= 1

    jeremy_location_x += 3
    jeremy_location_y = + 3

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
