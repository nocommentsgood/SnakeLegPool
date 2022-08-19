import pygame
from control import *


class Player:
    def __init__(self, control):
        self.control = control
        self.total_score = 0
        self.credits = 0
        self.shots = 3

    def blit_screen(self):
        self.control.window.blit(self.control.display, (0, 0))
        pygame.display.update()

    def add_shot(self):
        self.shots += 1

    def remove_shot(self):
        self.shots -= 1

    def add_score(self, score):
        self.total_score += score

    def add_credit(self):
        self.credits += 1

    def remove_credit(self):
        self.credits -= 1