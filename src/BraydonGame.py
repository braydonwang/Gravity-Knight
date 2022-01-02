#######################################
# File Name: BraydonGame.py
# Description: Solution for final project
# Author: Braydon Wang
# Date: 28/04/2018
#########################################
# Imports
from math import sqrt
from random import randint

import pygame
pygame.init()

# Colours and outline
RED = (255,0,0)
ORANGE = (255,165,0)
DARK_ORANGE = (255,140,0)
LIGHT_YELLOW = (255,255,224)
YELLOW = (255,255,0)
GOLD = (255,215,0)
LIGHTGREEN = (152,251,152)
GREEN = (0,255,0)
SKYBLUE = (135,206,250)
PALE_TURQUOISE = (190,253,253)
LIGHTBLUE = (30,144,255)
TURQUOISE = (72,209,204)
BLUE = (65,105,225)
LAVENDER = (230,230,250)
BLACK = (0,0,0)
LIGHT_GREY = (230,230,230)
GREY = (192,192,192)
DARK_GREY = (90,90,90)
BROWN = (255,228,196)
DARK_BROWN = (222,184,135)
CHOCOLATE = (205,133,63)
SIENNA = (175,103,33)
SADDLE = (139,69,19)
WHITE = (255,255,255)
PINK = (255,192,203)
outline = 0

# Background music
pygame.mixer.music.load("cool_music.mp3")
pygame.mixer.music.set_volume(0.4) 
pygame.mixer.music.play(loops = -1)

def main(menu,howToPlay,inPlay,shop,coins,deaths,step,RUN_SPEED,totalKeys,gun,levelOne,levelTwo,levelThree,levelFour,levelFive,circleCLR,keyCLR,keyCLR2,backgroundCLR):
# Initializing width and height of the game window
    WIDTH = 800
    HEIGHT = 600
    gameWindow = pygame.display.set_mode((WIDTH,HEIGHT))

    # Fonts
    font1 = pygame.font.SysFont("Impact", 40)
    font2 = pygame.font.SysFont("Calibri Bold", 35)
    font3 = pygame.font.SysFont("Calibri Bold", 50)
    font4 = pygame.font.SysFont("Impact", 120)
    font5 = pygame.font.SysFont("Impact", 80)
    font6 = pygame.font.SysFont("Impact", 20)
    font7 = pygame.font.SysFont("Impact", 50)
    font8 = pygame.font.SysFont("Impact",75)
    font9 = pygame.font.SysFont("Calibri Bold", 45)
    font10 = pygame.font.SysFont("Calibri Bold", 23)

# Function to find distance between two points
    def distance(x1, y1, x2, y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)

# Function to find the equation of a circle
    def equationCircle(x,y,centerX,centerY):
        return (x-centerX)**2 + (y-centerY)**2 

# Draw main menu
    def mainMenu(buttonX1,buttonY1,buttonX2,buttonY2,buttonX3,buttonY3,button1Width,button1Height,button2Width,button2Height,button3Width,button3Height):
        gameWindow.fill(SKYBLUE)
# The text in the main menu screen
        graphicsTitle = font8.render("GRAVITY KNIGHT", 1, LIGHT_GREY)
        graphicsPlay = font9.render("PLAY", 1, WHITE)
        graphicsLevelSelect = font9.render("LEVEL SELECT", 1, WHITE)
        graphicsShop = font9.render("SHOP", 1, WHITE)
        graphicsQuit = font9.render("QUIT",1,WHITE)
# The buttons in the main menu screen
        pygame.draw.rect(gameWindow,buttonClr1,(buttonX1,buttonY1,button1Width,button1Height),0)
        pygame.draw.rect(gameWindow,buttonClr2,(buttonX2,buttonY2,button2Width,button2Height),0)
        pygame.draw.rect(gameWindow,buttonClr3,(buttonX3,buttonY3,button3Width,button3Height),0)
        pygame.draw.rect(gameWindow,buttonClr4,(60,370,450,50),outline)
            
        gameWindow.blit(tree2,(270,80))
        gameWindow.blit(tree4,(50,480))
        gameWindow.blit(tree3,(150,450))
        gameWindow.blit(tree,(210,250))
        gameWindow.blit(tree1,(550,250))
        gameWindow.blit(castle,(360,250))
        gameWindow.blit(dragon,(410,-130))
        gameWindow.blit(graphicsTitle,(80,75))
        gameWindow.blit(graphicsPlay,(80,200))
        gameWindow.blit(graphicsLevelSelect,(80,260))
        gameWindow.blit(graphicsShop,(80,320))
        gameWindow.blit(graphicsQuit,(80,380))
        pygame.display.update()

# Draw how to play screen
    def rulesToPlay():
        gameWindow.fill(SKYBLUE)
# The text explaining how to play the game
        graphicsHowToPlay = font8.render("HOW TO PLAY",1,BLACK)
        graphicsRuleOne = font9.render("1. Move the character using the arrow keys",1,BLACK)
        graphicsRuleOne2 = font9.render("Press the spacebar to switch gravity",1,BLACK)
        graphicsRuleTwo = font9.render("2. Avoid hitting the red circles/obstacles",1,BLACK)
        graphicsRuleThree = font9.render("3. Collect all of the keys in order to complete",1,BLACK)
        graphicsRuleThree2 = font9.render("the level",1,BLACK)
        graphicsRuleFour = font9.render("4. Once all of the keys are collected, move",1,BLACK)
        graphicsRuleFour2 = font9.render("safely to the other green side",1,BLACK)
        graphicsRuleFive = font9.render("5. Collect as many coins as you can to buy",1,BLACK)
        graphicsRuleFive2 = font9.render("cool stuff in the shop",1,BLACK)
        graphicsPress = font9.render("PRESS 'P' TO CONTINUE",1,WHITE)
# The shapes to outline the obstacles, keys and coins
        pygame.draw.rect(gameWindow,BLACK,(30,40,150,30),outline)
        pygame.draw.rect(gameWindow,BLACK,(620,40,150,30),outline)
        pygame.draw.circle(gameWindow,RED,(45,215),20,outline)
        pygame.draw.circle(gameWindow,GREY,(45,290),20,outline)
        pygame.draw.circle(gameWindow,DARK_GREY,(45,290),20,3)
        pygame.draw.rect(gameWindow,LIGHTGREEN,(30,360,36,60),outline)
        pygame.draw.circle(gameWindow,YELLOW,(45,490),20,outline)
        pygame.draw.circle(gameWindow,BLACK,(45,490),20,3)
        pygame.draw.rect(gameWindow,BLACK,(200,540,400,45),outline)
        
        gameWindow.blit(knight,(20,110))
        gameWindow.blit(graphicsHowToPlay,(210,10))
        gameWindow.blit(graphicsRuleOne,(90,110))
        gameWindow.blit(graphicsRuleOne2,(90,150))
        gameWindow.blit(graphicsRuleTwo,(90,200))
        gameWindow.blit(graphicsRuleThree,(90,250))
        gameWindow.blit(graphicsRuleThree2,(90,300))
        gameWindow.blit(graphicsRuleFour,(90,350))
        gameWindow.blit(graphicsRuleFour2,(90,400))
        gameWindow.blit(graphicsRuleFive,(90,450))
        gameWindow.blit(graphicsRuleFive2,(90,500))
        gameWindow.blit(graphicsPress,(220,550))
        pygame.display.update()

# Draw level select screen
    def levelSelect():
        gameWindow.fill(LIGHTBLUE)
