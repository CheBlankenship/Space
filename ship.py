import pygame

class Ship():
    def __init__(self, screen):
        """ Initialize the ship and set it starting potition"""
        self.screen = screen
        # load the ship img and get its rect
        self.image = pygame.image.load("img-file/small-ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # start each new ship from the buttom from the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Movement flag
        # self.moving_right = True
        # self.moving_left = True

    def update(self):
        """Update the ships position"""
        if self.moving_right == True:
            self.rect.centerx += 1
        if self.moving_left == True:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the current location """
        self.screen.blit(self.image, self.rect)
