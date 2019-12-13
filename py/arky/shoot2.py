# trying to port my crappy breaky to pyarcade

# better keyboard movement
# and now the coins move
# and now you can shoot at them !!!!
# and now maybe you can shoot at an angle!


import random
import arcade
import os
import math


#-----constants
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN= 0.2
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 50

MOVEMENT_SPEED = 5

BULLET_SPEED = 5


SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
SCREEN_TITLE = "coin gettin shot"




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
"""            
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
            """         


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
        self.bullet_sprite_list = None
            
      
        
        # player info
        self.player_sprite = None
        self.score = 0
        self.score_text = None
        
        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.sound.load_sound("sounds/laser1.wav")
        self.hit_sound = arcade.sound.load_sound("sounds/phaseJump1.wav")
        
        
        
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
        self.bullet_sprite_list = arcade.SpriteList()
        
        
        self.score = 0
        
        # set up player char
        self.player_sprite = arcade.Sprite("images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_sprite_list.append(self.player_sprite)
             
        # create the coins
        for i in range (COIN_COUNT):
            # create instance of coin
            coin = Coin("images/coin_01.png", SPRITE_SCALING_COIN)
            
            # position the coin randomly
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(120, SCREEN_HEIGHT)
            
            # add coin to list of coins
            self.coin_sprite_list.append(coin)
        
            
    def on_draw(self):
        # draw everything
        arcade.start_render()
        #self.coin_list.draw()
        self.player_sprite_list.draw()
        self.coin_sprite_list.draw()
        self.bullet_sprite_list.draw()
        
        
        
        # put the text on the screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14) #14 is font size
        
    def on_mouse_press(self, x, y, button, modifiers):
        # SHOOOOOOOOOT
        """
        Called whenever the mouse button is clicked.
        """
        # Gunshot sound
        arcade.sound.play_sound(self.gun_sound)
        # Create a bullet
        bullet = arcade.Sprite("images/laserBlue01.png", SPRITE_SCALING_LASER)
        
        # position the bullet at the player's current location
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y
        
        # get the destination for the bullet from the mouse
        # important! if you have a scrolling screen,
        # you will also need to add in self.view_bottom
        # and self.view_left
        dest_x = x
        dest_y = y
        
        # DO MATH to calculate how to get the bullet to the destination
        # calculate the angle in radians between start coords 
        # and end coords.  this is the angle the bullet needs to travel
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        
        """
        # The image points to the right, and we want it to point up. So
        # rotate it.
        bullet.angle = 90
        """
        
        # angle the bullet sprite so it doesn't liik like 
        # it is flying sideways
        bullet.angle = math.degrees(angle)
        print(f"bullet angle: {bullet.angle:.2f}")
        # (we just figured out angle above remember)
        
        
        # taking into account the angle, calculate 
        # change_x and change_y.  velocity = how fast
        # bullet travels
        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED
    
        
        # Give the bullet a speed
        #bullet.change_y = BULLET_SPEED

        # Position the bullet


        # Add the bullet to the appropriate lists
        self.bullet_sprite_list.append(bullet)

    
    def on_mouse_motion(self, x, y, dx, dy):
        # handle mouse motion
        
        # move the center of the player sprite to match the mouse x. y
        self.player_sprite.center_x = x
        #self.player_sprite.center_y = y
   
  
    
    
    def on_update(self, delta_time):
        # movement and game logic
        
        self.bullet_sprite_list.update()
        
        # check to see if bullets hit anything
        for bullet in self.bullet_sprite_list:    
            # check to see if we hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_sprite_list)
            
            # if it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                
            # for each coin we hit, add to the score and remove the coin
            for coin in hit_list: 
                coin.remove_from_sprite_lists()
                self.score += 1
                
                # play hit sound!!!!!
                arcade.play_sound(self.hit_sound)
            
            # if the bullet flies off-screen, remove it
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
                
        
        
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
        
            
        
        
        
    
