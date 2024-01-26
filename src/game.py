import pygame
import sys

# ----- VARIABLES -----
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
GAME_NAME = 'Minnesota'
# ---------------------

# ----- GAME CLASS -----
class Game:
    def __init__(self):
        pygame.init()
        
        # creates the window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # naming the window
        pygame.display.set_caption(GAME_NAME)

        # forcing the game to run at a set clock/fps
        self.clock = pygame.time.Clock()
        
        # loading an image
        self.img = pygame.image.load('res/player/player_downidle1.png')

# ----- RUN FUNCTION -----
    def run(self):
        while True:
            # ----- loading images -----
            self.screen.blit(self.img, (100, 200))
            
            # ----- input handling -----
            # events include mouse clicks, keyboard clicks, etc, any form of the user interacting with the software.
            for event in pygame.event.get():
                # clicking x on window closes the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # updating the display
            pygame.display.update()
            # making sure the game runs at set fps
            self.clock.tick(FPS)
            
# actually initializing the game
Game().run()