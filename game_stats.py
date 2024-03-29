class GameStats:
    """ Tracks statistics for Target Practice"""
    
    def __init__(self, tp_game):
        """ initialize Statistics. """
        self.settings = tp_game.settings
        self.reset_status()
        
        # Start the game in an inactive mode
        self.game_active = False
        self.score = 0
        
    def reset_status(self):
        """ Initialize statistics that can change during the game"""
        self.settings.bullets_missed_limit = 6
        self.score = 0