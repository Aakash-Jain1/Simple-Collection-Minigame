'''
garbageCollectionGame.py
Aakash Jain
June 15th, 2021
Make a game where the user goes around collecting garbage to earn points
Objective: To get 4 points and not get hit by moving obstacle
'''

#import pygame and time---

import pygame #import pygame
pygame.init()  # initialize pygame

import time #import time for time.sleep()

#initialize variables---

#screen size
WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

#constants for colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
LIGHT_GREY = (192, 192, 192)

CYAN = (0, 255, 255)
LIGHT_BLUE = (155, 200, 255)
LIGHT_GREEN = (50, 255, 50)

YELLOW = (255, 255, 100)
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)
ORANGE_RED = (255, 69, 0) 
DARK_ORANGE = (255, 140, 0)

MAGENTA = (210, 0, 128)
DARK_PURPLE = (128, 0, 128)
LIGHT_PURPLE = (200, 200, 255)

PINK = (255, 153, 153)
LIGHT_PINK = (255, 229, 204)
DARK_PINK = (255, 51, 153)

BROWN= (150, 76, 0)
LIGHT_BROWN= (200, 120, 20)
MUD_BROWN = (125, 125, 0)

# set up fonts for DRAWING TEXT
font1 = pygame.font.SysFont("Courier New Bold", 36)
font2 = pygame.font.SysFont("Courier New Bold", 24)

#Centre of the screen
CENTREX= WIDTH// 2
CENTREY= HEIGHT//2

#score starts off at 0
score = 0

#x and y speeds of player
#how fast the player can move horizontally or vertically
#set as 0 to begin
xSpeed=0
ySpeed=0

#x and y coordinates of player
xCoordinate=330
yCoordinate=440

#load the garbage image from folder
garbageImg= pygame.image.load ("transparentBin.png")
trashImg = pygame.transform.scale(garbageImg,(50,78)) #resize to make it appropriate for screen

#when the garbage images are not displayed
garbageDisplay1 = 0
garbageDisplay2 = 0
garbageDisplay3 = 0
garbageDisplay4 = 0


#set enemy variables
enemyX = 275
enemyY = 250
enemyUp = True  #start with enemy moving upwards


#button variables
yesButton = True 
noButton = True
buttonPressed = True #a button is pressed

#set varibales to play the game
playGame= False #do not play game 
start = True

#Main program begins---

