import pygame
import json
from control import *


class Menu:
    def __init__(self, control):
        self.control = control
        self.run_display = True
				
        
    def blit_screen(self):
        self.control.window.blit(self.control.display, (0, 0))
        pygame.display.update()


class MainMenu(Menu):
    def __init__(self, control):
        Menu.__init__(self, control)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.control.check_events()
            pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))			
            self.control.draw_text("Snake Leg Pool",TITLE_FONT, 200, WIDTH/2, HEIGHT/4)
            pygame.Surface.blit(self.control.display, LOGO, (400,400)) 
            pygame.Surface.blit(self.control.display, RIGHT_ARROW, (1700,540))
            self.control.draw_text("To How To Play", TEXT_FONT, 40, 1600, 635) 
            pygame.Surface.blit(self.control.display, LEFT_ARROW, (0,520)) 
            self.control.draw_text("To High Scores", TEXT_FONT, 40, 275, 620) 
            self.control.draw_text("Credits: " + str(self.control.player.credits),TEXT_FONT, 40, WIDTH/2, 1000)
            self.check_input()
            self.blit_screen()
            self.control.reset_keys()

    def check_input(self):
        if self.control.right_bt:
            self.control.curr_menu = self.control.rules_menu
        elif self.control.left_bt:
            self.control.curr_menu = self.control.highscore_menu
        self.run_display = False

class RulesMenu(Menu):
    def __init__(self, control):
        Menu.__init__(self, control)


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.control.check_events()
            self.check_input()
            pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))
            pygame.Surface.blit(self.control.display, TRACK, (850,200))
            
            self.control.draw_text("How To Play",TITLE_FONT,  200, WIDTH/2, 100)
            pygame.draw.rect(self.control.display,WHITE,(550,210,175,75)) 
            pygame.draw.line(self.control.display,WHITE, (550, 240), (860, 240))
            self.control.draw_text("10,000",TEXT_FONT,  75, 635, 250)     
            pygame.draw.rect(self.control.display,WHITE,(1075,310,175,75)) 
            pygame.draw.line(self.control.display,WHITE, (930, 350), (1150, 350))
            self.control.draw_text("5,000",TEXT_FONT,  75, 1160, 350)
            pygame.draw.rect(self.control.display,WHITE,(550,410,175,75)) 
            pygame.draw.line(self.control.display,WHITE, (550, 445), (875, 445))
            self.control.draw_text("4,000",TEXT_FONT,  75, 635, 450)
            pygame.draw.rect(self.control.display,WHITE,(1075,510,175,75)) 
            pygame.draw.line(self.control.display,WHITE, (930, 550), (1150, 550))
            self.control.draw_text("3,000",TEXT_FONT,  75, 1160, 550)
            pygame.draw.rect(self.control.display,WHITE,(550,610,175,75)) 
            pygame.draw.line(self.control.display,WHITE, (550, 645), (875, 645))
            self.control.draw_text("2,000",TEXT_FONT,  75, 635, 650)
            pygame.draw.line(self.control.display,WHITE, (930, 750), (1150, 750))
            pygame.draw.rect(self.control.display,WHITE,(1075,710,175,75)) 
            self.control.draw_text("1,000",TEXT_FONT,  75, 1160, 750)
           

            self.control.draw_text("*Shoot the cue ball into the 8-ball and send it down the snake track",TEXT_FONT,  30, 400, 800)
            self.control.draw_text("*The further the shot the more points are rewarded, simple!",TEXT_FONT,  30, 360, 850)
            self.control.draw_text("*Players are given three shots with bonus shots if you can sink ",TEXT_FONT,  30, 375, 900)
            self.control.draw_text("3 snakes in a boot in a row (10,000 points). ",TEXT_FONT,  30, 280, 950)
            
            
            self.blit_screen()
            self.control.reset_keys()

    def check_input(self):
        if self.control.left_bt:
            self.run_display = False
            self.control.curr_menu = self.control.main_menu

class HighScoreMenu(Menu):
    def __init__(self, control):
        Menu.__init__(self, control)
        


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.control.check_events()
            self.check_input()
            pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))
            self.control.draw_text("High Scores",TITLE_FONT,  200, WIDTH/2, 100)
            self.control.highscore.display_dict()
            self.blit_screen()
            self.control.reset_keys()

    def check_input(self):
        if self.control.right_bt:
            self.control.curr_menu = self.control.main_menu
        self.run_display = False


