import pygame
from control import *
from game import *

class Animate:
    def __init__(self, control):
        self.control = control
        self.x = 50
        self.edge = 2300
        self.speed = 5
        self.score_sound = pygame.mixer.Sound("sounds/score_sound.wav")
        
        
    def blit_screen(self):
        self.control.window.blit(self.control.display, (0, 0))
        pygame.display.update()

    def reset(self):
        self.x = 50

class AnimateHoleOne(Animate):
    def __init__(self, control):
        Animate.__init__(self, control)

    def play_animation(self):
        self.control.check_events()
        pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))
        self.control.draw_text('1000 POINTS!', TEXT_FONT, 300, self.x, HEIGHT/2)
        self.blit_screen()
        self.x += self.speed
        if self.x > self.edge:
            self.control.game.main_game_display = True
            self.control.game.game_animation = False
        self.control.reset_keys()

class AnimateHoleTwo(Animate):
    def __init__(self, control):
        Animate.__init__(self, control)

    def play_animation(self):
        self.control.check_events()
        pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))
        self.control.draw_text('2000 POINTS!', TEXT_FONT, 300, self.x, HEIGHT/2)
        self.blit_screen()
        
        self.x += self.speed
        if self.x > self.edge:
            self.control.game.main_game_display = True
            self.control.game.game_animation = False
        self.control.reset_keys()

class AnimateHoleThree(Animate):
    def __init__(self, control):
        Animate.__init__(self, control)

    def play_animation(self):
        self.control.check_events()
        pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))
        self.control.draw_text('3000 POINTS!', TEXT_FONT, 300, self.x, HEIGHT/2)
        self.blit_screen()
        
        self.x += self.speed
        if self.x > self.edge:
            self.control.game.main_game_display = True
            self.control.game.game_animation = False
        self.control.reset_keys()

class AnimateHoleFour(Animate):
    def __init__(self, control):
        Animate.__init__(self, control)

    def play_animation(self):
        self.control.check_events()
        pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))
        self.control.draw_text('4000 POINTS!', TEXT_FONT, 300, self.x, HEIGHT/2)
        self.blit_screen()
        
        self.x += self.speed
        if self.x > self.edge:
            self.control.game.main_game_display = True
            self.control.game.game_animation = False
        self.control.reset_keys()

class AnimateHoleFive(Animate):
    def __init__(self, control):
        Animate.__init__(self, control)

    def play_animation(self):
        self.control.check_events()
        pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))
        self.control.draw_text('5000 POINTS!', TEXT_FONT, 300, self.x, HEIGHT/2)
        self.blit_screen()
        
        self.x += self.speed
        if self.x > self.edge:
            self.control.game.main_game_display = True
            self.control.game.game_animation = False
        self.control.reset_keys()

class AnimateHoleSix(Animate):
    def __init__(self, control):
        Animate.__init__(self, control)

    def play_animation(self):
        self.control.check_events()
        pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))
        self.control.draw_text('10000 POINTS!', TEXT_FONT, 300, self.x, HEIGHT/2)
        self.control.draw_text('Snake in a Boot!', TEXT_FONT, 300, self.x, 200)
        self.blit_screen()
        
        self.x += self.speed
        if self.x > self.edge:
            self.control.game.main_game_display = True
            self.control.game.game_animation = False
        self.control.reset_keys()
