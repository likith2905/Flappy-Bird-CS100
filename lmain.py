import random # For generating random numbers
import sys # We will use sys.exit to exit the program
import pygame
from pygame.locals import * # Basic pygame imports

# Global Variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
RED='gallery/sprites/rb.png'
YELLOW='gallery/sprites/yb.png'
GREEN='gallery/sprites/gb.png'
BACKGROUND = 'gallery/sprites/background.png'
NIGHT='gallery/sprites/night.png'
DESERT='gallery/sprites/deserttt.jpg'
HAUNTED='gallery/sprites/bghaunted.png'
PIPE = 'gallery/sprites/pipe.png'
HP='gallery/sprites/hauntedpipe.png'
HPL='gallery/sprites/hauntedpipel.png'
PIPENGT='gallery/sprites/pipengt.png'
GAMEOVER='gallery/sprites/gameover1.png'
MODEPAGE='gallery/sprites/modes.png'
BIRDPAGE='gallery/sprites/bmode.png'
a=0

def welcomeScreen():
    """
    Shows welcome images on the screen
    """
    messagex = 0
    messagey = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:    
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))      
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def modeScreen():
    """
    Shows welcome images on the screen
    """
    messagex = 0
    messagey = 0
    global a
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                a=0
                GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
                GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
                pygame.image.load(PIPE).convert_alpha())
                return

            elif event.type==KEYDOWN and (event.key==K_n):
                a=0
                GAME_SPRITES['background']=pygame.image.load(NIGHT).convert()
                GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPENGT).convert_alpha(), 180), 
                pygame.image.load(PIPENGT).convert_alpha())
                return
            
            elif event.type==KEYDOWN and (event.key==K_d):
                a=1
                GAME_SPRITES['background']=pygame.image.load(DESERT).convert()
                GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
                pygame.image.load(PIPE).convert_alpha())
                return

            elif event.type==KEYDOWN and (event.key==K_h):
                a=1
                GAME_SPRITES['background']=pygame.image.load(HAUNTED).convert()
                GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load(HP).convert_alpha(), 180), 
                pygame.image.load(HPL).convert_alpha())
                return

            else:    
                SCREEN.blit(GAME_SPRITES['modepage'], (messagex,messagey ))      
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def birdScreen():
    """
    Shows welcome images on the screen
    """
    messagex = 0
    messagey = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_c):
                GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha()
                return

            elif event.type==KEYDOWN and (event.key==K_r):
                GAME_SPRITES['player']=pygame.image.load(RED).convert_alpha()
                return
            
            elif event.type==KEYDOWN and (event.key==K_y):
                GAME_SPRITES['player']=pygame.image.load(YELLOW).convert_alpha()
                return

            elif event.type==KEYDOWN and (event.key==K_g):
                GAME_SPRITES['player']=pygame.image.load(GREEN).convert_alpha()
                return

            else:    
                SCREEN.blit(GAME_SPRITES['birdpage'], (messagex,messagey ))      
                pygame.display.update()
                FPSCLOCK.tick(FPS)                

def gameover():
    """
    Shows welcome images on the screen
    """
    messagex = 0
    messagey = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game  
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else: 
                SCREEN.blit(GAME_SPRITES['gameover'], (messagex,messagey ))   
                myDigits = [int(x) for x in list(str(score))]
                width = 0
                for digit in myDigits:
                    width += GAME_SPRITES['numbersb'][digit].get_width()
                Xoffset = (SCREENWIDTH - width)/2

                for digit in myDigits:
                    SCREEN.blit(GAME_SPRITES['numbersb'][digit], (Xoffset, SCREENHEIGHT*0.63))
                    Xoffset += GAME_SPRITES['numbersb'][digit].get_width()
                pygame.display.update()
                FPSCLOCK.tick(FPS)   
score=0
def mainGame():
    global score
    score=0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0 

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
    ]

    pipeVelX = -4
    
    playerVelY = -9
    playerMaxVelY = 10
    playerAccY = 1

    

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # It is true only when the bird is flapping


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()


        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
        if crashTest:
            return   

        #check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                print(f"Your score is {score}") 
                GAME_SOUNDS['point'].play()

           
        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = GAME_SPRITES['player'].get_height()
        if a==0:
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)
        else:
            playery = playery + playerVelY
        # move pipes to the left
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        
        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        if a==0:
            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if a==1:
        if playery> 486  or playery<0:
            GAME_SOUNDS['hit'].play()
            return True
    else:
        if playery> GROUNDY - 25  or playery<0:
            GAME_SOUNDS['hit'].play()
            return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()): 
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    return False

def getRandomPipe():
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2} #lower Pipe
    ]
    return pipe






if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.init() # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('CS 100/101 FLAPPY BIRD')
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['numbersb'] = ( 
        pygame.image.load('gallery/sprites/0b.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1b.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2b.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3b.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4b.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5b.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6b.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7b.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8b.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9b.png').convert_alpha(),
    )

    GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
    pygame.image.load(PIPE).convert_alpha()
    )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['gameover'] = pygame.image.load(GAMEOVER).convert_alpha()
    GAME_SPRITES['modepage'] = pygame.image.load(MODEPAGE).convert_alpha()
    GAME_SPRITES['birdpage'] = pygame.image.load(BIRDPAGE).convert_alpha()
    while True:
        welcomeScreen() # Shows welcome screen to the user until he presses a button
        modeScreen()
        birdScreen()
        mainGame() # This is the main game function 
        gameover()
