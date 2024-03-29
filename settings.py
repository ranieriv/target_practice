class Settings:
    """ To store all settings for the game"""
    
    def __init__(self):
        
    # Screen Settings
        self.screen_width  = 1200
        self.screen_height = 800
        self.bg_color = (100, 150, 200)
        
    # Time Settings
        self.framerate = 60
        
    # Target Settings
        self.target_color =(0,0,0)
        
    # Shooter settings
        self.shooter_color = (25,25,25)
        
    # Bullet settings
        self.bullet_color = (0, 0, 0)
        self.bullet_height = 60
        self.bullet_width = 3
        self.bullets_missed_limit = 6
        
    # How quick the game speeds up
        self.speed_up_scale = 1.2       
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game."""
        self.shooter_speed = 15
        self.target_speed = 5
        self.bullet_speed = 25

        # Targets direction of 1 represents right. -1 represents left.
        self.target_direction = 1
        
    def increase_speed(self):
        self.shooter_speed  *= self.speed_up_scale
        self.target_speed *= self.speed_up_scale
        self.bullet_speed  *= self.speed_up_scale
        print(f"New Shooter Speed {self.shooter_speed}")
        print(f"New Target Speed {self.target_speed}")
        print(f"New Bullet Speed {self.bullet_speed}")