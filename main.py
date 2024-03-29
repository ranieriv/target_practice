#pygame
import sys
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from target import Target
from shooter import Shooter
from bullet import Bullet
from math import ceil as round_up

class TargetPractice(pygame.sprite.Sprite):
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        # Create the display and the Caption
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")
        
        # set the game time and stats
        self.stats = GameStats(self)
        self.clock = pygame.time.Clock()
        
        # Create the instances of the other objects
        self.target = Target(self)
        self.shooter = Shooter(self)
        self.bullets = pygame.sprite.Group()
        
        # Make the play button
        self.play_button = Button(self, "Play")
        
    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            # frame_rate = self.clock.get_fps() # get the framerate
            
            # Check events in the game
            self._check_events()
            if self.stats.game_active:
                # Updates of the objects
                self.target.update()
                self.shooter.update()
                self._update_bullets()
                
            self._update_screen()
            
            # Game fps
            self.clock.tick(self.settings.framerate)
    
    def _check_events(self):
        """ Respond to keypresses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Check keydown and keyup events
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)     
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
            # Check mouse buttons and position
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.shooter.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.shooter.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:    
            self.shooter.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.shooter.moving_left = False
            
    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group. """  
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def _check_play_button(self, mouse_pos):
        """ Start a new game when the player clicks Play. """
        if self.play_button.rect.collidepoint(mouse_pos):
            # Reset the game statistics.
            self.stats.reset_status()
            self.stats.game_active = True
            self.shooter.center_shooter()
            self.bullets.empty()
            self.settings.initialize_dynamic_settings()
            
    def _update_bullets(self):
        """ Update the position of the bullets and get rid of old bullets. """
        # Update bullet positions
        self.bullets.update()
        
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                print("Bullet lost")
                if self.settings.bullets_missed_limit > 0:
                    self.settings.bullets_missed_limit -= 1
                    print(f' Bullets left: {self.settings.bullets_missed_limit}')
                else:
                    self._game_over()
        
        self._check_bullet_target_collisions()
        
    def _check_bullet_target_collisions(self):
        for bullet in self.bullets:
            
            if bullet.rect.colliderect(self.target):
                print("Target Hit")
                self.bullets.remove(bullet)
                self.stats.score += 1
                print(f"Score: {self.stats.score}")
                self.settings.increase_speed()

            
    
    def _game_over(self):
        self.stats.game_active = False
        print(f"{10 * '#'} Game Over {10 * '#'}")
        print(f"{10 * '#'} Total Score: {self.stats.score} {10 * '#'}")
                    
    def _update_screen(self):
        """ Update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)  
        self.target.blitme()
        self.shooter.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
            
        pygame.display.flip()
        
    
    
    
if __name__ == '__main__':
    tp = TargetPractice()
    tp.run_game()