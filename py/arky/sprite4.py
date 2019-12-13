# trying to port my crappy breaky to pyarcade

# better keyboard movement
# and now the coins move


import random
import arcade
import os

#-----constants
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN= 0.2
COIN_COUNT = 50

MOVEMENT_SPEED = 5


SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
SCREEN_TITLE = "coin rain"


#-------------------------------------------
#
#               classes
#
#--------------------------------------------

class Coin(arcade.Sprite):
    
    def reset_pos(self):
        # reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)
        
        
    def update(self):
        # move the coin
        self.center_y -= 1
            
        # check if coin has fallen off screen
        # if so, reset it
        if self.top < 0:
            self.reset_pos()
            

class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        # don't let player move off the screen
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH -1
        
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT
            


class MyGame(arcade.Window):
    # our custom window class
    
    def __init__(self, width, height, title):
        # call superclass init
        super().__init__(width, height, title)
        
        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        # variables for sprite lists
        self.player_sprite_list = None
        self.coin_sprite_list = None
        
      
        
        # player info
        self.player_sprite = None
        self.score = 0
        
        
        # track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        # don't show mouse cursor
        self.set_mouse_visible(False)
        
        arcade.set_background_color(arcade.color.AMAZON)
        
    def setup(self):
        # set up game, init variables
        
        #sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.coin_sprite_list = arcade.SpriteList()
        
        self.score = 0
        
        # set up player char
        self.player_sprite = arcade.Sprite("images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)
             
        # create the coins
        for i in range (COIN_COUNT):
            # create instance of coin
            coin = Coin("images/coin_01.png", SPRITE_SCALING_COIN)
            
            # position the coin randomly
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            
            # add coin to list of coins
            self.coin_sprite_list.append(coin)
        
            
    def on_draw(self):
        # draw everything
        arcade.start_render()
        #self.coin_list.draw()
        self.player_sprite_list.draw()
        self.coin_sprite_list.draw()
        
        
        # put the text on the screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14) #14 is font size
        
    def on_mouse_motion(self, x, y, dx, dy):
        # handle mouse motion
        
        # move the center of the player sprite to match the mouse x. y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
     
    def on_key_press(self, key, modifiers):
        # called whenever a key is pressed
        
        if key == arcade.key.UP:
            self.up_pressed = True
        if key == arcade.key.DOWN:
            self.down_pressed = True
        if key == arcade.key.LEFT:
            self.left_pressed = True
        if key == arcade.key.RIGHT:
            self.right_pressed = True
            
    def on_key_release(self, key, modifiers):
        # called whenever a key is released
        if key == arcade.key.UP:
            self.up_pressed = False
        if key == arcade.key.DOWN:
            self.down_pressed = False
        if key == arcade.key.LEFT:
            self.left_pressed = False
        if key == arcade.key.RIGHT:
            self.right_pressed = False
        
        
    
    
    def on_update(self, delta_time):
        # movement and game logic
        
        # calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        
        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        if self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED
        
        # call update to move the sprite 
        # if using a physics enginge, call update on it instead
        # of the sprite list.
        self.player_sprite_list.update()
        self.coin_sprite_list.update()
        
    
        
        
        # call update on all the sprites
        #self.coin_list.update()
        
        # generate list of all sprites that collided iwth the player
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, 
                                                        self.coin_sprite_list)
        
        # loop thru list of collided sprites, remove it, increment score
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
        

#----------------------end of classes-----------------------------

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()
    

 
if __name__ == "__main__":
    main()   
        
            
        
        
        
    
