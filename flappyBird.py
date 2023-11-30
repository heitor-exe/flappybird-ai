import pygame
import os
import random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800

IMG_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','pipe.png')))
IMG_BASE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','base.png')))
IMG_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bg.png')))
IMGS_BIRD = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird3.png')))
]

pygame.font.init()
SCORE_FONT = pygame.font.SysFont('Flappy Bird Font', 50)

class Bird:
    IMGS = IMGS_BIRD

    # Rotations animation
    MAX_ROTATION = 25
    ROTATION_SPEED = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.angle = 0
        self.speed = 0
        self.height = self.y

        self.time = 0
        self.img_count = 0
        self.img = IMGS[0]

    def jump(self):
        self.speed = -10.5
        self.time = 0
        self.height = self.y

    def move(self):

        # Calculating distance

        # Restricting distance

        
        # Bird angle




class Pipe:
    pass

class Base:
    pass
