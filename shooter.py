import pygame

class Shooter:
    
    def __init__(self, tp_game):
        """ A class to manage the shooter. """
        
        self.screen = tp_game.screen
        self.settings = tp_game.settings 
        self.screen_rect = tp_game.screen.get_rect()
        
        # Load the rect
        self.surf = pygame.Surface((50,50))
        self.surf.fill(self.settings.shooter_color)
        self.rect = self.surf.get_rect()        
        
        # Start the shooter at the center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a decimal value for the shooter's horizontal position.
        self.x = float(self.rect.x)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """ Update the shooters position based on the movement flags."""
        #Update the shooter's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.shooter_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.shooter_speed
            
        self.rect.x = self.x
        
    def blitme(self):
        """ Draw the shooter at its current location. """
        self.screen.blit(self.surf, self.rect)
        
    def center_shooter(self):
        """ Center the shooter on the screen. """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        