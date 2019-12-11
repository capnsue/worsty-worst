import pygame
pygame.init()

#create a window of 500x500

S_WIDTH = 500
S_HEIGHT = 500

win = pygame.display.set_mode((S_WIDTH, S_HEIGHT))

pygame.display.set_caption("the worsty worst")

#game stuff

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#constants / init vals
# starting point of rectangle
x = 400
y = 400

width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

# jumping stuff
isJump = False
jumpCount = 10

# animation stuff?
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    # we have 9 images for our walking animation
    # i want to the same image for 3 frames
    # so i use the number 27 as an upper bound for walkCount
    # because 27 / 3 = 9.  9 images.  
    # 9 images shown 3x each animation.  

    win.blit(bg, (0,0)) # draw bg image at 0,0 (blit)
    
    if walkCount + 1 >= 27:
        walkCount = 0
    
    if left: # if we are facing left
        win.blit(walkLeft[walkCount//3], (x,y)) # figure out where in walkCount we are, draw right image
                                                    # why not use mod %
                                                    # in python // means "integer divide" ..ok
        walkCount += 1  # blah can't do x++ in python
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y)) # character is standing still
        walkCount = 0

    pygame.display.update()



# game loop!
run = True

while run:
    # pygame.time.delay(100) # delay the game 100ms (why)
    clock.tick(27)   

    for event in pygame.event.get(): # loop through event queue (key/mouse events)
        if event.type == pygame.QUIT: # the user has clicked the X button or whatever
            run = False  # ends game loop

        # is this event a key press event? if so which one

        keys = pygame.key.get_pressed() # dictionary, k/v: key/0 or 1 


        ####################################################
        # pygame is weird
        # the coords system goes like this
        # the top left corner is (0,0) 
        # x = 0  y = 0
        # 
        # the bottom right is (width, height)
        # x = width  y = height
        #
        # to move up, subtract y
        # to move down, add y
        # this makes no sense to me right now
        # but there must be a reason for it
        #
        #
        # (0,0)-----------------------(width,0)
        # |
        # |
        # |
        # |
        # |
        # |
        # (0,height)-------------------(width,height)
        #
        # this will be hard to remember ugh


        
        if keys[pygame.K_LEFT] and  (x > vel):  
            x -= vel
            left = True
            right = False

        if keys[pygame.K_RIGHT] and (x < S_WIDTH - vel - width):
            x += vel
            left = False
            right = True
        
        else: # If the character is not  moving we will set both
              # left and right to false and reset the walkCount
              # (walkCount = animationCounter)
            left = False
            right = False
            walkCount = 0

        if not(isJump): # check if we are jumping right now if so, 
                        # disable up and down keys
        
            if keys[pygame.K_UP] and (y > vel):
                y -= vel
            if keys[pygame.K_DOWN] and (y < S_HEIGHT - height - vel):
                y += vel
            # did they jump this time
            if keys[pygame.K_SPACE]:
                isJump = True
        
        # ok we are jumping
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False

    # now the important stuff of drawing on the screen goes here

    # redrawGameWindow() somehow does all this stuff??
    redrawGameWindow()

    
    #fill screen with black to erase previous stuff..rectangles
    # win.fill((0,0,0))

    # draw a dang rectangle in the new spot
    # pygame.draw.rect(win, (255,0,0), (x, y, width, height)) # window, color, co-ords of rectangle to draw

    # pygame.display.update() #updates the screen


pygame.quit()




