import pygame
import random


# import pygame.locals for easy access to key coords
# updated to conform to flake8 and black standards

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

pygame.init()

# Define a player object that extends pygame.sprite.Sprite
# the surface dwarn on the screen is now an attr of Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        #self.surf = pygame.Surface((75, 25))
        #self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

    # move the sprite based on user keypresses
    # move_ip means move in place
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        #self.surf = pygame.Surface((20,10))
        #self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center = (
                #random.randint(0,SCREEN_WIDTH),
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0,SCREEN_HEIGHT),
            )

        )
        self.speed = random.randint(5,20)

        #print("created enemy")

    # move the sprite based on speed
    # remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Define the cloud object by extending pygame.sprite.Sprite

# Use an image for a better-looking sprite


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

    


# set up a clock for a sane frame rate
clock = pygame.time.Clock()


# constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)  # fire the ADDENEMY event every 250ms
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000) # 1000ms 1s

# create instance of player
player = Player()

# create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


running = True

# main game loop
while running:
    # look at every event in Q
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # was it escape? if so quit
            if event.key == K_ESCAPE:
                running = False
        
        elif event.type == QUIT:
            running = False
    
        # add a new enemy?  check for ADDENEMY
        elif event.type == ADDENEMY:
            #print('got ADDENEMY event')
            # create new enemy and add it to the sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        
        # add a new cloud?
        elif event.type == ADDCLOUD:
            # create new cloud and add to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)


    
    # process keyboard input
    pressed_keys = pygame.key.get_pressed()

    # update player sprite based on user keypresses
    player.update(pressed_keys)

    # update enemy position
    enemies.update()
    clouds.update()

    # draw stuff on screen

    # fill screen w blue
    screen.fill((135,206,250))


    # draw all sprites
    for entity in all_sprites:
        #print(entity)
        screen.blit(entity.surf, entity.rect)
    
    # check to see if any enemies have collided with the player
    if pygame.sprite.pygame.sprite.spritecollideany(player, enemies):
        # if yes, remove player and stop loop
        player.kill()
        running = False

    
    
    # when you pass a rect to blit() it uses the top left corner to draw the surf (okaaaay)
 
    # updates screen with everything since last flip
    pygame.display.flip()

    # make sure we get 30 fps
    clock.tick(30)




