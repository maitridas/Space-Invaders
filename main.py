import pygame as pg
import random
import math
from pygame import mixer
# mixer helps is using music


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


# Background sound
# -1 helps in playing in loop
# music is because we are playing continuously 
# for playing sounds for a short period of time we use sound
mixer.music.load('./sound/background.wav')
mixer.music.play(-1)


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
# Multiple enemy
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append( pg.image.load('./images/enemy.png') )
    # playerx and playery are coordinates , pygame follows (0,0) coordinate system
    enemyx.append(random.randint(0, 735) )
    enemyy.append(random.randint(50, 150) )
    # to measure the change
    enemyx_change.append(3 )
    enemyy_change.append(40 )



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

# score
# Display text on the screen
# For fonts download and keep in the directory
# free font website dafont.com
score = 0
font = pg.font.Font('freesansbold.ttf', 32)

textx = 10
texty = 10

# Game over text
game_over = pg.font.Font('freesansbold.ttf', 60)

def game_over_text():
    s = game_over.render("GAME OVER",True, (255,255,255))
    screen.blit(s,(200, 250))

def show_score(x,y):
    # rendering text
    # font.render("Score :" + str(score),<do you want to display on screen>, (R,G,B))
    s = font.render("Score :" + str(score),True, (255,255,255))
    screen.blit(s,(x, y))


# This function can be used for movements for player
def player(x,y):
    # blit means drawing and we are drawing our player on the surface of our game
    # screen.blit(<image> , <coordinates>)
    screen.blit(playerimg,(x, y))



# This function can be used for movements for enemy
def enemy(x,y,i):
    # blit means drawing and we are drawing our player on the surface of our game
    screen.blit(enemyimg[i],(x, y))



# This function can be used for movements for bullet 
def fire_bullet(x,y):
    # to access the global bullet state
    global bullet_state
    bullet_state = "fire"
    # blit means drawing and we are drawing our player on the surface of our game
    screen.blit(bulletimg,(x + 16 , y + 10))



def isCollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt( math.pow((bulletx- enemyx), 2) +  math.pow((bullety - enemyy), 2))
    if distance < 27:
        return True
    else:
        return False



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
                if bullet_state == "ready":
                    # not giving -1 here because we don't intend to run it in a loop
                    bullet_sound = mixer.Sound('./sound/laser.wav')
                    bullet_sound.play()
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
    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change

    # Enemy movement
    
    for i in range(num_of_enemies):

        # Game Over
        if enemyy[i]>440:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break

        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 3
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >=736:
            enemyx_change[i] = -3
            enemyy[i] += enemyy_change[i]

        # Collision
        collision = isCollision(enemyx[i] , enemyy[i] , bulletx, bullety)
        if collision:
            explosion_sound = mixer.Sound('./sound/explosion.wav')
            explosion_sound.play()
            bullety = 480
            bullet_state = "ready"
            score += 1
            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)

        enemy(enemyx[i],enemyy[i] , i)

    # Always call the player function after the screen or else player won't appear on the screen
    # will appear behind the screen which is not desirerable
    player(playerx,playery)
    show_score(textx, texty)
    # Without update statement the color wont update
    pg.display.update()