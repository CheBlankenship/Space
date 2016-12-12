import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien")
    bg_color = (0, 0, 102)
    screen.fill(bg_color)
    ship = Ship(screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        ship.blitme()

run_game()


# import sys
# import pygame
#
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# import game_functions as gf
#
#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien")
#     bg_color = (0, 0, 102)
#     screen.fill(bg_color)
#     ship = Ship(ai_settings, screen)
#     bullets = Group()
#
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         ship.update()
#         bullets.update()
#         gf.update_screen(ai_settings, screen, ship, bullets)
#         ship.blitme()
#
# run_game()
