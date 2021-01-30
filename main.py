# Just move to the right
# Jan 30 2021

import pygame
from pygame.locals import *
import sys

swidth = 800  # screen size
sheight = 400


class MyMap:  # the map class

    def __init__(self, x, y, back):
        # load the picture
        self.bg = pygame.image.load(back).convert_alpha()  # picture
        self.x = x
        self.y = y

    def map_rolling(self):
        if self.x < -790:  # map disappeared on the left side
            self.x = 800  # give the map a new pos
        else:
            self.x -= 5  # roll the map to the left

    # 更新地图
    def map_update(self):
        SCREEN.blit(self.bg, (self.x, self.y))  # update the map


def Game():
    pygame.init()
    end = False
    global SCREEN, FPSCLOCK
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((swidth, sheight))
    pygame.display.set_caption("move move")
    bg1 = MyMap(0, 0, "pic/back.png")
    bg2 = MyMap(800, 0, "pic/back2.png")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if not end:
            bg1.map_update()
            bg1.map_rolling()
            bg2.map_update()
            bg2.map_rolling()
        FPSCLOCK.tick(30)

        pygame.display.update()


if __name__ == '__main__':
    Game()
