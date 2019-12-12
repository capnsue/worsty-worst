# starting template to make breakout clone


import pygame
import random

from pygame.locals import(
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


#########################################################################################################
#
# classes
#
#########################################################################################################


# this class describes a block (player and bricks)
# maybe it could also describe the bricks?
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # constructor

        super().__init__()

        # create image of block, fill w color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # get rectangle of image that has the dimensions
        self.rect = self.image.get_rect()
############################################################################################################




pygame.init()




WIDTH = 800
HEIGHT = 600

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("breaky 1")

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# make a bunch of blocks
for i in range(50):
    # make a block object
    block = Block(BLACK, 20, 15)

    # put in random location
    block.rect.x = random.randrange(WIDTH)
    block.rect.y = random.randrange(HEIGHT)

    # add to list of sprites
    block_list.add(block)
    all_sprites_list.add(block)
    
# create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)


# loop until the user clicks close 
running = True

# get a timer for a sane frame rate
clock = pygame.time.Clock()

# oooh keep SCORE
score = 0

###########################################################################
#      game loop
#
###########################################################################

while running:
    # process event Q
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            # was it escape? if so quit
            if event.key == K_ESCAPE:
                running = False
            

    # get current mouse position as list (x,y) coords
    pos = pygame.mouse.get_pos()
# ------------------------------------------------------------

    # do stuff!
    
    # set player position from mouse coords
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # check if player block collided with any of the block in block_list
    # if so, kill the block
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    
    # give them a score for each block they hit
    for block in blocks_hit_list:
        score += 1
        print(score)
        
# --------------------------------------------------
    # draw stuff on screen!
    
    # clear the screen, fill w white
    screen.fill(WHITE)
    
    # draw all the sprites
    all_sprites_list.draw(screen)
    
    # update the screen and show it
    pygame.display.flip()
    
    # limit to 60 frames per second
    clock.tick(60)

###################################################################
#  end of game loop
    
pygame.quit()


    
    
    










 


 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()