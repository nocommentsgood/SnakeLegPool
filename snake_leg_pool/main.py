import pygame
from control import Control
from constants import WIDTH, HEIGHT

pygame.display.set_caption('SNAKE LEG!')
snake = Control()

snake.run()
    

pygame.Surface.blit(self.control.display, BACKGROUND, (0,0))