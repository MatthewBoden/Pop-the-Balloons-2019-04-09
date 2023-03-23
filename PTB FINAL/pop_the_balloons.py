#########################################
# Programmer: Matthew Bodenstein
# Date: 04/05/2019
# File Name: pop_the_balloons.py
# Description: pop the balloons, click a balloon before it hits the top.
#########################################
import random
import pygame


pygame.init()
import time
from math import sqrt                   # only sqrt function is needed from the math module
from random import randint              # only randint function is needed from the random module
gameover=False

balIMG = pygame.image.load("ball.png")
balIMG = pygame.transform.scale(balIMG,(70,70))

#ballDict = {1:balIMG,2:}

miss = 0
popped = 0
# Game window
HEIGHT = 600
WIDTH  = 800
game_window = pygame.display.set_mode((WIDTH,HEIGHT))
pic1= pygame.image.load("ptb.png")                    # Image properties
pic1= pic1.convert_alpha()                           #
pic1X = 0
pic1Y = 0
# Colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
yellow = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
outline=0                               # thickness of the shapes' outline
CLR = [WHITE, blue, red, green, purple, yellow]
elapseTime=0                             # Timer variables/properties
startTime=time.time()                    #
endTime=0                                #
#---------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
#---------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)    # Pythagorean theorem
#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redraw_game_window():
    game_window.fill(BLACK)
    game_window.blit(pic1, (pic1X, pic1Y))
    if popped + miss== 20:  # Checks for the end of the game
        endgame()           #
    else:
        for i in range(20):
            if visible[i] == True:
               # pygame.draw.circle(game_window, balloonCLR[i], (balloonX[i], balloonY[i]), balloonR[i], outline)
                game_window.blit(balIMG,(balloonX[i],balloonY[i]))
            endTime = time.time()             #
            elapseTime = endTime - startTime  # Calculating the elapse time
            elapseTime = int(elapseTime)      #
            font = pygame.font.SysFont("Ariel Black", 50)  # create a variable font
            time1 = font.render(str(elapseTime), 1, BLACK)      # printing time
            time2 = font.render("Time:", 1, BLACK)              #
            textscore = font.render("score:" + str(popped), 1, blue)  # put the font and the message together
            textmiss = font.render("missed:" + str(miss), 1, red)     #
            game_window.blit(textscore, (0, 0))  # draw it on the screen at the text_X and text_Y
            game_window.blit(time2, (300, 0))    #
            game_window.blit(time1, (390, 0))    #
            game_window.blit(textmiss, (625, 0)) #
    pygame.display.update()    # display must be updated, in order to show the drawings
def endgame():
    game_window.fill(BLACK)
    game_window.blit(pic1, (pic1X, pic1Y))
    font = pygame.font.SysFont("Ariel Black", 100)  # create a variable font
    textscore = font.render("Score:" + str(popped), 1, BLACK)  # p
    textmiss = font.render("Missed:" + str(miss), 1, BLACK)     # put the font and the message together
    game_window.blit(textscore, (250, 500))  #
    game_window.blit(textmiss, (250, 400))   # draw it on the screen at the text_X and text_Y
    time2 = font.render(str(elapseTime), 1, BLACK)  #
    FinalTime = font.render("Final Time:", 1, BLACK)  #
    game_window.blit(time2, (540,200))
    game_window.blit(FinalTime, (120,200))
    if miss > popped:
        statement = "LOSER"
        clr = red
    if popped > miss:
        statement = "WINNER"
        clr = green
    if popped == miss:
        statement = "TIE GAME"
        clr = yellow
    text = font.render(statement, 1, clr)  # put the font and the message together
    game_window.blit(text, (250, 100))  # draw it on the screen at the text_X and text_Y
    pygame.time.delay(100)
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
exit_flag = False
visible = [True]*20                     #
balloonCLR = [0]*20                     #
balloonR = [0]*20                       # create lists of 20 items each
balloonX = [0]*20                       # for balloons' properties
balloonY = [0]*20                       #
balloonSPEED = [0]*20                   #
for i in range(20):
    balloonX[i] = randint(0, WIDTH)     # initialize the coordinates and the size of the balloons
    balloonY[i] = randint(HEIGHT/2, HEIGHT)
    balloonR[i] = randint(25,45)
    balloonSPEED[i] = randint(4,7)
    balloonCLR[i] = random.choice(CLR)

while not exit_flag:                    #
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            exit_flag = True            # Flag that we are done so we exit this loop

# act upon mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(20):
                (cursorX,cursorY)=pygame.mouse.get_pos()
                if distance(cursorX, cursorY, balloonX[i], balloonY[i])< balloonR[i] and visible[i] :
                    visible[i] = False       # makes the balloon not visible
                 #   balloonY[i] = 99999
                    game_window.fill(BLACK)
                    game_window.blit(pic1, (pic1X, pic1Y))
                    popped += 1              # adds 1 to score for each balloon popped
                    print(popped)
    # move the balloons
    for i in range(20):
        if visible[i]:
            balloonY[i] = balloonY[i] - balloonSPEED[i]  # changes the direction of the balloon to move it
            if balloonY[i] < 0 :                          #   checks if the balloon passed 0 to count as a miss
                visible[i] = False
                miss += 1                                #   counts if the balloon missed
          #  balloonY[i] = 99999                      #   puts the hitbox of the balloon at 99999 so it can not be pressed by accident
    if popped + miss == 20:
        if gameover == False:
            endTime = time.time()               #
            elapseTime = endTime - startTime    #   Pauses the time for end screen
            elapseTime = int(elapseTime)        #
            gameover = True
# update the screen
    redraw_game_window()
    pygame.time.delay(100)
pygame.quit()                           # always quit pygame when done!
