from dataclasses import dataclass

'''
Class that represent a player
'''
@dataclass
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __repr__(self):
        s = "Player " + str(self.name) + " has " + str(self.score) + " points" +"\n"
        return s