# The shapes for the button boxes and designs
        pygame.draw.rect(gameWindow,SKYBLUE,(60,130,680,400),outline)
        pygame.draw.rect(gameWindow,YELLOW,(60,130,680,400),5)
        pygame.draw.rect(gameWindow,WHITE,(90,40,150,25),outline)
        pygame.draw.rect(gameWindow,WHITE,(550,40,150,25),outline)
        pygame.draw.rect(gameWindow,LIGHTGREEN,(170,200,100,100),outline)
        pygame.draw.rect(gameWindow,BLACK,(170,200,100,100),3)
        pygame.draw.rect(gameWindow,LIGHTGREEN,(350,200,100,100),outline)
        pygame.draw.rect(gameWindow,BLACK,(350,200,100,100),3)
        pygame.draw.rect(gameWindow,LIGHTGREEN,(530,200,100,100),outline)
        pygame.draw.rect(gameWindow,BLACK,(530,200,100,100),3)
        pygame.draw.rect(gameWindow,LIGHTGREEN,(260,360,100,100),outline)
        pygame.draw.rect(gameWindow,BLACK,(260,360,100,100),3)
        pygame.draw.rect(gameWindow,LIGHTGREEN,(440,360,100,100),outline)
        pygame.draw.rect(gameWindow,BLACK,(440,360,100,100),3)
# The text for the numbers of the level
        graphicsLevelOne = font5.render("1",1,BLACK)
        graphicsLevelTwo = font5.render("2",1,BLACK)
        graphicsLevelThree = font5.render("3",1,BLACK)
        graphicsLevelFour = font5.render("4",1,BLACK)
        graphicsLevelFive = font5.render("5",1,BLACK)
        graphicsLevelSelect = font7.render("LEVEL SELECT",1,WHITE)
        graphicsLevels = font10.render("SELECT A LEVEL THAT YOU WOULD LIKE TO START AT",1,WHITE)
        
        gameWindow.blit(graphicsLevelOne,(200,200))
        gameWindow.blit(graphicsLevelTwo,(380,200))
        gameWindow.blit(graphicsLevelThree,(560,200))
        gameWindow.blit(graphicsLevelFour,(290,360))
        gameWindow.blit(graphicsLevelFive,(470,360))
        gameWindow.blit(graphicsLevels,(200,90))
        gameWindow.blit(graphicsLevelSelect,(270,20))
        pygame.display.update()

    def itemShop(shopCLR1,shopCLR2,shopCLR3,shopCLR4,shopCLR5,shopCLR6,shopCLR7,shopCLR8,shopCLR9):
        gameWindow.fill(TURQUOISE)
# The shapes for the buttons and the items in the shop
        pygame.draw.circle(gameWindow,YELLOW,(50,50),16,outline)
        pygame.draw.circle(gameWindow,BLACK,(50,50),16,3)
        pygame.draw.line(gameWindow,PALE_TURQUOISE,(0,125),(620,125),3)
        pygame.draw.rect(gameWindow,CHOCOLATE,(25,150,595,430),outline)
        pygame.draw.polygon(gameWindow,GOLD,((25,150),(55,150),(25,180)),outline)
        pygame.draw.polygon(gameWindow,GOLD,((620,150),(590,150),(620,180)),outline)
        pygame.draw.polygon(gameWindow,GOLD,((25,580),(25,550),(55,580)),outline)
        pygame.draw.polygon(gameWindow,GOLD,((620,580),(590,580),(620,550)),outline)
        pygame.draw.rect(gameWindow,SIENNA,(60,190,525,360),outline)
        pygame.draw.rect(gameWindow,PALE_TURQUOISE,(645,0,25,600),outline)
        pygame.draw.rect(gameWindow,shopCLR1,(200,215,75,75),outline)
        pygame.draw.circle(gameWindow,BLUE,(237,252),25,outline)
        pygame.draw.rect(gameWindow,shopCLR2,(330,215,75,75),outline)
        pygame.draw.circle(gameWindow,GREEN,(367,252),25,outline)
        pygame.draw.rect(gameWindow,shopCLR3,(460,215,75,75),outline)
        pygame.draw.circle(gameWindow,BLACK,(497,252),25,outline)
        pygame.draw.rect(gameWindow,shopCLR4,(200,330,75,75),outline)
        pygame.draw.circle(gameWindow,ORANGE,(237,367),25,outline)
        pygame.draw.circle(gameWindow,DARK_ORANGE,(237,367),25,4)
        pygame.draw.rect(gameWindow,shopCLR5,(330,330,75,75),outline)
        pygame.draw.circle(gameWindow,PALE_TURQUOISE,(367,367),25,outline)
        pygame.draw.circle(gameWindow,TURQUOISE,(367,367),25,4)
        pygame.draw.rect(gameWindow,shopCLR6,(460,330,75,75),outline)
        pygame.draw.circle(gameWindow,WHITE,(497,367),25,outline)
        pygame.draw.circle(gameWindow,BLACK,(497,367),25,4)
        pygame.draw.rect(gameWindow,shopCLR7,(200,445,75,75),outline)
        pygame.draw.rect(gameWindow,PINK,(215,460,45,45),outline)
        pygame.draw.rect(gameWindow,shopCLR8,(330,445,75,75),outline)
        pygame.draw.rect(gameWindow,LIGHT_YELLOW,(345,460,45,45),outline)
        pygame.draw.rect(gameWindow,shopCLR9,(460,445,75,75),outline)
        pygame.draw.rect(gameWindow,LAVENDER,(475,460,45,45),outline)
# The shapes to draw the coins beside each price
        pygame.draw.circle(gameWindow,YELLOW,(222,302),8,outline)
        pygame.draw.circle(gameWindow,BLACK,(222,302),8,1)
        pygame.draw.circle(gameWindow,YELLOW,(352,302),8,outline)
        pygame.draw.circle(gameWindow,BLACK,(352,302),8,1)
        pygame.draw.circle(gameWindow,YELLOW,(482,302),8,outline)
        pygame.draw.circle(gameWindow,BLACK,(482,302),8,1)
        pygame.draw.circle(gameWindow,YELLOW,(222,417),8,outline)
        pygame.draw.circle(gameWindow,BLACK,(222,417),8,1)
        pygame.draw.circle(gameWindow,YELLOW,(352,417),8,outline)
        pygame.draw.circle(gameWindow,BLACK,(352,417),8,1)
        pygame.draw.circle(gameWindow,YELLOW,(482,417),8,outline)
        pygame.draw.circle(gameWindow,BLACK,(482,417),8,1)
        pygame.draw.circle(gameWindow,YELLOW,(222,532),8,outline)
        pygame.draw.circle(gameWindow,BLACK,(222,532),8,1)
        pygame.draw.circle(gameWindow,YELLOW,(352,532),8,outline)
        pygame.draw.circle(gameWindow,BLACK,(352,532),8,1)
        pygame.draw.circle(gameWindow,YELLOW,(482,532),8,outline)
        pygame.draw.circle(gameWindow,BLACK,(482,532),8,1)
# The 'back to game' button
        pygame.draw.rect(gameWindow,GREEN,(690,220,90,140),outline)
        pygame.draw.rect(gameWindow,BLACK,(690,220,90,140),3)
# The text for the prices of each item
        graphicsPrice1 = font10.render("5",1,WHITE)
        graphicsPrice2 = font10.render("5",1,WHITE)
        graphicsPrice3 = font10.render("5",1,WHITE)
        graphicsPrice4 = font10.render("10",1,WHITE)
        graphicsPrice5 = font10.render("10",1,WHITE)
        graphicsPrice6 = font10.render("10",1,WHITE)
        graphicsPrice7 = font10.render("15",1,WHITE)
        graphicsPrice8 = font10.render("15",1,WHITE)
        graphicsPrice9 = font10.render("15",1,WHITE)
