# starting template to make breakout clone
# with thanks to programarcadegames.com
# break2.py -- attempt to organize classes in a nice OO way


import pygame
import random

#-------------global constants----------------------------#
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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


#########################################################################################################
#
# classes
#
#########################################################################################################


# a simple block the player collects
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # constructor

        super().__init__()

        # create image of block, fill w color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # get rectangle of image that has the dimensions
        self.rect = self.image.get_rect()
    
    def update(self):
        # called each frame
        # move block down one pixel
        self.rect.y += 1
        # if blocks go off the bottom of the screen,
        # send them back to the top
        if self.rect.y > SCREEN_HEIGHT + 100: # docs say 410, why
            self.reset_pos()
 

    def reset_pos(self):
        # reset position at top of screen at random x location
        # called by update() or if there is a collision
        self.rect.y = random.randrange(-300, -20) # i dont understand why these numbers
        self.rect.x = random.randrange(0, SCREEN_WIDTH)

# player class (real similar to block)
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # constructor

        super().__init__()

        # create image of block, fill w color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # get rectangle of image that has the dimensions
        self.rect = self.image.get_rect()

    def update(self):
        
        # Update the player location
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

# game class.  if we need to reset the game, just make a new instance
# of this class
class Game(object):
    def __init__(self):

        self.score = 0
        self.game_over = False

        # create sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # create block sprites
        # make a bunch of blocks
        for i in range(50):
            # make a block object
            block = Block(BLACK, 20, 15)

            # put in random location
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT)

            # add to list of sprites
            self.block_list.add(block)
            self.all_sprites_list.add(block)

        # create the player
        self.player = Player(RED, 20,20)
        self.all_sprites_list.add(self.player)

    def process_events(self):
        # process all events.  returns "True" if we need to close the window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        
        return False

    def run_logic(self):
        # this runs for each frame.  
        # updates positions and checks for collisons

        if not self.game_over:
            # move all sprites (call each sprite's update()  method)
            self.all_sprites_list.update()

            # check if player block has collided with anything
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)
            
            # go through hit list and update score
            for block in blocks_hit_list:
                self.score += 1
                print(self.score)

            if len(self.block_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        # display everything that needs to go to the screen
        screen.fill(WHITE)

        if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
        
        if not self.game_over:
            self.all_sprites_list.draw(screen)
        
        pygame.display.flip()

#-------end of classes--------------------------------------------------------------------------------------------------------------


def main():
    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("breaky 2")
    pygame.mouse.set_visible(False)

    # create our objects 
    done = False
    clock = pygame.time.Clock()

    # create instance of Game!
    mygame = Game()

    # main game loop
    while not done:

        # process events: mouse clicks, keys
        done = mygame.process_events()

        # update object positions and check for collisions
        mygame.run_logic()

        # draw the current frame
        mygame.display_frame(screen)

        # pause for the next frame
        clock.tick(60)

    # done, close window and exit
    pygame.quit()

# call main function using magic incantiation, start up
if __name__ == "__main__":
    main()










