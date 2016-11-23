import sys

import pygame

# Gets the class values from setting.py
from settings import Settings

def run_game():
    # Initialize game and creat a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode ((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invation")
    # Set the back ground color

    # Start the main loop for the game
    while True:
        # Mach for keybord and mouse events
        screen.fill(ai_settings.bg_color)
        # While it'S True it updates the page color
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    # Make the most recently screen visible.

run_game()
