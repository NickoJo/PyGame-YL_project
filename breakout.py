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

    def update(self, mousex, blocks, paddle, *args):
        if self.moving == False:
            self.rect.centerx = mousex

        else:
            self.rect.y += self.vectory

            hitGroup = pygame.sprite.Group(paddle, blocks)

            spriteHitList = pygame.sprite.spritecollide(self, hitGroup, False)
            if len(spriteHitList) > 0:
                for sprite in spriteHitList:
                    if sprite.name == block:
                        sprite.kill()
                        self.score += 1
                self.vectory *= -1
                self.rect.y += self.vectory

            self.rect.x += self.vectorx

            blockHitList = pygame.sprite.spritecollide(self, blocks, True)

            if len(blockHitList) > 0:
                self.vectorx *= -1
                self.score += 1

            if self.rect.right > width:
                self.vectorx *= -1
                self.rect.right = width

            elif self.rect.left < 0:
                self.vectorx *= -1
                self.rect.left = 0

            if self.rect.top < 0:
                self.vectory *= -1
                self.rect.top = 0


class Paddle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((paddlewidth, paddleheight))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.name = paddle

    def update(self, mousex, *args):
        if self.rect.x >= 0 and self.rect.right <= width:
            self.rect.centerx = mousex

        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > width:
            self.rect.right = width



class Score(object):
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('Helvetica', 25)
        self.render = self.font.render('Score: ' + str(self.score), True, white, black)
        self.rect = self.render.get_rect()
        self.rect.x = 0
        self.rect.bottom = height


class App(object):
    def __init__(self):
        pygame.init()
        self.displaySurf, self.displayRect = self.makeScreen()
        self.mousex = 0
        self.blocks = self.createBlocks()
        self.paddle = self.createPaddle()
        self.ball = self.createBall()
        self.score = Score()

        self.allSprites = pygame.sprite.Group(self.blocks, self.paddle, self.ball)

    def updateScore(self):
        self.score.score = self.ball.score
        self.score.render = self.score.font.render('Score: ' + str(self.score.score), True, white, black)
        self.score.rect = self.score.render.get_rect()
        self.score.rect.x = 0
        self.score.rect.bottom = height

    def makeScreen(self):
        pygame.display.set_caption('Arkanoid')
        displaySurf = pygame.display.set_mode((width, height))
        displayRect = displaySurf.get_rect()
        displaySurf.fill(background)
        displaySurf.convert()

        return displaySurf, displayRect

    def createBall(self):
        ball = Ball(self.displaySurf)
        ball.rect.centerx = self.paddle.rect.centerx
        ball.rect.bottom = self.paddle.rect.top

        return ball

    def createPaddle(self):
        paddle = Paddle()
        paddle.rect.centerx = self.displayRect.centerx
        paddle.rect.bottom = self.displayRect.bottom

        return paddle

    def createBlocks(self):
        blocks = pygame.sprite.Group()

        for row in range(arrayheight):
            for i in range(arraywidth):
                block = Block()
                block.rect.x = i * (blockwidth + blockgap)
                block.rect.y = row * (blockheight + blockgap)
                block.color = self.setBlockColor(block, row, i)
                block.image.fill(block.color)
                blocks.add(block)

        return blocks

    def setBlockColor(self, block, row, column):
        if column == 0 or column % 2 == 0:
            return green
        else:
            return blue

    def checkInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()

            if event.type == MOUSEMOTION:
                # We only need the x value of a mousemotion, so we grab
                # only the first value of the event.pos tuple
                self.mousex = event.pos[0]

            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    self.ball.moving = True

    def terminate(self):
        pygame.quit()
        sys.exit()

    def mainLoop(self):
        while True:
            self.displaySurf.fill(background)
            self.updateScore()
            self.displaySurf.blit(self.score.render, self.score.rect)
            self.allSprites.update(self.mousex, self.blocks, self.paddle)
            self.allSprites.draw(self.displaySurf)
            pygame.display.update()
            self.checkInput()

if __name__ == '__main__':
    runGame = App()
    runGame.mainLoop()
