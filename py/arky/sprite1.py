# trying to port my crappy breaky to pyarcade

import random
import arcade
import os

#-----constants
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50


SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
SCREEN_TITLE = "sprite coin 1"

class MyGame(arcade.Window):
    # our custom window class
    
    def __init__(self):
        # call superclass init
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        # variables for sprite lists
        self.player_list = None
        self.coin_list = None
        
        # player info
        self.player_sprite = None
        self.score = 0
        
        # don't show mouse cursor
        self.set_mouse_visible(False)
        
        arcade.set_background_color(arcade.color.AMAZON)
        
    def setup(self):
        # set up game, init variables
        
        #sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        
        self.score = 0
        
        # set up player char
        self.player_sprite = arcade.Sprite("images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        
        # create the coins
        for i in range (COIN_COUNT):
            # create instance of coin
            coin = arcade.Sprite("images/coin_01.png", SPRITE_SCALING_COIN)
            
            # position the coin randomly
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            
            # add coin to list of coins
            self.coin_list.append(coin)
            
    def on_draw(self):
        # draw everything
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        
        # put the text on the screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14) #14 is font size
        
    def on_mouse_motion(self, x, y, dx, dy):
        # handle mouse motion
        
        # move the center of the player sprite to match the mouse x. y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        
    def on_update(self, delta_time):
        # movement and game logic
        
        # call update on all the sprites
        self.coin_list.update()
        
        # generate list of all sprites that collided iwth the player
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        
        # loop thru list of collided sprites, remove it, increment score
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


#----------------------end of classes-----------------------------

def main():
    window = MyGame()
    window.setup()
    arcade.run()
    

 
if __name__ == "__main__":
    main()   
        
            
        
        
        
    