# The text for the description and subtitles of the items shop
        graphicsBack = font2.render("BACK",1,BLACK)
        graphicsTo = font2.render("TO",1,BLACK)
        graphicsGame = font2.render("GAME",1,BLACK)
        graphicsObstacles = font10.render("OBSTACLES",1,BLACK)
        graphicsKeys = font10.render("KEYS",1,BLACK)
        graphicsStatistics = font10.render("BACKGROUND",1,BLACK)
        graphicsItemShop = font7.render("ITEM SHOP",1,PALE_TURQUOISE)
        graphicsDescription = font10.render("PURCHASE RARE ITEMS TO ENHANCE YOUR PLAYING EXPERIENCE",1,PALE_TURQUOISE)
        graphicsCoins = font10.render("COINS",1,BLACK)
        graphicsNumCoins = font1.render(str(coins),1,BLACK)

        gameWindow.blit(graphicsObstacles,(80,240))
        gameWindow.blit(graphicsKeys,(80,360))
        gameWindow.blit(graphicsStatistics,(80,480))
        gameWindow.blit(graphicsDescription,(85,90))
        gameWindow.blit(graphicsItemShop,(85,20))
        gameWindow.blit(graphicsPrice1,(235,295))
        gameWindow.blit(graphicsPrice2,(365,295))
        gameWindow.blit(graphicsPrice3,(495,295))
        gameWindow.blit(graphicsPrice4,(235,410))
        gameWindow.blit(graphicsPrice5,(365,410))
        gameWindow.blit(graphicsPrice6,(495,410))
        gameWindow.blit(graphicsPrice7,(235,525))
        gameWindow.blit(graphicsPrice8,(365,525))
        gameWindow.blit(graphicsPrice9,(495,525))
        gameWindow.blit(graphicsCoins,(710,60))
        gameWindow.blit(graphicsNumCoins,(720,10))
        gameWindow.blit(graphicsBack,(700,245))
        gameWindow.blit(graphicsTo,(715,275))
        gameWindow.blit(graphicsGame,(700,305))
        pygame.display.update()

# Draw the borders that surround the level
    def drawBorders():
        pygame.draw.rect(gameWindow,LIGHTBLUE,(20,100,760,480),outline)
        pygame.draw.rect(gameWindow,backgroundCLR,(40,160,720,400),outline)
        pygame.draw.rect(gameWindow,BLACK,(40,160,720,400),4)

# Draw the character as a sprite image
    def drawCharacter():
        gameWindow.blit(knightPic[knightPicNum],(knightX,knightY))

# Draw the green area where the character starts and ends at
    def drawStartEndPoints():
        pygame.draw.rect(gameWindow,LIGHTGREEN,(43,163,100,394),outline)
        pygame.draw.rect(gameWindow,LIGHTGREEN,(657,163,100,394),outline)

# Draw the obstacles/red circles for each level
    def drawObstacles():
        if levelOne: 
            for i in range(len(circleX1)-1,-1,-1):
                pygame.draw.circle(gameWindow,circleCLR,(circleX1[i],circleY1[i]),circleR,outline)
        elif levelTwo: 
            for i in range(len(circleX2)-1,-1,-1):
                pygame.draw.circle(gameWindow,circleCLR,(circleX2[i],circleY2[i]),circleR,outline)
        elif levelThree:
            for i in range(len(circleX3)-1,-1,-1):
                pygame.draw.circle(gameWindow,circleCLR,(circleX3[i],circleY3[i]),circleR,outline)
            pygame.draw.rect(gameWindow,LIGHTBLUE,(250,300,310,120),outline)
            pygame.draw.rect(gameWindow,BLUE,(250,300,310,120),5)
        elif levelFour:
            for i in range(len(circleX4)-1,-1,-1):
                pygame.draw.circle(gameWindow,circleCLR,(circleX4[i],circleY4[i]),circleR,outline)
        elif levelFive:
            for i in range(len(circleX5)):
                pygame.draw.circle(gameWindow,circleCLR,(circleX5[i],circleY5[i]),circleR,outline)

# Draw the keys/grey circles for each level
    def drawKeys():
        if levelOne: 
            for i in range(len(keyX1)-1,-1,-1):
                pygame.draw.circle(gameWindow,keyCLR,(keyX1[i],keyY1[i]),keyR,outline)
                pygame.draw.circle(gameWindow,keyCLR2,(keyX1[i],keyY1[i]),keyR,3)
        elif levelTwo:
            for i in range(len(keyX2)-1,-1,-1):
                pygame.draw.circle(gameWindow,keyCLR,(keyX2[i],keyY2[i]),keyR,outline)
                pygame.draw.circle(gameWindow,keyCLR2,(keyX2[i],keyY2[i]),keyR,3)
        elif levelThree:
            for i in range(len(keyX3)-1,-1,-1):
                pygame.draw.circle(gameWindow,keyCLR,(keyX3[i],keyY3[i]),keyR,outline)
                pygame.draw.circle(gameWindow,keyCLR2,(keyX3[i],keyY3[i]),keyR,3)
        elif levelFour:
            for i in range(len(keyX4)-1,-1,-1):
                pygame.draw.circle(gameWindow,keyCLR,(keyX4[i],keyY4[i]),keyR,outline)
                pygame.draw.circle(gameWindow,keyCLR2,(keyX4[i],keyY4[i]),keyR,3)
        elif levelFive:
            for i in range(len(keyX5)-1,-1,-1):
                pygame.draw.circle(gameWindow,keyCLR,(keyX5[i],keyY5[i]),keyR,outline)
                pygame.draw.circle(gameWindow,DARK_GREY,(keyX5[i],keyY5[i]),keyR,3)

# Draw the bullets when the gun upgrade is equipped
    def drawBullets():
        for i in range(len(bulletX)):
            pygame.draw.ellipse(gameWindow,BLACK,(bulletX[i],bulletY[i],20,6),outline)

# Check for collision between the character and the obstacles
    def countingDeaths(knightX,knightY,circleX,circleY):
        for i in range(len(circleX)):
            if distance(circleX[i],circleY[i],knightX + 25,knightY + 35) < circleR + knightR:
                pygame.time.delay(200)
                return True

# Draw the coins/yellow circles for each level
    def drawCoins():
        if levelThree:
            pygame.draw.circle(gameWindow,YELLOW,(coinX2,coinY2),coinR,outline)
            pygame.draw.circle(gameWindow,BLACK,(coinX2,coinY2),coinR,3)
        else:
            pygame.draw.circle(gameWindow,YELLOW,(coinX,coinY),coinR,outline)
            pygame.draw.circle(gameWindow,BLACK,(coinX,coinY),coinR,3)
            
# Draw the score board 
    def drawScoreBoard():
        pygame.draw.rect(gameWindow,SKYBLUE,(35,110,730,40),outline)

# Redraw the game window including all of the drawing functions
    def redrawGameWindow():
        gameWindow.fill(BLUE)
        drawBorders()
        drawStartEndPoints()
        drawScoreBoard()
        drawCharacter()
        drawKeys()
        drawCoins()
        drawObstacles()
        drawBullets()
        pygame.draw.rect(gameWindow,WHITE,(20,15,250,30),outline)
        pygame.draw.rect(gameWindow,WHITE,(530,15,250,30),outline)
        pygame.draw.rect(gameWindow,shopCLR,(30,65,50,10),outline)
        pygame.draw.polygon(gameWindow,shopCLR,((20,70),(30,60),(30,80)),outline)
        pygame.draw.rect(gameWindow,WHITE,(700,65,50,10),outline)
        pygame.draw.polygon(gameWindow,WHITE,((760,70),(750,60),(750,80)),outline)
