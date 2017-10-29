import messages

class Intro:
    intro_message_1_location_y = 250
    intro_message_2_location_y = 500
    intro_message_3_location_y = 600
    intro_message_4_location_y = 800
    intro_message_spaceship_location_y = 900
    intro_message_spaceman_location_y = 1000

def playIntroMessages(screen, location_x):
    messages.displayIntroMessageOne(screen, location_x, Intro.intro_message_1_location_y)
    messages.displayIntroMessageTwo(screen, location_x, Intro.intro_message_2_location_y)
    messages.displayIntroMessageThree(screen, location_x, Intro.intro_message_3_location_y)
    messages.displayIntroMessageFour(screen, location_x, Intro.intro_message_4_location_y)
    #Pink is spaceship
    messages.displayIntroMessageSpaceship(screen, location_x, Intro.intro_message_spaceship_location_y)
    #Blue is spaceman
    messages.displayIntroMessageSpaceman(screen, location_x, Intro.intro_message_spaceman_location_y)

    messages.displayPlayer1Message(screen, 600, 650)
    messages.displayPlayer2Message(screen, 850, 650)

    Intro.intro_message_1_location_y -= 1
    Intro.intro_message_2_location_y -= 1
    Intro.intro_message_3_location_y -= 1

    if Intro.intro_message_4_location_y > 250:
        Intro.intro_message_4_location_y -= 1
        Intro.intro_message_spaceship_location_y -= 1
        Intro.intro_message_spaceman_location_y -= 1
