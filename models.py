'''
Data models for Albion Insight.
'''

class Player:
    '''Represents a player in the game.'''
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name
        self.damage_done = 0
        self.healing_done = 0

    def __repr__(self):
        return f"Player(id={self.player_id}, name='{self.name}', damage={self.damage_done}, healing={self.healing_done})"
