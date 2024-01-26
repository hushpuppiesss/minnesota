import pygame
import sys

pygame.init()

# ----- VARIABLES -----
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
GAME_NAME = 'Minnesota'
# ----- VARIABLES -----

# creates the window
screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
# naming the window
pygame.display.set_caption(GAME_NAME)

# forcing the game to run at a set clock/fps
clock = pygame.time.Clock()

# game loop
while True:
    # input handling 
    # events include mouse clicks, keyboard clicks, etc, any form of the user
    # interacting with the software.
    for event in pygame.event.get():
        # clicking x on window closes the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # updating the display
    pygame.display.update()
    # making sure the game runs at set fps
    clock.tick(FPS)