while not playGame: #while true
    if start == True:
        #starting screen
        start = False
        gameWindow.fill(CYAN) #fill window in cyan colour
        #welcome message
        welcome = font1.render("The Garbage Collection Game", 0, BLACK)
        
        #Instruction messages
        message = font1.render("Instructions:", 0, BLACK)
        instruction1= font1.render("Collect all the garbage by moving character to win", 0, BLACK)
        instruction2= font1.render("Press W to move up", 0, BLACK)
        instruction3= font1.render("Press A to move left", 0, BLACK)
        instruction4= font1.render("Press S to move down", 0, BLACK)
        instruction5= font1.render("Press D to move right", 0, BLACK)
        instruction6= font1.render("Hitting the red block results in loss", 0, BLACK)
        hint=font1.render("Hint: Avoid hitting barrier edges, they make you bounce!", 0, BLACK)#hint for playing
        
        #display all messages on the screen
        gameWindow.blit(welcome, (200, 20))
        gameWindow.blit(message, (50, 70))
        gameWindow.blit(instruction1, (50, 120))
        gameWindow.blit(instruction2, (50, 150))
        gameWindow.blit(instruction3, (50, 180))
        gameWindow.blit(instruction4, (50, 210))
        gameWindow.blit(instruction5, (50, 240))
        gameWindow.blit(instruction6, (50, 270))
        gameWindow.blit(hint, (50, 300))

        #the game is about to begin message
        startMessage= font1.render("The game will start in a few seconds...", 0, BLACK)
        #display startMessage
        gameWindow.blit(startMessage, (50, 400))
        pygame.display.update()#update screen
        time.sleep(3) #wait 15 seconds to let user read

        #Let the buttons show and work each loop
        noButton=True 
        yesButton=True
        buttonPressed=True
        
    #start game screen---
    
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            playGame = True #game is set to true
            pygame.display.update() #update screen
            
        #set up how the player moves around the screen--
            
        elif event.type == pygame.KEYDOWN: #when a key is pressed
        
            if event.key == pygame.K_a: #press a to move left 
                xSpeed = -3
            elif event.key == pygame.K_d:#press d to move right 
                xSpeed = 3
            elif event.key == pygame.K_w:#press w to move up 
                ySpeed=-3
            elif event.key == pygame.K_s:#press s to move down 
                ySpeed = 3

        elif event.type == pygame.KEYUP: #when a key is not pressed

            #if the key is not pressed do not move
            if event.key == pygame.K_a or event.key == pygame.K_d:
                xSpeed = 0 #set speed to 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                ySpeed=0 #set speed to 0

    gameWindow.fill(GREY)#game background is set to grey
   
    #limit the player within the screen contents--

    #the player can't go too far up or down
    if yCoordinate > 550:
        ySpeed=0
        yCoordinate -=1
    elif yCoordinate <0:
        ySpeed =0
        yCoordinate +=1
    else:
        yCoordinate += ySpeed
        
    #the player can't go too far right or left
    if xCoordinate > 750:
        xSpeed=0
        xCoordinate -=1
    elif xCoordinate <0:
        xSpeed =0
        xCoordinate +=1
    else:
        xCoordinate += xSpeed

        #draw the player
        player = pygame.draw.rect(gameWindow,BLUE, [xCoordinate, yCoordinate,50,50])

   
    #enemy moves across player's path
        
    if enemyY < 150 and enemyUp == True:
        enemyUp = False #to move the block down
        
    elif enemyY > 280 and enemyUp == False :        
        enemyUp = True # to move the block upward
    #end if
        
    #how fast the enemy moves up and down
    if enemyUp == True:
        enemyY -= 1 #move block up by 1 each loop
    else:
        enemyY += 1 #move block down by 1 each loop
    #end if
    
    #draw the enemy block    
    enemy= pygame.draw.rect(gameWindow, RED, (enemyX,enemyY, 325, 40), 0)
    
    #collisions with maze barriers---

    #draw barriers
    barrier1= pygame.draw.rect(gameWindow, BLACK, (200,0, 15, 300), 0)
    barrier2= pygame.draw.rect(gameWindow, BLACK, (600,300, 15, 300), 0)
    barrier3= pygame.draw.rect(gameWindow, BLACK, (0,400, 500, 15), 0)
    barrier4= pygame.draw.rect(gameWindow, BLACK, (600,200, 200, 15), 0)
    barrier5= pygame.draw.rect(gameWindow, BLACK, (400,100, 300, 15), 0)
    barrier6= pygame.draw.rect(gameWindow, BLACK, (100,500, 400, 15), 0)
    barrier7= pygame.draw.rect(gameWindow, BLACK, (550,0, 15, 100), 0)
    barrier8= pygame.draw.rect(gameWindow, BLACK, (250,400, 15, 100), 0)
    barrier9= pygame.draw.rect(gameWindow, BLACK, (200,175, 75, 15), 0)
    barrier10= pygame.draw.rect(gameWindow, BLACK, (400,100, 15, 50), 0)
    barrier11= pygame.draw.rect(gameWindow, BLACK, (95,165, 12, 175), 0)
    barrier12= pygame.draw.rect(gameWindow, BLACK, (131,0, 12, 170), 0)
    barrier13= pygame.draw.rect(gameWindow, BLACK, (600,200, 15, 40), 0)
    barrier14= pygame.draw.rect(gameWindow, BLACK, (55,55, 15, 100), 0)
    barrier15= pygame.draw.rect(gameWindow, BLACK, (55,155, 80, 15), 0)

    #if player collides with barriers, stop and bounce back
    
    #barrier1 collision
    if xCoordinate +50 >=200 and xCoordinate <=205 and yCoordinate <300:
        xCoordinate= 150
    elif xCoordinate >= 213 and xCoordinate <=215 and yCoordinate <300:
        xCoordinate= 216
    #barrier2 collision
    if xCoordinate+ 50>=600 and xCoordinate <= 605 and yCoordinate >=250 and yCoordinate <= 600:
        xCoordinate = 550
    elif xCoordinate>=600 and xCoordinate <= 615 and yCoordinate >=250 and yCoordinate <= 600:
        xCoordinate = 616
    #barrier3 collision
    if xCoordinate >=-50 and xCoordinate <=500 and yCoordinate >= 350 and yCoordinate <=410:
        yCoordinate = 350
    elif xCoordinate  >=-50 and xCoordinate <=500 and yCoordinate >=400 and yCoordinate <=415:
        yCoordinate = 415
    #barrier4 collision
    if xCoordinate >= 555 and xCoordinate <= 800 and yCoordinate >=150 and yCoordinate <= 210:
        yCoordinate =150
    elif xCoordinate >= 555 and xCoordinate <= 800 and yCoordinate >=200 and yCoordinate <=215:
        yCoordinate = 215
    #barrier5 collision
    if xCoordinate >= 355 and xCoordinate <= 700 and yCoordinate >= 50 and yCoordinate <= 110:
        yCoordinate =50
    elif xCoordinate >= 355 and xCoordinate <= 700 and yCoordinate >=100 and yCoordinate <=115:
        yCoordinate = 115  
    #barrier6 collision
    if xCoordinate >= 50 and xCoordinate <= 500 and yCoordinate >=450 and yCoordinate <=510:
        yCoordinate = 450
    elif xCoordinate >= 50 and xCoordinate <= 500 and yCoordinate >= 500 and yCoordinate <515:
        yCoordinate = 515
    #barrier7 collision
    if xCoordinate +50 >= 550 and xCoordinate <= 555 and yCoordinate <100:
        xCoordinate = 500
    elif xCoordinate >= 563 and xCoordinate <= 565 and yCoordinate <100:
        xCoordinate = 566
    #barrier8 collision
    if xCoordinate +50 >= 250 and xCoordinate <= 255 and yCoordinate >= 400 and yCoordinate <=500:
        xCoordinate =200
    elif xCoordinate >= 263 and xCoordinate <= 265 and yCoordinate >= 400 and yCoordinate <=500:
        xCoordinate = 266
    #barrier9 collision
    if xCoordinate >= 175 and xCoordinate <=275 and yCoordinate >= 125 and yCoordinate <= 185:
        yCoordinate = 125
    elif xCoordinate >= 175 and xCoordinate <=275 and yCoordinate >= 175 and yCoordinate <= 190:
        yCoordinate=190
    #barrier10 collision
    if xCoordinate+50 >= 400 and xCoordinate <= 405 and yCoordinate >= 55 and yCoordinate<= 150:
        xCoordinate = 350
    elif xCoordinate >= 400 and xCoordinate <= 415 and yCoordinate >= 55 and yCoordinate <= 150:
        xCoordinate =416
    #barrier11 collision
    if xCoordinate+50 >= 95 and xCoordinate <= 100 and yCoordinate >= 135 and yCoordinate<= 340:
        xCoordinate = 45
    elif xCoordinate >= 105 and xCoordinate <= 107 and yCoordinate >= 135 and yCoordinate <= 340:
        xCoordinate =108
    #barrier12 collision
    if xCoordinate +50 >= 131 and xCoordinate <=136 and yCoordinate <160:
        xCoordinate = 81
    elif xCoordinate >= 141 and xCoordinate <=143 and yCoordinate <160:
        xCoordinate =144
    #barrier13 collision
    if xCoordinate+50 >= 600 and xCoordinate <= 605 and yCoordinate >= 155 and yCoordinate<= 240:
         xCoordinate = 550
    elif xCoordinate >= 600 and xCoordinate <= 615 and yCoordinate >= 155 and yCoordinate <= 240:
        xCoordinate = 616
    #barrier14 collision
    if xCoordinate+50 >= 55 and xCoordinate <= 60 and yCoordinate >= 5 and yCoordinate<= 155:
         xCoordinate = 5
    elif xCoordinate >= 68 and xCoordinate <= 70 and yCoordinate >= 5 and yCoordinate <= 155:
        xCoordinate = 71
    #barrier15 collision
    if xCoordinate >= 15 and xCoordinate <= 140 and yCoordinate >= 105 and yCoordinate <= 155:
        yCoordinate= 105
    elif xCoordinate >= 15 and xCoordinate <= 140 and yCoordinate >= 155 and yCoordinate <=170:
        yCoordinate = 170 

    #if player collides with garbage, add a score of 1 and take garbage off screen---
        
    if garbageDisplay1 ==0:
        garbageRect1 = pygame.draw.rect(gameWindow, GREY,(70,90,50,60))#draw a rectangle under garbage
        if xCoordinate+50 >= 70 and xCoordinate <= 120 and yCoordinate >= 40 and yCoordinate <= 158:
            garbageDisplay1 = 1 #show garbage image
            score+=1 #add 1 to score
    elif garbageDisplay1 ==1: #when player collides
        del garbageRect1 #delete the rectangle
        garbageDisplay1=2 #don't show the garbage image
    else:
        print("") #empty string to act as a null statement, basically else do nothing to avoid error
        
        
    if garbageDisplay2 ==0:
        garbageRect2 = pygame.draw.rect(gameWindow, GREY,(700,120,50,60))#draw a rectangle under garbage
        if xCoordinate+50 >= 700 and xCoordinate <= 750 and yCoordinate >= 100 and yCoordinate <= 180:
            garbageDisplay2 = 1 #show garbage image
            score+=1#add 1 to score
    elif garbageDisplay2 ==1:#when player collides
        del garbageRect2#delete the rectangle
        garbageDisplay2=2#don't show the garbage image
    else:
        print("")#empty string to act as a null statement, basically else do nothing to avoid error
        
    if garbageDisplay3 ==0:
        garbageRect3 = pygame.draw.rect(gameWindow, GREY,(200,425,50,70))#draw a rectangle under garbage
        if xCoordinate+50 >= 200 and xCoordinate <= 250 and yCoordinate >= 400 and yCoordinate <= 495:
            garbageDisplay3 = 1#show garbage image
            score+=1#add 1 to score
    elif garbageDisplay3 ==1:#when player collides
        del garbageRect3#delete the rectangle
        garbageDisplay3=2#don't show the garbage image
    else:
        print("")#empty string to act as a null statement, basically else do nothingto avoid pygame.display.update()
        
    if garbageDisplay4 ==0:
        garbageRect4 = pygame.draw.rect(gameWindow, GREY,(700,500,50,60))#draw a rectangle under garbage
        if xCoordinate+50 >= 700 and xCoordinate <= 750 and yCoordinate >= 450 and yCoordinate <= 560:
            garbageDisplay4 = 1#show garbage image
            score+=1#add 1 to score
    elif garbageDisplay4 ==1:#when player collides
        del garbageRect4#delete the rectangle
        garbageDisplay4=2#don't show the garbage image
    else:
        print("")#empty string to act as a null statement, basically else do nothing to avoid error
        
        
    #show the score at the top right of game screen---

    #draw text for the score
    scoreText= font1.render("Score: " + str(score),0, WHITE)#needs to be str to add the together
    gameWindow.blit(scoreText, [650,25])#show the text on screen

    #when the garbage display is set to 0, show the garbage images on screen---

    if garbageDisplay1 ==0:
        gameWindow.blit(trashImg, (70,80))#draw on screen
    else:
        print("")#empty string to act as a null statement, basically else do nothing to avoid error
    if garbageDisplay2 ==0:
        gameWindow.blit(trashImg, (700,120))#draw on screen
    else:
        print("")#empty string to act as a null statement, basically else do nothing to avoid error
    if garbageDisplay3 ==0:
        gameWindow.blit(trashImg, (200,425))#draw on screen
    else:
        print("")#empty string to act as a null statement, basically else do nothing to avoid error
    if garbageDisplay4 ==0:
        gameWindow.blit(trashImg, (700,500))#draw on screen
    else:
        print("")#empty string to act as a null statement, basically else do nothing to avoid error


    #if the user gets all garbage and wins---
        
    if score == 4:
        gameWindow.fill(WHITE)#make screen white
        
        #write messages and display them
        winnerText=font1.render("GAME OVER, YOU WIN!",0, BLUE)
        playAgainText=font1.render("PLAY AGAIN?",0,BLACK)
        gameWindow.blit (playAgainText,[315,300])
        gameWindow.blit (winnerText, [264,250])
        
       #when a button is pressed---
        
        while buttonPressed ==True:
            
            #draw and display yesButton
            if yesButton ==True: 
                pygame.draw.rect(gameWindow, GREEN,  (250,350, +100, +50), 0)
                responseYes = font1.render("YES", 0, BLACK)
                gameWindow.blit(responseYes,[275,360])
                pygame.display.update()
                
            #draw and display noButton
            if noButton ==True:
                pygame.draw.rect(gameWindow, RED,  (450,350, +100, +50), 0)
                responseNo = font1.render("NO", 0, BLACK)
                gameWindow.blit(responseNo,[480,360])
                pygame.display.update()
            
            #clear Python Memory to continue polling for events
            pygame.event.clear()
            #get mouse click data
            buttonClicked = pygame.mouse.get_pressed()
            #get mouse position
            (mouseX, mouseY) = pygame.mouse.get_pos()

            #collision with mouse and LEFT mouse button CLICK-->(Left click, Middle click, Right click)---
            
            #when mouse and left click collide with noButton
            if mouseX > 450 and mouseX < 450+100 and mouseY > 350 and mouseY < 350+50 and noButton == True and buttonClicked == (True, False, False):
                gameWindow.fill(YELLOW)#make screen yellow
                pygame.display.update()
                thankYou=font1.render("Thank you for playing!",0, BLUE)
                gameWindow.blit(thankYou,[250,250])#display thank you message
                goodbye=font1.render("Goodbye!",0, BLUE)
                gameWindow.blit(goodbye,[250,350])#display goodbye message
                pygame.display.update()
                time.sleep(2)#wait 2 seconds
                pygame.quit()#close the program
                noButton=False #no button does not show or work
                yesButton=False#yes button does not show or work
                buttonPressed=False #buttons are not pressed
                playGame = True #end the game

            #when mouse and left click collide with yes button
            elif mouseX > 250 and mouseX < 250+100 and mouseY > 350 and mouseY < 350+50 and yesButton == True and buttonClicked == (True, False, False):
                playGame=False #continue to play game
                pygame.display.update()
                noButton=False #no button does not show or work
                yesButton=False#yes button does not show or work
                buttonPressed=False#buttons are not pressed
                score=0 #score is reset to 0
                #x and y coordinates are reset
                xCoordinate=330
                yCoordinate=440
                #player speed is reset
                xSpeed=0
                ySpeed=0
                #images are reset
                garbageDisplay1 = 0
                garbageDisplay2 = 0
                garbageDisplay3 = 0
                garbageDisplay4 = 0
                start =True #start game, loop game again


    #if collision with enemy block---
                
    if xCoordinate +50 >= enemyX and xCoordinate-50 <= enemyX+275 and yCoordinate-50<=enemyY-20 and yCoordinate+50>enemyY:
        gameWindow.fill(WHITE)#make screen white

        #write messages and display them
        loserText=font1.render("GAME OVER, YOU LOSE!",0, BLUE)
        playAgainText=font1.render("PLAY AGAIN?",0,BLACK)
        gameWindow.blit (playAgainText,[315,300])
        gameWindow.blit (loserText, [264,250])
        
        #when a button is pressed---
        
        while buttonPressed ==True:

            #draw and display yesButton
            if yesButton ==True:
                pygame.draw.rect(gameWindow, GREEN,  (250,350, +100, +50), 0)
                responseYes = font1.render("YES", 0, BLACK)
                gameWindow.blit(responseYes,[275,360])
                pygame.display.update()
                
            #draw and display noButton
            if noButton ==True:
                pygame.draw.rect(gameWindow, RED,  (450,350, +100, +50), 0)
                responseNo = font1.render("NO", 0, BLACK)
                gameWindow.blit(responseNo,[480,360])
                pygame.display.update()
            
            #clear Python Memory to continue polling for events
            pygame.event.clear()
            #get mouse click data
            buttonClicked = pygame.mouse.get_pressed()
            #get mouse position
            (mouseX, mouseY) = pygame.mouse.get_pos()
            
            #collision with mouse and LEFT mouse button CLICK-->(Left click, Middle click, Right click)---
            
            #when mouse and left click collide with noButton
            if mouseX > 450 and mouseX < 450+100 and mouseY > 350 and mouseY < 350+50 and noButton == True and buttonClicked == (True, False, False):
                gameWindow.fill(YELLOW)#make screen yellow
                pygame.display.update()
                thankYou=font1.render("Thank you for playing!",0, BLUE)
                gameWindow.blit(thankYou,[250,250])#display thank you message
                goodbye=font1.render("Goodbye!",0, BLUE)
                gameWindow.blit(goodbye,[250,350])#display goodbye message
                pygame.display.update()
                time.sleep(2)#wait 2 seconds
                pygame.quit()#close the program
                noButton=False#no button does not show or work
                yesButton=False#yes button does not show or work
                buttonPressed=False#buttons are not pressed
                playGame = True #end the game
                
            #when mouse and left click collide with ywaButton   
            elif mouseX > 250 and mouseX < 250+100 and mouseY > 350 and mouseY < 350+50 and yesButton == True and buttonClicked == (True, False, False):
                playGame=False#continue to play game
                pygame.display.update()   
                noButton=False#no button does not show or work
                yesButton=False#yes button does not show or work
                buttonPressed=False#buttons are not pressed
                score=0 #score is reset to 0
                #x and y coordinates are reset
                xCoordinate=330
                yCoordinate=440
                #player speed is reset
                xSpeed=0
                ySpeed=0
                #images are reset
                garbageDisplay1 = 0
                garbageDisplay2 = 0
                garbageDisplay3 = 0
                garbageDisplay4 = 0
                start =True#start game, loop game again
                
            
        pygame.display.update()#show the buttons and screens
        pygame.time.delay(500)#delay 500 milliseconds before showing
        
    pygame.display.update()#update screen to show game screen again

 
    clock = pygame.time.Clock()
    clock.tick(60)



pygame.quit()#to not get a NO-responding window
