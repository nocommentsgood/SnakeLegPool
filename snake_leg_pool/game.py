import pygame
from control import *
from player import *
from animate import *
from constants import *

class Game:
    def __init__(self, control):
        self.control = control
        self.game_animation = False
        self.end_game_display = False
        self.scored = ''              

    def blit_screen(self):
        self.control.window.blit(self.control.display, (0, 0))
        pygame.display.update()


class MainDisplay(Game):
    def __init__(self, control):
        Game.__init__(self, control)
        
    def display_main_screen(self):
        if self.control.player.shots == 0:
            self.end_game_display = True
            self.main_game_display = False
        self.control.holeOne.reset()
        self.control.holeTwo.reset()
        self.control.holeThree.reset()
        self.control.holeFour.reset()
        self.control.holeFive.reset()
        self.control.holeSix.reset()



        
        self.control.check_events()
        pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))
        
        pygame.Surface.blit(self.control.display, TRACK, (850,200))
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
        pygame.Surface.blit(self.control.display, SEMO, (1450,50))
        pygame.draw.rect(self.control.display,WHITE,(1450,650,400,400))
        self.control.draw_text("advertisement",TEXT_FONT,  75, 1650, 800) 
        self.control.draw_text("Score: ",TEXT_FONT, 100, 150, 100)
        self.control.draw_text(str(self.control.player.total_score),TEXT_FONT, 100, 350, 100)
        self.control.draw_text("Shots Left: " + str(self.control.player.shots), TEXT_FONT, 100, 250, 1000)
        
        self.check_input()
        self.blit_screen()
        self.control.reset_keys()

    def hole_animations(self):
        if self.scored == 'one':
            self.control.holeOne.play_animation()
        if self.scored == 'two':
            self.control.holeTwo.play_animation()
        if self.scored == 'three':
            self.control.holeThree.play_animation()
        if self.scored == 'four':
            self.control.holeFour.play_animation()
        if self.scored == 'five':
            self.control.holeFive.play_animation()
        if self.scored == 'six':
            self.control.holeSix.play_animation()

    def check_input(self):
        if self.control.hole1_sensor:
            self.control.player.remove_shot()
            self.control.player.add_score(1000)         
            self.main_game_display = False
            self.game_animation = True
            self.scored = 'one'
        
        if self.control.hole2_sensor:
            self.control.player.remove_shot()
            self.control.player.add_score(2000)          
            self.main_game_display = False
            self.game_animation = True
            self.scored = 'two'
        
        if self.control.hole3_sensor:
            self.control.player.remove_shot()
            self.control.player.add_score(3000)
            self.main_game_display = False
            self.game_animation = True
            self.scored = 'three'
        
        if self.control.hole4_sensor:
            self.control.player.remove_shot()
            self.control.player.add_score(4000)
            self.main_game_display = False
            self.game_animation = True
            self.scored = 'four'
        
        if self.control.hole5_sensor:
            self.control.player.remove_shot()
            self.control.player.add_score(5000)
            self.main_game_display = False
            self.game_animation = True
            self.scored = 'five'
       
        if self.control.hole6_sensor:
            self.control.player.remove_shot()
            self.control.player.add_score(10000)
            self.main_game_display = False
            self.game_animation = True
            self.scored = 'six'

    def display_end_screen(self):
        if self.control.highscore.check_new_highscore(self.control.player.total_score):          
            self.control.highscore.enter_name()
            self.blit_screen()
            self.control.reset_keys() 
            self.control.check_events()
        else:
            pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))    
            self.control.draw_text("Game Over", TITLE_FONT,200, WIDTH/2, 100)
            self.control.draw_text("You scored:", TEXT_FONT,200, WIDTH/2, 400)
            self.control.draw_text(str(self.control.player.total_score) + " Points" ,TEXT_FONT, 200, WIDTH/2, 600)
            self.blit_screen()       
            self.control.reset_keys()       
            pygame.time.wait(5000)
            self.game_reset()

    def game_reset(self):       
        self.control.player.total_score = 0
        self.control.player.shots = 3
        self.control.playing = False
        self.end_game_display = False
