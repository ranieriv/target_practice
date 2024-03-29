import pygame
from settings import Settings
from pygame.sprite import Sprite
from random import randint

class Target(Sprite):
    """ A class to manage the target"""
    
    def __init__(self, tp_game):
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        
        # Load the rect
        self.surf = pygame.Surface((150, 20))
        self.surf.fill(self.settings.target_color)
        self.rect = self.surf.get_rect()
        self.rect.x = self.rect.width
        self.x = float(self.rect.x)
        
    def blitme(self):
        """ Draw the target at the current location"""
        self.screen.blit(self.surf, self.rect)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        
    def update(self):
        """ Move the target to left and right"""
        if self.check_edges():
            self.settings.target_direction *= -1
        self.x += (self.settings.target_speed * self.settings.target_direction)
        self.rect.x = self.x
        