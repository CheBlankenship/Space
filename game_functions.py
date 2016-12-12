import sys
import pygame

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False




def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         ship.moving_right = True
        #     if event.key == pygame.K_LEFT:
        #         ship.moving_left = True
        #
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_RIGHT:
        #         ship.moving_right = False
        #     if event.key == pygame.K_LEFT:
        #         ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()






#
#
# import sys
# import pygame
# from bullet import Bullet
#
# def check_keydown_events(event, ai_settings, screen, ship, bullets):
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = True
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = True
#     elif event_key == pygame.K_space:
#         new_bullet = Bullet(ai_settings, screen, ship)
#         bullets.add(new_bullet)
#
# def check_keyup_events(event, ship):
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = False
#
#
#
#
# def check_events(ship, ai_settings, screen, bullets):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             # check_keydown_events(event, ship)
#             check_keydown_events(event, ai_settings, screen, ship, bullets)
#
#         elif event.type == pygame.KEYUP:
#             check_keyup_events(event, ship)
#         # elif event.type == pygame.KEYDOWN:
#         #     if event.key == pygame.K_RIGHT:
#         #         ship.moving_right = True
#         #     if event.key == pygame.K_LEFT:
#         #         ship.moving_left = True
#         #
#         # elif event.type == pygame.KEYUP:
#         #     if event.key == pygame.K_RIGHT:
#         #         ship.moving_right = False
#         #     if event.key == pygame.K_LEFT:
#         #         ship.moving_left = False
#
#
# def update_screen(ai_settings, screen, ship, bullets):
#     screen.fill(ai_settings.bg_color)
#     for bullet in bullets.sprites():
#         bullet.draw_bullet()
#     ship.blitme()
#
#     pygame.display.flip()
