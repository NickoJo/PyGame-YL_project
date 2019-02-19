import pygame
import sys
from pygame.locals import *

# нужные данные

width = 650
height = 480

gray = (100, 100, 100)
white = (255, 255, 255)
red = (255, 0, 0)
green = (102, 255, 153)
blue = (102, 102, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
purple = (255, 0, 255)
black = (0, 0, 0)

background = black
blockgap = 2
blockwidth = 62
blockheight = 25
arraywidth = 10
arrayheight = 5
paddlewidth = 100
paddleheight = 10
ballradius = 20
ballcolour = white
block = 'block'
ball = 'ball'
paddle = 'paddle'
ballspeed = 1


class Block(pygame.sprite.Sprite):

    def __init__(self):
        self.blockWidth = blockwidth
        self.blockHeight = blockheight
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.blockWidth, self.blockHeight))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.name = block


class Ball(pygame.sprite.Sprite):
    def __init__(self, displaySurf):
        pygame.sprite.Sprite.__init__(self)
        self.name = ball
        self.moving = False
        self.image = pygame.Surface((15, 15))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.vectorx = ballspeed
        self.vectory = ballspeed * -1
        self.score = 0

    def update(self, *args):
        pass


class Paddle(pygame.sprite.Sprite):
    pass


class Score(object):
    pass


class App(object):
    pass

