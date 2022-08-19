import pygame
import json
import string
from control import *
from game import *

class Highscore:
    def __init__(self, control):
        self.control = control
        self.player_name = ''
        self.scores_dict = self.read_file()
        alphabet_string = string.ascii_uppercase
        self.alphabet_list = list(alphabet_string)
        self.list_index = 0

    def blit_screen(self):
        self.control.window.blit(self.control.display, (0, 0))
        pygame.display.update()


    def read_file(self):
        with open("highscores.txt") as f:
            file_data = f.read()

        js = json.loads(file_data)
        return js

    def write_file(self, new_dict):
        with open("highscores.txt", 'w') as convert_file:
            convert_file.write(json.dumps(new_dict))

    def display_dict(self):
        x = 300
        for key, value in self.scores_dict.items():
            self.control.draw_text(key, TEXT_FONT, 150, 540, x)
            self.control.draw_text("...................", TEXT_FONT, 150, 925, x)
            self.control.draw_text(str(value), TEXT_FONT, 150, 1350, x)
            x+=150

    def check_new_highscore(self, player_score):
        for score in self.scores_dict.values():
            if player_score > score:
                return True

    def enter_name(self):    
        if len(self.player_name) < 3: 
            pygame.Surface.blit(self.control.display, BACKGROUND, (0,0)) 
            self.control.draw_text("Nice Shooting!", TEXT_FONT, 150, WIDTH/2, 100)
            self.control.draw_text("You got a new highscore!", TEXT_FONT, 150, WIDTH/2, 300)  
            self.control.draw_text("Enter your initials: " + self.player_name + self.alphabet_list[self.list_index], TEXT_FONT, 100, WIDTH/2, 500)
            self.check_input()
            self.blit_screen()
            self.control.reset_keys()
        else:
            self.update_score()
            self.control.game.game_reset()
            self.self_reset()
 


    def check_input(self):
        if self.control.right_bt:
            self.list_index += 1
        if self.control.left_bt:
            self.list_index -= 1
        if self.control.enter_bt:
            self.player_name = self.player_name + self.alphabet_list[self.list_index]
            self.blit_screen()

    def update_score(self):
        min_key = min(self.scores_dict, key=self.scores_dict.get)
        self.scores_dict[self.player_name] = self.scores_dict.pop(min_key)
        self.scores_dict[self.player_name] = self.control.player.total_score
        sorted_dict = sorted(self.scores_dict.items(), key=lambda x: x[1],reverse=True)
        self.write_file(sorted_dict)


    def self_reset(self):
        self.player_name = ''
        self.list_index = 0