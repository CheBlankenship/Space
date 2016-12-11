import pygame

class Ship():
    def __init__(self, screen, ai_settings):
        """ Initialize the ship and set it starting potition"""
        self.screen = screen
        self.ai_settings = ai_settings
        # load the ship img and get its rect
        self.image = pygame.image.load("img-file/small-ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # start each new ship from the buttom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center


    def blitme(self):
        """Draw the current location """
        self.screen.blit(self.image, self.rect)