# Change the level text depending on the level it is on
        if levelOne:
            graphicsTitle = font5.render("LEVEL 1",1,WHITE)
            graphicsKey = font2.render("Keys: " + str(keysCollected) + "/" + str(totalKeys),1,BLACK)
        elif levelTwo:
            graphicsTitle = font5.render("LEVEL 2",1,WHITE)
            graphicsKey = font2.render("Keys: " + str(keysCollected) + "/" + str(totalKeys),1,BLACK)
        elif levelThree:
            graphicsTitle = font5.render("LEVEL 3",1,WHITE)
            graphicsKey = font2.render("Keys: " + str(keysCollected) + "/" + str(totalKeys3),1,BLACK)
        elif levelFour:
            graphicsTitle = font5.render("LEVEL 4",1,WHITE)
            graphicsKey = font2.render("Keys: " + str(keysCollected) + "/" + str(totalKeys),1,BLACK)
        elif levelFive:
            graphicsTitle = font5.render("LEVEL 5",1,WHITE)
            graphicsKey = font2.render("Keys: " + str(keysCollected) + "/" + str(totalKeys),1,BLACK)
        graphicsDeath = font2.render("Deaths: " + str(deaths),1,BLACK)
        graphicsCoins = font2.render("Coins: " + str(coins),1,BLACK)
        graphicsGiveUp = font2.render("Give Up?",1,WHITE)
        graphicsShop = font2.render("Go to shop",1,shopCLR)
        graphicsKeyG = font10.render("PRESS 'G'",1,BLACK)
        graphicsKeyS = font10.render("PRESS 'S'",1,BLACK)
        
        gameWindow.blit(graphicsTitle,(295,0))
        gameWindow.blit(graphicsDeath,(630,117))
        gameWindow.blit(graphicsKey,(350,117))
        gameWindow.blit(graphicsCoins,(60,117))
        gameWindow.blit(graphicsGiveUp,(580,60))
        gameWindow.blit(graphicsShop,(95,60))
        gameWindow.blit(graphicsKeyG,(680,25))
        gameWindow.blit(graphicsKeyS,(50,25))
        pygame.display.update()
        clock.tick(FPS)

# Draw the power-up/upgrade screen
    def drawPowerUps():
        gameWindow.fill(DARK_BROWN)
# Draw the upgrade option buttons
        pygame.draw.rect(gameWindow,BROWN,(20,20,760,560),outline)
        pygame.draw.rect(gameWindow,BLACK,(50,70,170,30),outline)
        pygame.draw.rect(gameWindow,BLACK,(600,70,150,30),outline)
        pygame.draw.circle(gameWindow,BLACK,(138,250),75,4)
        pygame.draw.circle(gameWindow,BLACK,(313,250),75,4)
        pygame.draw.circle(gameWindow,BLACK,(488,250),75,4)
        pygame.draw.circle(gameWindow,BLACK,(663,250),75,4)
        pygame.draw.circle(gameWindow,upgrade1CLR,(138,250),71,outline)
        pygame.draw.circle(gameWindow,upgrade2CLR,(313,250),71,outline)
        pygame.draw.circle(gameWindow,upgrade3CLR,(488,250),71,outline)
        pygame.draw.circle(gameWindow,upgrade4CLR,(663,250),71,outline)
        pygame.draw.circle(gameWindow,RED,(138,250),50,outline)
        gameWindow.blit(boots,(270,200))
        gameWindow.blit(pistol,(440,205))
        pygame.draw.circle(gameWindow,GREY,(663,250),50,outline)
        pygame.draw.circle(gameWindow,DARK_GREY,(663,250),50,4)
        pygame.draw.polygon(gameWindow,playCLR,((440,510),(380,470),(380,550)),outline)
# Print the description for each upgrade available
        if slowObstacles:
            graphicsSlowObstacles = font7.render("Slower moving obstacles!",1,BLACK)
            gameWindow.blit(graphicsSlowObstacles,(slowObstaclesX,370))
        if fasterMovement:
            graphicsFasterMovement = font7.render("Increase movement speed!",1,BLACK)
            gameWindow.blit(graphicsFasterMovement,(fasterMovementX,370))
        if equipGun:
            graphicsEquipGun = font1.render("Equip an obstacle-destroying gun!",1,BLACK)
            graphicsInfo = font1.render("(3 bullets per level and press 'up' to shoot)",1,BLACK)
            gameWindow.blit(graphicsEquipGun,(equipGunX,340))
            gameWindow.blit(graphicsInfo,(infoX,380))
        if lessKeys:
            graphicsLessKeys = font7.render("Collect one less key to progress!",1,BLACK)
            gameWindow.blit(graphicsLessKeys,(lessKeysX,370))

        graphicsUpgrades = font5.render("UPGRADES",1,BLACK)
        gameWindow.blit(graphicsUpgrades,(250,40))
        pygame.display.update()

