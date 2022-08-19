import pygame


WIDTH = 1920
HEIGHT = 1080
PLACE = 225
FPS = 60

PINK = (255,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (11, 252, 3)
ORANGE = (252, 161, 3)

BACKGROUND = pygame.image.load("imgs/bg.png")

LOGO = pygame.image.load("imgs/logo.png")

SEMO = pygame.image.load("imgs/semo.png")
SEMO = pygame.transform.scale(SEMO, (350,350))

LOGO = pygame.transform.scale(LOGO, (1024,422))

RIGHT_ARROW = pygame.image.load("imgs/arrow.png")
RIGHT_ARROW = pygame.transform.scale(RIGHT_ARROW, (200,200))
RIGHT_ARROW.set_colorkey(WHITE)
LEFT_ARROW = pygame.transform.flip(RIGHT_ARROW, True, False)

TRACK = pygame.image.load("imgs/SnakeTrack.png")
TRACK = pygame.transform.scale(TRACK, (130, 800))
TRACK.set_colorkey(WHITE)

TITLE_FONT = "fonts/DancingScript-Regular.otf"
TEXT_FONT = "fonts/BebasNeue-Regular.otf"
