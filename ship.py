import pygame

class ship():

    def __init__(self, screen):
        """ Initialize the ship and set it starting potition"""
        self.screen = screen
        # load the ship img and get its rect
        slef.image = pygame.image.load("img-file/space-ship-148536_640.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # start each new ship from the button from the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.botton = self.screen_rect.button


    def blitme(self):
        """Draw the current location """
        self.screen.blit(self.image, self.rect)
