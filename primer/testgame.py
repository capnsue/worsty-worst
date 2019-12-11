

# simple pygame program

# import and initalize
import pygame
pygame.init()

S_WIDTH = 640
S_HEIGHT = 480

# set up drawing window
screen = pygame.display.set_mode([S_WIDTH,S_HEIGHT])   # instructions say 500x500 but doing
                                                         # this so i can get the width and height
                                                         # under my fingers

# run until user asks to quit
running = True
while running:

    # did the user close the window?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill background w white
    screen.fill((255,255,255))                                                         

    # draw blue circle
    pygame.draw.circle(screen, (0,0,255), (250,250), 75)

    # flip the display
    pygame.display.flip()

# done, quit
pygame.quit()

