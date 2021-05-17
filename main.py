import pygame as pg

# reference - https://www.youtube.com/watch?v=FfWpgLFMI7w

# initialize pygame - very important
pg.init()

# This is to access the methods that is inside the pygame make sure to add a bracket inside
# create the screen
#  screen = pygame.display.set_mode(( width, height )) -> () means a tuple width->x axis height-> y axis
# game window created but closes automatically after a few seconds
# The above is because our python program goes throught the three line and exits remember i have done till screen till now
screen = pg.display.set_mode((800, 600))

"""
while True:
    pass
This statement will hang your python window 
This is because we don't have an event of a quit function here
"""

"""
Event is anything happening inside game window is an event 
Like moving arrow , close button pressed
"""

# Title and Icon
# Title
pg.display.set_caption("Space Invaders")
# Icon
icon = pg.image.load('./images/spaceship.png')
pg.display.set_icon(icon)

# Setting the Player
playerimg = pg.display.load('./images/player.png')
# playerx and playery are coordinates , pygame follows (0,0) coordinate system
playerx = 370
playery = 480

# Game Loop This loop ensures that our window is always running untill quit is pressed
# Doesn't give the above errors
# Anythin we want to appear consistently should be inside out while loop
running = True
while running:
    # checks through the list of all events
    for event in pg.event.get():
        if event.type == pg.QUIT :
            running = False

    # Change Background
    # inside the tuple we give it three values of RGB 0 - 255
    # for finding color search color to rgb
    screen.fill((0,0,0))
    # Without update statement the color wont update
    pg.display.update()