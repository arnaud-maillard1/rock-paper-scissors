import pygame
import time

"""
This class contains functions for obtaining the results 
by converting suit shapes into numbers during the analysis process :
    rock = 1
    paper = 2
    scissors = 3
    well = 10
"""
class Test:
    def __init__(self, screen, player, enemy):
        self.screen = screen
        self.player = player
        self.enemy = enemy
        # self.position = (244, 190)

    def get_result(self):
        self.check = self.player - self.enemy
        # rock vs scissors = -2 -> win
        # paper vs rock = 1 -> win
        # scissors vs paper = 1 -> win

        # rock vs paper = -1 -> lose
        # paper vs scissors = -1 -> lose
        # scissors vs rock = 2 -> lose

        # paper vs well = -8 -> win
        # well vs scissors = 7 -> win
        # well vs rock = 9 -> win

        # rock vs well = -9 -> lose
        # scissors vs well = -7 -> lose
        # well vs paper = 8 -> lose

        if self.check == 1 or self.check == -2 or self.check == 7 or self.check == 9 or self.check == -8:
            self.result = "win"
        elif self.check == 0:
            self.result = "draw"
        else:
            self.result = "lose"

        return self.result