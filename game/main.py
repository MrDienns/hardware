from sense_hat import SenseHat
from time import sleep
from random import choice

# CREATE a sense object
sense = SenseHat()

# Set up the colours (white, green, red, empty)

w = (150, 150, 150)
g = (0, 255, 0)
r = (255, 0, 0)
e = (0, 0, 0)

# Create images for three different coloured arrows

arrow = [
    e, e, e, w, w, e, e, e,
    e, e, w, w, w, w, e, e,
    e, w, e, w, w, e, w, e,
    w, e, e, w, w, e, e, w,
    e, e, e, w, w, e, e, e,
    e, e, e, w, w, e, e, e,
    e, e, e, w, w, e, e, e,
    e, e, e, w, w, e, e, e
]

arrow_red = [
    e, e, e, r, r, e, e, e,
    e, e, r, r, r, r, e, e,
    e, r, e, r, r, e, r, e,
    r, e, e, r, r, e, e, r,
    e, e, e, r, r, e, e, e,
    e, e, e, r, r, e, e, e,
    e, e, e, r, r, e, e, e,
    e, e, e, r, r, e, e, e
]

arrow_green = [
    e, e, e, g, g, e, e, e,
    e, e, g, g, g, g, e, e,
    e, g, e, g, g, e, g, e,
    g, e, e, g, g, e, e, g,
    e, e, e, g, g, e, e, e,
    e, e, e, g, g, e, e, e,
    e, e, e, g, g, e, e, e,
    e, e, e, g, g, e, e, e
]

# Set a variable pause to 3 (the initial time between turns)
# Set variables score and angle to 0
# Create a variable called play set to True (this will be used to stop the game later)
pause = 3
score = 0
angle = 0
play = True

def start():
    sense.show_message("Start")
    play()

def play():
    global score
    global angle
    global pause
    global play
    while play:

        # CHOOSE a new random angle
        last_angle = angle
        while angle == last_angle:
            angle = choice([0, 90, 180, 270])

        sense.set_rotation(angle)

        # DISPLAY the white arrow
        sense.set_pixels(arrow)

        # SLEEP for current pause length
        sleep(pause)

        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = round(x, 0)
        y = round(y, 0)

        correct = check_orientation(x, y)
        display_orientation(correct)
        if correct:
            score += 1
        else:
            sleep(0.5)
            game_over()

        # Shorten the pause duration slightly
        pause = pause * 0.75

        # Pause before the next arrow
        sleep(0.5)

def check_orientation(x, y):
    if y == -1 and angle == 180:
        return True
    elif y == 1 and angle == 0:
        return True
    elif x == -1 and angle == 90:
        return True
    elif x == 1 and angle == 270:
        return True
    else:
        return False

def display_orientation(correct):
    if correct:
        sense.set_pixels(arrow_green)
    else:
        sense.set_pixels(arrow_red)

def game_over():
    global play
    play = False
    sense.show_message(str(score))

start()