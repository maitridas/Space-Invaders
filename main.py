import pygame as pg
import random



# reference - https://www.youtube.com/watch?v=FfWpgLFMI7w
# icons from flaticon.com
# background - freepik.com



# initialize pygame - very important
pg.init()



# Follows coordinate system the left topmost corner is (0, 0)
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



# Adding Background
# Background image size should be same as window size
background = pg.image.load('./images/background.png')



# Title and Icon
# Title
pg.display.set_caption("Space Invaders")
# Icon
icon = pg.image.load('./images/spaceship.png')
pg.display.set_icon(icon)



# Setting the Player
playerimg = pg.image.load('./images/player.png')
# playerx and playery are coordinates , pygame follows (0,0) coordinate system
playerx = 370
playery = 480
# to measure the change
playerx_change = 0



# Setting the enemy
enemyimg = pg.image.load('./images/enemy.png')
# playerx and playery are coordinates , pygame follows (0,0) coordinate system
enemyx = random.randint(0, 800)
enemyy = random.randint(50, 150)
# to measure the change
enemyx_change = 3
enemyy_change = 40



# Setting the bullet
bulletimg = pg.image.load('./images/bullet.png')
# playerx and playery are coordinates , pygame follows (0,0) coordinate system
bulletx = 0
bullety = 480
# to measure the change
bulletx_change = 0
bullety_change = 10
# ready -> you can't see the bullet in the screen
# fire -> bullet is moving
bullet_state = "ready"



"""def player():
    # blit means drawing and we are drawing our player on the surface of our game
    screen.blit(playerimg,(playerx, playery))
"""



# This function can be used for movements for player
def player(x,y):
    # blit means drawing and we are drawing our player on the surface of our game
    # screen.blit(<image> , <coordinates>)
    screen.blit(playerimg,(x, y))



# This function can be used for movements for enemy
def enemy(x,y):
    # blit means drawing and we are drawing our player on the surface of our game
    screen.blit(enemyimg,(x, y))



# This function can be used for movements for bullet 
def fire_bullet(x,y):
    # to access the global bullet state
    global bullet_state
    bullet_state = "fire"
    # blit means drawing and we are drawing our player on the surface of our game
    screen.blit(bulletimg,(x + 16 , y + 10))



# Game Loop This loop ensures that our window is always running untill quit is pressed
# Doesn't give the above errors
# Anythin we want to appear consistently should be inside out while loop
running = True
while running:

    # Change Background
    # inside the tuple we give it three values of RGB 0 - 255
    # for finding color search color to rgb
    screen.fill((0,0,0))
    # background Image
    screen.blit(background, (0,0))

    # print(playerx) -> this statement prints the value in console
    # checks through the list of all events
    for event in pg.event.get():
        # checks if close button pressed
        if event.type == pg.QUIT :
            running = False

        # if keystroke is placed check whether its right or left
        # keydown is pressing the key and keyup is releasing the key
        if event.type == pg.KEYDOWN :
            # print("A key stroke is pressed")
            if event.key == pg.K_LEFT:
                # print("Left arrow pressed")
                playerx_change -= 5
            if event.key == pg.K_RIGHT:
                # print("Right arrow pressed")
                playerx_change += 5
            if event.key == pg.K_SPACE:
                if bullet_state is "ready":
                    fire_bullet(playerx,bullety)
                    bulletx = playerx
        
        # check if key released
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                playerx_change = 0

    # changes the x coordinate
    playerx += playerx_change

    # Adding Boundaries to our game
    if playerx <= 0:
        playerx = 0
    elif playerx >=736:
        # 800 - 64 = 736 64 is pixle of our player (64*64)
        playerx = 736

    # bullet movement
    if bullety<= 0:
        bullety = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change

    # Enemy movement
    enemyx += enemyx_change

    if enemyx <= 0:
        enemyx_change = 3
        enemyy += enemyy_change
    elif enemyx >=736:
        enemyx_change = -3
        enemyy += enemyy_change

    # Always call the player function after the screen or else player won't appear on the screen
    # will appear behind the screen which is not desirerable
    player(playerx,playery)
    enemy(enemyx,enemyy)
    # Without update statement the color wont update
    pg.display.update()