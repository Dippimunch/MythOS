import random
import numpy as np



class Team:
    def __init__(self, size, roster=[]):
        self.size = size
        self.roster = roster 

    def make_team(self):
        for i in range(self.size):
            self.roster.append(i+1)
class Entity:
    def __init__(self, attack, defense, health, energy):
        self.attack = attack
        self.defense = defense
        self.health = health
        self.energy = energy
