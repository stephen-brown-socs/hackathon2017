import messages

class Intro:
    intro_message_1_location_y = 250
    intro_message_2_location_y = 500
    intro_message_3_location_y = 600
    intro_message_4_location_y = 800

def playIntroMessages(screen, location_x):
    messages.displayIntroMessageOne(screen, location_x, Intro.intro_message_1_location_y)
    messages.displayIntroMessageTwo(screen, location_x, Intro.intro_message_2_location_y)
    messages.displayIntroMessageThree(screen, location_x, Intro.intro_message_3_location_y)
    messages.displayIntroMessageFour(screen, location_x, Intro.intro_message_4_location_y)

    Intro.intro_message_1_location_y -= 1
    Intro.intro_message_2_location_y -= 1
    Intro.intro_message_3_location_y -= 1

    if Intro.intro_message_4_location_y > 250:
        Intro.intro_message_4_location_y -= 1
