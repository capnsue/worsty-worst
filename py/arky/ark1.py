# actually gonna try to build breakout in steps
# step 1: set up window and draw blocks to kill

import arcade
import os

#----- constants ------#

COLUMN_SPACING = 50
ROW_SPACING = 50
LEFT_MARGIN = 30
BOTTOM_MARGIN = 300

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_TITLE = "ark1"





class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        self.block_list = None
        self.ball_list = None

        # Set up the player info
        self.player_sprite = None
        self.ball_sprite = None

        # Set up sprite that will serve as trigger
        #self.trigger_sprite = None

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)
        
    def setup(self):
        
        # draw blocks
        
        self.block_list = arcade.SpriteList()
        
        blocks_rows = 5
        blocks_cols = (SCREEN_WIDTH // COLUMN_SPACING)
        
        for row in range(0, blocks_rows):
            for column in range(0, blocks_cols):
            
                # calculate location of block
                x = column * COLUMN_SPACING + LEFT_MARGIN
                y = row * ROW_SPACING + BOTTOM_MARGIN
                
                block = arcade.Sprite("images/boxCrate_double.png",
                                      scale=0.25, center_x=x, center_y=y)
                #block = arcade.Sprite("images/coin_01.png", 
                                      
                self.block_list.append(block)
    
    def on_draw(self):
        arcade.start_render()
        
        self.block_list.draw()
#--------------------------------------------------------------------------------

        
def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
        
         

        
        
        
        