# Draw the game over screen
    def drawGameOver():
        gameWindow.fill(BLACK)
        pygame.draw.rect(gameWindow,buttonMainMenuCLR,(175,500,150,40),outline)
        pygame.draw.rect(gameWindow,buttonQuitCLR,(500,500,150,40),outline)
        graphicsMainMenu = font6.render("MAIN MENU",1,BLACK)
        graphicsQuit = font6.render("QUIT",1,BLACK)
        graphicsDeaths = font2.render("TOTAL NUMBER OF DEATHS: " + str(deaths),1,WHITE)
        graphicsCoins = font2.render("TOTAL NUMBER OF COINS COLLECTED: " + str(coins),1,WHITE)
        gameWindow.blit(endScreen,(200,70))
        gameWindow.blit(graphicsDeaths,(230,350))
        gameWindow.blit(graphicsCoins,(170,390))
        gameWindow.blit(graphicsMainMenu,(200,505))
        gameWindow.blit(graphicsQuit,(550,505))
        pygame.display.update()
    
    # Time properties
    clock = pygame.time.Clock()
    FPS = 64

    # Pictures and Sound
    endScreen = pygame.image.load("endScreen.jpg")
    castle = pygame.image.load("castle.png")
    dragon = pygame.image.load("dragon.png")
    tree = pygame.image.load("tree.png")
    tree1 = pygame.image.load("tree.png")
    tree2 = pygame.image.load("tree1.png")
    tree3 = pygame.image.load("tree3.png")
    tree4 = pygame.image.load("tree3.png")
    boots = pygame.image.load("boots.png")
    pistol = pygame.image.load("gun.png")
    bulletSound = pygame.mixer.Sound("bulletSound.wav")
    bulletSound.set_volume(0.8)
    jump = pygame.mixer.Sound("jump.wav")
    jump.set_volume(0.3)

    # Character properties
    knight = pygame.image.load("knight1.png")
    knightR = 21
    knightX = 60
    knightY = 495
    knightVx = 0
    knightVy = 0
    knightDir = "right"
    knightPicNum = 0
    knightPic = [0]*59
    
    for i in range(59):
        knightPic[i] = pygame.image.load("knight" + str(i) + ".png")

    # Animating sprite images
    nextLeftPic = [11,11,11,11,11,11,11,11,11,11,11,12,13,14,15,16,17,18,19,20,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11]
    nextRightPic = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    nextLeftPic2 = [22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,23,24,25,26,27,28,29,30,31,32,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22]
    nextRightPic2 = [33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,34,35,36,37,38,39,40,41,42,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33]
    rightGravityPic = [44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,33,44,44,44,44,44,44,44,44,44,44,45,46,47,48,49,50,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33]
    leftGravityPic2 = [50,50,50,50,50,50,50,50,50,50,50,11,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,11,44,45,46,47,48,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49]
    leftGravityPic = [51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,22,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,52,53,54,55,56,57,58,22,22,22,22,22,22,22]
    rightGravityPic2 = [0,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,0,51,52,53,54,55,56,57,58,58,58]
    leftOnly = False
    rightOnly = False

    # Obstacles properties
    circleX1 = [300,400,500,600]
    circleY1 = [200,200,200,200]
    circleX2 = [200,300,400,500,600,200,200]
    circleY2 = [200,200,200,200,200,325,375]
    circleX3 = [180,220,180,620,620,180,590,630,250,250,250,250,250,560,560,560,560,560]
    circleY3 = [180,180,190,270,450,530,180,180,300,330,360,390,420,300,330,360,390,420]
    circleX4 = [180,620,180,620,180,180,180,180,620,620,620,620]
    circleY4 = [195,250,520,465,310,340,370,400,310,340,370,400]
    circleX5 = [180,620,180,180,180,400,400,400]
    circleY5 = [250,250,190,355,530,190,355,530]
    circleR = 15
    stepX = [step,step,step,step]
    stepY = [step,step,step,step]
    stepX2 = [step,step,step,step,step,step,step]
    stepY2 = [step,step,step,step,step,step,step]
    stepX3 = [step-1,step-1,-step+2,-step+2,-step+2,step-2,step-1,step-1,step-5,step-5,step-5,step-5,step-5,step-5,step-5,step-5,step-5,step-5]
    stepY3 = [step-1,step-1,step-2,step-2,step-2,step-2,step-1,step-1,step-5,step-5,step-5,step-5,step-5,step-5,step-5,step-5,step-5,step-5]
    stepX4 = [step-1,step-1,step-1,step-1,step-3,step-3,step-3,step-3,-step+3,-step+3,-step+3,-step+3]
    stepY4 = [0,0,0,0,step-1,step-1,step-1,step-1,step-1,step-1,step-1,step-1]
    stepX5 = [step-1,-step+1,step-1,step-1,step-1,step-1,step-1,step-1,step-1,step-1,step-1,step-1,step-1,step-1]
    stepY5 = [step-3,step-3,0,0,0,0,0,0]

    # Key properties
    removedKeyX1 = []
    removedKeyY1 = []
    removedKeyX2 = []
    removedKeyY2 = []
    removedKeyX3 = []
    removedKeyY3 = []
    removedKeyX4 = []
    removedKeyY4 = []
    removedKeyX5 = []
    removedKeyY5 = []
    keyX1 = [250,250,550,550]
    keyY1 = [250,450,250,450]
    keyX2 = [200,600,400,400]
    keyY2 = [350,350,220,500]
    keyX3 = [400,400,220,220,580,580]
    keyY3 = [230,490,190,530,190,530]
    keyX4 = [400,400,270,530]
    keyY4 = [250,465,350,350]
    keyX5 = [250,450,350,550]
    keyY5 = [270,270,450,450]
    keyR = 12
    keysCollected = 0
    totalKeys3 = totalKeys + 2

    # Coin properties
    coinX = randint(152,645)
    coinY = randint(170,545)
    coinX2 = randint(580,645)
    coinY2 = randint(170,545)
    coinR = 12

    # Bullet properties
    bulletX = []
    bulletY = []
    bulletStep = 8
    bulletCount = 0
    
    # Main menu properties
    buttonX1 = 60
    buttonY1 = 190
    buttonX2 = 60
    buttonY2 = 250
    buttonX3 = 60
    buttonY3 = 310
    button1Width = 450
    button1Height = 50
    button2Width = 450
    button2Height = 50
    button3Width = 450
    button3Height = 50
    buttonClr1 = SKYBLUE
    buttonClr2 = SKYBLUE
    buttonClr3 = SKYBLUE
    buttonClr4 = SKYBLUE

    # In game properties
    GROUND_LEVEL = 495
    CEILING = 160
    knightG = 1
    gravity = False
    gravityCount = 0
    howToPlay = False

    # Level select properties
    levels = False

    # Shop properties
    shopCLR = WHITE
    shopCLR1 = SADDLE
    shopCLR2 = SADDLE
    shopCLR3 = SADDLE
    shopCLR4 = SADDLE
    shopCLR5 = SADDLE
    shopCLR6 = SADDLE
    shopCLR7 = SADDLE
    shopCLR8 = SADDLE
    shopCLR9 = SADDLE

    # Power up properties
    powerUp = False
    slowObstacles = False
    slowObstaclesX = 150
    fasterMovementX = 140
    fasterMovement = False
    equipGunX = 130
    infoX = 70
    equipGun = False
    lessKeysX = 70
    lessKeys = False
    playCLR = BLACK
    upgrade1CLR = TURQUOISE
    upgrade2CLR = TURQUOISE
    upgrade3CLR = TURQUOISE
    upgrade4CLR = TURQUOISE

    # Game over properties
    gameOver = False
    buttonMainMenuCLR = WHITE
    buttonQuitCLR = WHITE

