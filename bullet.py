import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage the bullets fired from the shooter """
    def __init__(self, tp_game):
        super().__init__()  
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = (self.settings.bullet_color)
        
        # Create a bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = tp_game.shooter.rect.midtop
        
        # Store the bullets position at a decimal value
        self.y = float(self.rect.y)
        
    def update(self):
        """ Move the bullets up the screen. """
        self.y -= self.settings.bullet_speed
        
        # Update the rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """ Draw the bullet to the screen. """
        pygame.draw.rect(self.screen, self.color, self.rect)
        