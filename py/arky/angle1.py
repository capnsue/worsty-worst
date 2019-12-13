import arcade
import os
import math


#-----constants
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN= 0.2
SPRITE_SCALING = 0.5
#COIN_COUNT = 50

MOVEMENT_SPEED = 5
ANGLE_SPEED = 5

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
SCREEN_TITLE = "move sprite by angle test"


#-------------------------------------------
#
#               classes
#
#--------------------------------------------

class Player(arcade.Sprite):
    def __init__(self, image, scale):
        
        super().__init__(image, scale)        
        self.speed = 0
        
    def update(self):
        # convert angle in degrees to radians
        # the angle comes from the parent class (sprite)
        angle_rad = math.radians(self.angle)
        
        # rotate the ship
        self.angle += self.change_angle   # wtf is change_angle
        
        # use MAAATH to find change based on our speed andn angle
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)
        
        # TODO: figure out wtf this angle shit means
        
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # constructor
        
        # call parent constructor
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)
        
    def setup(self):
        # set up game and init variables
        
        # sprite lists
        self.player_list = arcade.SpriteList()
        
        # set up player
        self.player_sprite = Player("images/playerShip1_orange.png", SPRITE_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)  
    
    def on_draw(self):
        # render the screen
        
        # this always has to happen first
        arcade.start_render()
        
        # draw all the sprites
        self.player_list.draw()
        
    def on_update(self, delta_time):
        # movement and game logiv
        
        # call update on all sprites
        self.player_list.update()
        
    def on_key_press(self, key, modifiers):

        # Forward/back
        if key == arcade.key.UP:
            self.player_sprite.speed = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.speed = -MOVEMENT_SPEED

        # Rotate left/right
        elif key == arcade.key.LEFT:
            self.player_sprite.change_angle = ANGLE_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_angle = -ANGLE_SPEED
    
    def on_key_release(self, key, modifiers):
        
        # if they let go of up or down, bring speed to 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.speed = 0
        
        # if they let go of L or R stop changing the angle
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0
        
        
################################################################
#   end of classes
################################################################

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
    
        
        
        
        