# Main program
    while menu:
        mainMenu(buttonX1,buttonY1,buttonX2,buttonY2,buttonX3,buttonY3,button1Width,button1Height,button2Width,button2Height,button3Width,button3Height)

    # Getting mouse position
        (mouseX,mouseY) = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Play button
            if (mouseX >= 60 and mouseX <= 510) and (mouseY >= 190 and mouseY <= 240):
                buttonClr1 = GOLD
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        menu = False
                        howToPlay = True

            # Levels button
            elif (mouseX >= 60 and mouseX <= 510) and (mouseY >= 250 and mouseY <= 300):
                buttonClr2 = GOLD
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        menu = False
                        levels = True

            # Shop button   
            elif (mouseX >= 60 and mouseX <= 510) and (mouseY >= 310 and mouseY <= 360):
                buttonClr3 = GOLD
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        menu = False
                        shop = True
            # Quit button
            elif (mouseX >= 60 and mouseX <= 510) and (mouseY >= 370 and mouseY <= 420):
                buttonClr4 = GOLD
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        menu = False

            else:
                buttonClr1 = SKYBLUE
                buttonClr2 = SKYBLUE
                buttonClr3 = SKYBLUE
                buttonClr4 = SKYBLUE

    while shop:
        itemShop(shopCLR1,shopCLR2,shopCLR3,shopCLR4,shopCLR5,shopCLR6,shopCLR7,shopCLR8,shopCLR9)

        # Getting mouse position
        (mouseX,mouseY) = pygame.mouse.get_pos()

        keys = pygame.key.get_pressed()    
        if keys[pygame.K_ESCAPE]:
            main(True,True,False,False,coins,deaths,step,RUN_SPEED,totalKeys,gun,True,False,False,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)

        for event in pygame.event.get():
            # Shop item 1
            if (mouseX >= 200 and mouseX <= 275) and (mouseY >= 215 and mouseY <= 290) and coins >= 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        shopCLR1 = YELLOW
                        circleCLR = BLUE
                        coins = coins - 5
            # Shop item 2
            elif (mouseX >= 330 and mouseX <= 405) and (mouseY >= 215 and mouseY <= 290) and coins >= 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        shopCLR2 = YELLOW
                        circleCLR = GREEN
                        coins = coins - 5
            # Shop item 3
            elif (mouseX >= 460 and mouseX <= 535) and (mouseY >= 215 and mouseY <= 290) and coins >= 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        shopCLR3 = YELLOW
                        circleCLR = BLACK
                        coins = coins - 5
            # Shop item 4
            elif (mouseX >= 200 and mouseX <= 275) and (mouseY >= 330 and mouseY <= 405) and coins >= 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        shopCLR4 = YELLOW
                        keyCLR = ORANGE
                        keyCLR2 = DARK_ORANGE
                        coins = coins - 10
            # Shop item 5
            elif (mouseX >= 330 and mouseX <= 405) and (mouseY >= 330 and mouseY <= 405) and coins >= 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        shopCLR5 = YELLOW
                        keyCLR = PALE_TURQUOISE
                        keyCLR2 = TURQUOISE
                        coins = coins - 10
            # Shop item 6
            elif (mouseX >= 460 and mouseX <= 535) and (mouseY >= 330 and mouseY <= 405) and coins >= 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        shopCLR6 = YELLOW
                        keyCLR = WHITE
                        keyCLR2 = BLACK
                        coins = coins - 10
            # Shop item 7
            elif (mouseX >= 200 and mouseX <= 275) and (mouseY >= 445 and mouseY <= 520) and coins >= 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        shopCLR7 = YELLOW
                        backgroundCLR = PINK
                        coins = coins - 15
            # Shop item 8
            elif (mouseX >= 330 and mouseX <= 405) and (mouseY >= 445 and mouseY <= 520) and coins >= 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        shopCLR8 = YELLOW
                        backgroundCLR = LIGHT_YELLOW
                        coins = coins - 15
            # Shop item 9
            elif (mouseX >= 460 and mouseX <= 535) and (mouseY >= 445 and mouseY <= 520) and coins >= 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        shopCLR9 = YELLOW
                        backgroundCLR = LAVENDER
                        coins = coins - 15
            elif (mouseX >= 690 and mouseX <= 780) and (mouseY >= 220 and mouseY <= 360 ):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if levelOne:
                            main(False,False,True,False,coins,deaths,step,RUN_SPEED,totalKeys,gun,True,False,False,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
                        elif levelTwo:
                            main(False,False,True,False,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,True,False,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
                        elif levelThree:
                            main(False,False,True,False,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,False,True,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
                        elif levelFour:
                            main(False,False,True,False,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,False,False,True,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
                        elif levelFive:
                            main(False,False,True,False,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,False,False,False,True,circleCLR,keyCLR,keyCLR2,backgroundCLR)

    while levels:
        levelSelect()

        # Getting mouse position
        (mouseX2,mouseY2) = pygame.mouse.get_pos()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            main(True,True,False,False,0,0,5,5,4,False,True,False,False,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)

        for event in pygame.event.get():
        # Level one button
            if (mouseX2 >= 170 and mouseX2 <= 270) and (mouseY2 >= 200 and mouseY2 <= 300):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        main(False,True,True,False,0,0,5,5,4,False,True,False,False,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
        # Level two button
            elif (mouseX2 >= 350 and mouseX2 <= 450) and (mouseY2 >= 200 and mouseY2 <= 300):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        levels = False
                        powerUp = True
        # Level three button
            elif (mouseX2 >= 530 and mouseX2 <= 630) and (mouseY2 >= 200 and mouseY2 <= 300):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        levels = False
                        powerUp = True
                        levelOne = False
                        levelTwo = True
        # Level four button
            elif (mouseX2 >= 260 and mouseX2 <= 360) and (mouseY2 >= 360 and mouseY2 <= 460):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        levels = False
                        powerUp = True
                        levelOne = False
                        levelThree = True
        # Level five button
            elif (mouseX2 >= 440 and mouseX2 <= 540) and (mouseY2 >= 360 and mouseY2 <= 460):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        levels = False
                        powerUp = True
                        levelOne = False
                        levelFour = True
                    
    while howToPlay:
        rulesToPlay()

        pygame.event.clear()
        keys = pygame.key.get_pressed()
        
        # Press 'p' to continue to the game
        if keys[pygame.K_p]:
            howToPlay = False
            inPlay = True

        if keys[pygame.K_ESCAPE]:
            howToPlay = False
            main(True,True,False,False,0,0,5,5,4,False,True,False,False,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)

    while inPlay:
        redrawGameWindow()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Press 'space' to switch gravity
                if event.key == pygame.K_SPACE:
                    jump.play()
                    knightG = 1
                    gravity = True
                    leftOnly = True
                    rightOnly = True
                    gravityCount = gravityCount + 1
                # Press 'up' with the gun upgrade to shoot
                elif event.key == pygame.K_UP and gun and bulletCount < 3:
                    bulletSound.play()
                    bulletX.append(knightX+30)
                    bulletY.append(knightY+20)
                    bulletCount = bulletCount + 1

        # Press 'escape' to go to the main menu
        keys = pygame.key.get_pressed()    
        if keys[pygame.K_ESCAPE]:
            main(True,True,False,False,0,0,5,5,4,False,True,False,False,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)

        # Move the character to the left
        if keys[pygame.K_LEFT] and knightX > 35:
            knightVx = -RUN_SPEED
            knightDir = "left"
            if knightY == GROUND_LEVEL:
                knightPicNum = nextLeftPic[knightPicNum]
            elif knightY == CEILING:
                knightPicNum = nextLeftPic2[knightPicNum]
            elif levelThree and knightY == 238:
                knightPicNum = nextLeftPic[knightPicNum]
            elif levelThree and knightY == 417:
                knightPicNum = nextLeftPic2[knightPicNum]
        # Move the character to the right
        elif keys[pygame.K_RIGHT] and knightX < 700:
            knightVx = RUN_SPEED
            knightDir = "right"
            if knightY == GROUND_LEVEL:
                knightPicNum = nextRightPic[knightPicNum]
            elif knightY == CEILING:
                knightPicNum = nextRightPic2[knightPicNum]
            elif levelThree and knightY == 238:
                knightPicNum = nextRightPic[knightPicNum]
            elif levelThree and knightY == 417:
                knightPicNum = nextRightPic2[knightPicNum]
        # Default position for the character depending on the direction they are facing
        else:
            knightVx = 0
            if knightDir == "left" and knightY == GROUND_LEVEL or (knightDir == "left" and knightY == 238 and knightX >= 250 and knightX <= 560 and levelThree):
                knightPicNum = 11
            elif knightDir == "right" and knightY == GROUND_LEVEL or (knightDir == "right" and knightY == 238 and knightX >= 250 and knightX <= 560 and levelThree):
                knightPicNum = 0
            elif knightDir == "left" and knightY == CEILING or (knightDir == "left" and knightY == 417 and knightX >= 250 and knightX <= 560 and levelThree):
                knightPicNum = 22
            elif knightDir == "right" and knightY == CEILING or (knightDir == "right" and knightY == 417 and knightX >= 250 and knightX <= 560 and levelThree):
                knightPicNum = 33

        # Press 'g' to go to the game over screen
        if keys[pygame.K_g]:
            inPlay = False
            gameOver = True

        # Press 's' to go to the shop menu
        if keys[pygame.K_s]:
            if levelOne:
                main(False,False,False,True,coins,deaths,step,RUN_SPEED,totalKeys,gun,True,False,False,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
            elif levelTwo:
                main(False,False,False,True,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,True,False,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
            elif levelThree:
                main(False,False,False,True,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,False,True,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
            elif levelFour:
                main(False,False,False,True,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,False,False,True,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
            elif levelFive:
                main(False,False,False,True,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,False,False,False,True,circleCLR,keyCLR,keyCLR2,backgroundCLR)

        # Update the position of the character
        knightX = knightX + knightVx

        # Switching the gravity from the floor to the ceiling
        if gravity and gravityCount % 2 != 0:
            if knightDir == "right" and rightOnly:
                knightPicNum = rightGravityPic[knightPicNum]
                leftOnly = False
            elif knightDir == "left" and leftOnly:
                knightPicNum = leftGravityPic[knightPicNum]
                rightOnly = False
            knightY = knightY - knightG
            knightG = knightG + 1
            if knightY <= CEILING:
                knightY = CEILING
                gravity = False
        # Switching the gravity from the ceiling to the floor
        elif gravity and gravityCount % 2 == 0:
            if knightDir == "right" and rightOnly:
                knightPicNum = rightGravityPic2[knightPicNum]
                leftOnly = False
            elif knightDir == "left" and leftOnly:
                knightPicNum = leftGravityPic2[knightPicNum]
                rightOnly = False
            knightY = knightY + knightG
            knightG = knightG + 1
            if knightY >= GROUND_LEVEL:
                knightY = GROUND_LEVEL
                gravity = False

        # Prevent the knight from moving out of the boundaries
        if knightY == CEILING or knightY == GROUND_LEVEL:
            knightG = 1
        
# Moving the obstacles in level one
        for i in range(len(circleX1)):
            circleX1[i] = circleX1[i] + stepX[i]
            circleY1[i] = circleY1[i] + stepY[i]

# Bouncing the obstacles off of the walls in level one
            if circleX1[i] > 640 or circleX1[i] < 160:
                stepX[i] = -stepX[i]
            if circleY1[i] > 540 or circleY1[i] < 180:
                stepY[i] = -stepY[i]

# Moving the obstacles in level two
        for i in range(len(circleX2)-2):
            circleY2[i] = circleY2[i] + stepY2[i]

            if circleY2[i] > 540 or circleY2[i] < 180:
                stepY2[i] = -stepY2[i]

        for i in range(5,len(circleX2)):
            circleX2[i] = circleX2[i] + stepX2[i]

            if circleX2[i] > 650 or circleX2[i] < 150:
                stepX2[i] = -stepX2[i]

# Moving the obstacles in level three
        for i in range(len(circleX3)-16):
            circleY3[i] = circleY3[i] + stepY3[i]

            if circleY3[i] > 540 or circleY3[i] < 180:
                stepY3[i] = -stepY3[i]

        for i in range(2,(len(circleX3))-12):
            circleX3[i] = circleX3[i] + stepX3[i]

            if circleX3[i] > 620 or circleX3[i] < 180:
                stepX3[i] = -stepX3[i]

        for i in range(6,(len(circleX3))-10):
            circleY3[i] = circleY3[i] + stepY3[i]

            if circleY3[i] > 540 or circleY3[i] < 180:
                stepY3[i] = -stepY3[i]

# Moving the obstacles in level four
        for i in range(2):
            if circleX4[i] == 620 and circleY4[i] == 195:
                stepX4[i] = 0
                stepY4[i] = 5
            elif circleX4[i] == 620 and circleY4[i] == 250:
                stepX4[i] = -4
                stepY4[i] = 0
            elif circleX4[i] == 180 and circleY4[i] == 250:
                stepX4[i] = 0
                stepY4[i] = -5
            elif circleX4[i] == 180 and circleY4[i] == 195:
                stepX4[i] = 4
                stepY4[i] = 0

            circleX4[i] = circleX4[i] + stepX4[i]
            circleY4[i] = circleY4[i] + stepY4[i]

        for i in range(2,4):
            if circleX4[i] == 620 and circleY4[i] == 520:
                stepX4[i] = 0
                stepY4[i] = -5
            elif circleX4[i] == 620 and circleY4[i] == 465:
                stepX4[i] = -4
                stepY4[i] = 0
            elif circleX4[i] == 180 and circleY4[i] == 465:
                stepX4[i] = 0
                stepY4[i] = 5
            elif circleX4[i] == 180 and circleY4[i] == 520:
                stepX4[i] = 4
                stepY4[i] = 0

            circleX4[i] = circleX4[i] + stepX4[i]
            circleY4[i] = circleY4[i] + stepY4[i]

        for i in range(4,8):
            circleX4[i] = circleX4[i] + stepX4[i]

            if circleX4[i] >= 380 or circleX4[i] <= 180:
                stepX4[i] = -stepX4[i]

        for i in range(8,12):
            circleX4[i] = circleX4[i] + stepX4[i]

            if circleX4[i] <= 420 or circleX4[i] >= 620:
                stepX4[i] = -stepX4[i]

# Moving the obstacles in level five
        for i in range(len(circleX5)):
            pygame.draw.circle(gameWindow,circleCLR,(circleX5[i],circleY5[i]),circleR,outline)

        for i in range(len(keyX5)-1,-1,-1):
            pygame.draw.circle(gameWindow,keyCLR,(keyX5[i],keyY5[i]),keyR,outline)
            pygame.draw.circle(gameWindow,DARK_GREY,(keyX5[i],keyY5[i]),keyR,3)    
            
        for i in range(2):
            circleX5[i] = circleX5[i] + stepX5[i]
            circleY5[i] = circleY5[i] + stepY5[i]

            if circleX5[i] >= 630 or circleX5[i] <= 170:
                stepX5[i] = -stepX5[i]
                stepY5[i] = -stepY5[i]

        for i in range(2,5):
            circleX5[i] = circleX5[i] + stepX5[i]

            if circleX5[i] >= 400 or circleX5[i] <= 170:
                stepX5[i] = -stepX5[i]

        for i in range(5,len(circleX5)):
            circleX5[i] = circleX5[i] + stepX5[i]

            if circleX5[i] >= 630 or circleX5[i] <= 402:
                stepX5[i] = -stepX5[i]

# Stop the game when the character reaches the finish line
        if levelOne or levelTwo or levelFour:
            if knightX > 660 and keysCollected >= totalKeys:
                inPlay = False
                powerUp = True
        elif levelThree:
            if knightX > 660 and keysCollected >= totalKeys3:
                inPlay = False
                powerUp = True
        elif levelFive:
            if knightX > 660 and keysCollected >= totalKeys:
                inPlay = False
                gameOver = True

# Moving and decaying the bullets
        for i in range(len(bulletX)-1,-1,-1):
            bulletX[i] = bulletX[i] + bulletStep
            if bulletX[i] > 800:
                bulletX.pop(i)
                bulletY.pop(i)

# Checking for collision between bullets and obstacles in each level
        if levelTwo and gun:
            for i in range(len(circleX2)):
                for j in range(len(bulletX)-1,-1,-1):
                    if distance(circleX2[i],circleY2[i],bulletX[j],bulletY[j]) < circleR + 10:
                        bulletX.pop(j)
                        bulletY.pop(j)
                        circleX2[i] = -1000
                        circleY2[i] = -1000
        elif levelThree and gun:
            for i in range(len(circleX3)):
                for j in range(len(bulletX)-1,-1,-1):
                    if distance(circleX3[i],circleY3[i],bulletX[j],bulletY[j]) < circleR + 10:
                        bulletX.pop(j)
                        bulletY.pop(j)
                        circleX3[i] = -1000
                        circleY3[i] = -1000
        elif levelFour and gun:
            for i in range(len(circleX4)):
                for j in range(len(bulletX)-1,-1,-1):
                    if distance(circleX4[i],circleY4[i],bulletX[j],bulletY[j]) < circleR + 10:
                        bulletX.pop(j)
                        bulletY.pop(j)
                        circleX4[i] = -1000
                        circleY4[i] = -1000
        elif levelFive and gun:
            for i in range(len(circleX5)):
                for j in range(len(bulletX)-1,-1,-1):
                    if distance(circleX5[i],circleY5[i],bulletX[j],bulletY[j]) < circleR + 10:
                        bulletX.pop(j)
                        bulletY.pop(j)
                        circleX5[i] = -1000
                        circleY5[i] = -1000  

# Checking for collision between the character and the obstacles
        if levelOne:
            countingDeaths(knightX,knightY,circleX1,circleY1)
            if countingDeaths(knightX,knightY,circleX1,circleY1):
                gravity = False
                gravityCount = 0
                knightX = 60
                knightY = GROUND_LEVEL
                deaths = deaths + 1
                keysCollected = 0
                keyX1 = keyX1 + removedKeyX1
                keyY1 = keyY1 + removedKeyY1
                removedKeyX1 = []
                removedKeyY1 = []
        elif levelTwo:
            countingDeaths(knightX,knightY,circleX2,circleY2)
            if countingDeaths(knightX,knightY,circleX2,circleY2):
                gravity = False
                gravityCount = 0
                knightX = 60
                knightY = GROUND_LEVEL
                deaths = deaths + 1
                keysCollected = 0
                keyX2 = keyX2 + removedKeyX2
                keyY2 = keyY2 + removedKeyY2
                removedKeyX2 = []
                removedKeyY2 = []
        elif levelThree:
            countingDeaths(knightX,knightY,circleX3,circleY3)
            if countingDeaths(knightX,knightY,circleX3,circleY3):
                gravity = False
                gravityCount = 0
                knightX = 60
                knightY = GROUND_LEVEL
                deaths = deaths + 1
                keysCollected = 0
                keyX3 = keyX3 + removedKeyX3
                keyY3 = keyY3 + removedKeyY3
                removedKeyX3 = []
                removedKeyY3 = []
        elif levelFour:
            countingDeaths(knightX,knightY,circleX4,circleY4)
            if countingDeaths(knightX,knightY,circleX4,circleY4):
                gravity = False
                gravityCount = 0
                knightX = 60
                knightY = GROUND_LEVEL
                deaths = deaths + 1
                keysCollected = 0
                keyX4 = keyX4 + removedKeyX4
                keyY4 = keyY4 + removedKeyY4
                removedKeyX4 = []
                removedKeyY4 = []
        elif levelFive:
            countingDeaths(knightX,knightY,circleX5,circleY5)
            if countingDeaths(knightX,knightY,circleX5,circleY5):
                gravity = False
                gravityCount = 0
                knightX = 60
                knightY = GROUND_LEVEL
                deaths = deaths + 1
                keysCollected = 0
                keyX5 = keyX5 + removedKeyX5
                keyY5 = keyY5 + removedKeyY5
                removedKeyX5 = []
                removedKeyY5 = []

# Checking for when the character picks up a key      
        if levelOne: 
            for i in range(len(keyX1)-1,-1,-1):
                if distance(keyX1[i],keyY1[i],knightX + 30,knightY + 40) < keyR + knightR:
                    removedKeyX1.append(keyX1[i])
                    removedKeyY1.append(keyY1[i])
                    keyX1.pop(i)
                    keyY1.pop(i)
                    keysCollected = keysCollected + 1
        elif levelTwo:
            for i in range(len(keyX2)-1,-1,-1):
                if distance(keyX2[i],keyY2[i],knightX + 30,knightY + 40) < keyR + knightR:
                    removedKeyX2.append(keyX2[i])
                    removedKeyY2.append(keyY2[i])
                    keyX2.pop(i)
                    keyY2.pop(i)
                    keysCollected = keysCollected + 1
        elif levelThree:
            for i in range(len(keyX3)-1,-1,-1):
                if distance(keyX3[i],keyY3[i],knightX + 30,knightY + 40) < keyR + knightR:
                    removedKeyX3.append(keyX3[i])
                    removedKeyY3.append(keyY3[i])
                    keyX3.pop(i)
                    keyY3.pop(i)
                    keysCollected = keysCollected + 1
        elif levelFour:
            for i in range(len(keyX4)-1,-1,-1):
                if distance(keyX4[i],keyY4[i],knightX + 30,knightY + 40) < keyR + knightR:
                    removedKeyX4.append(keyX4[i])
                    removedKeyY4.append(keyY4[i])
                    keyX4.pop(i)
                    keyY4.pop(i)
                    keysCollected = keysCollected + 1
        elif levelFive:
            for i in range(len(keyX5)-1,-1,-1):
                if distance(keyX5[i],keyY5[i],knightX + 30,knightY + 40) < keyR + knightR:
                    removedKeyX5.append(keyX5[i])
                    removedKeyY5.append(keyY5[i])
                    keyX5.pop(i)
                    keyY5.pop(i)
                    keysCollected = keysCollected + 1

# Generating the coins at random coordinates once picked up
        if levelThree:
            if distance(coinX2,coinY2,knightX + 30, knightY + 40) < coinR + knightR:
                coinX2 = randint(580,645)
                coinY2 = randint(170,545)
                coins = coins + 1
        else:
            if distance(coinX,coinY,knightX + 30,knightY + 40) < coinR + knightR:
                coinX = randint(152,645)
                coinY = randint(170,545)
                coins = coins + 1

# Checking for platform in level three
        if levelThree:
            if knightX >= 250 and knightX <= 560 and knightY >= 238 and knightY <= 417:
                knightG = 0
                gravity = False

    while powerUp:
        drawPowerUps()

        # Getting mouse position
        (mouseX,mouseY)= pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            # Upgrade button 1
            if equationCircle(mouseX,mouseY,138,250) < 75**2:
                slowObstaclesX = 150
                slowObstacles = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        upgrade1CLR = YELLOW
                        upgrade2CLR = TURQUOISE
                        upgrade3CLR = TURQUOISE
                        upgrade4CLR = TURQUOISE
            # Upgrade button 2
            elif equationCircle(mouseX,mouseY,313,250) < 75**2:
                fasterMovementX = 140
                fasterMovement = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        upgrade1CLR = TURQUOISE
                        upgrade2CLR = YELLOW
                        upgrade3CLR = TURQUOISE
                        upgrade4CLR = TURQUOISE
            # Upgrade button 3
            elif equationCircle(mouseX,mouseY,488,250) < 75**2:
                equipGunX = 130
                infoX = 70
                equipGun = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        upgrade1CLR = TURQUOISE
                        upgrade2CLR = TURQUOISE
                        upgrade3CLR = YELLOW
                        upgrade4CLR = TURQUOISE
            # Upgrade button 4
            elif equationCircle(mouseX,mouseY,663,250) < 75**2:
                lessKeysX = 70
                lessKeys = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        upgrade1CLR = TURQUOISE
                        upgrade2CLR = TURQUOISE
                        upgrade3CLR = TURQUOISE
                        upgrade4CLR = YELLOW
            # Play button
            elif (mouseX >= 380 and mouseX <= 440) and (mouseY >= 470 and mouseY <= 550):
                playCLR = GREEN
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if upgrade1CLR == YELLOW:
                            step = 4
                            totalKeys = 4
                            RUN_SPEED = 5
                            gun = False
                        elif upgrade2CLR == YELLOW:
                            step = 5
                            totalKeys = 4
                            RUN_SPEED = 7
                            gun = False
                        elif upgrade3CLR == YELLOW:
                            step = 5
                            totalKeys = 4
                            RUN_SPEED = 5
                            gun = True
                        elif upgrade4CLR == YELLOW:
                            step = 5
                            RUN_SPEED = 5
                            totalKeys = 3
                            gun = False
                            
                        if levelOne:
                            main(False,False,True,False,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,True,False,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
                        elif levelTwo:
                            main(False,False,True,False,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,False,True,False,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
                        elif levelThree:
                            main(False,False,True,False,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,False,False,True,False,circleCLR,keyCLR,keyCLR2,backgroundCLR)
                        elif levelFour:
                            main(False,False,True,False,coins,deaths,step,RUN_SPEED,totalKeys,gun,False,False,False,False,True,circleCLR,keyCLR,keyCLR2,backgroundCLR)

            else:
                slowObstaclesX = -1000
                fasterMovementX = -1000
                equipGunX = -1000
                infoX = -1000
                lessKeysX = -1000
                playCLR = BLACK

    while gameOver:
        drawGameOver()

        # Getting mouse position
        (mouseX3,mouseY3) = pygame.mouse.get_pos()

        for event in pygame.event.get():

            # Main menu button
            if (mouseX3 >= 175 and mouseX3 <= 325) and (mouseY3 >= 500 and mouseY3 <= 540):
                buttonMainMenuCLR = GREEN
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        main(True,True,False,False,0,0,5,5,4,False,True,False,False,False,False,RED,GREY,DARK_GREY,WHITE)

            # Quit button
            elif (mouseX3 >= 500 and mouseX3 <= 650) and (mouseY3 >= 500 and mouseY3 <= 540):
                buttonQuitCLR = RED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        gameOver = False
                        
            else:
                buttonMainMenuCLR = WHITE
                buttonQuitCLR = WHITE

    # Stop the music and exit pygame
    pygame.mixer.music.stop()
    pygame.quit()

# Calling the main function
main(True,True,False,False,0,0,5,5,4,False,True,False,False,False,False,RED,GREY,DARK_GREY,WHITE)





