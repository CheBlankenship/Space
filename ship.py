import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        # self.ai_settings = ai_settings
        self.image = pygame.image.load("img-file/small-ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            # if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.rect.centerx > 1170:
                self.moving_right = False
            else:
                self.rect.centerx +=3
                # self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left:
            # if self.moving_left and self.rect.left > 0:
            if self.rect.centerx < 30:
                self.moving_left = False
            else:
                self.rect.centerx -=3
                # self.centerx -= self.ai_settings.ship_speed_factor

        # self.rect.centerx = self.centerx

    def blitme(self):
        """Draw the current location """
        self.screen.blit(self.image, self.rect)
