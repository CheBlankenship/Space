import pygame

class Ship():
    def __init__(self, screen):
        """ Initialize the ship and set it starting potition"""
        self.screen = screen
        # load the ship img and get its rect
        # self.image = pygame.image.load("img-file/space-ship-148536_640.png")
        self.image = pygame.image.load("img-file/small-ship.png")
        # self.image_size = self.image.
        # self.image_height = 70
        # self.image_width = 50
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # start each new ship from the buttom from the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """Draw the current location """
        self.screen.blit(self.image, self.rect)
