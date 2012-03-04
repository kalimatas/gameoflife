#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Conway's Game of life
"""

import pygame, time, random
from optparse import OptionParser
from sprites.boxes import Box
from pygame.locals import *

VERSION = "%prog 1.0"
DESCRIPTION = "Conway's Game of life"

DEFAULT_HEIGHT = 40
DEFAULT_WIDTH = 80
DEFAULT_SIZE = 10
CELL_DEAD = '.'
CELL_LIVE = 'o'

# colors
black = (0, 0, 0)

def init_screen(width, height, size):
    """
    Initialize pygame screen
    """
    pygame.init()
    pygame.display.set_caption(DESCRIPTION)
    screen = pygame.display.set_mode([width * size, height * size])
    return screen

def main(options, args):
    # prepare boxes
    boxes = [['' for i in range(options.width)] for j in range(options.height)]

    # fill board with dead cells
    board = [[CELL_DEAD for i in range(options.width)] for j in range(options.height)]

    # set screen params
    screen = init_screen(options.width, options.height, options.size)
    clock = pygame.time.Clock()

    running = False
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                running = False

        screen.fill(black)
        clock.time(20)
        pygame.display.flip()


if __name__ == "__main__":
    parser = OptionParser(version=VERSION, description=DESCRIPTION)
    parser.add_option("--width", type="int", dest="width", default=DEFAULT_WIDTH, help="Field width")
    parser.add_option("--height", type="int", dest="height", default=DEFAULT_HEIGHT, help="Field height")
    parser.add_option("--size", type="int", dest="size", default=DEFAULT_SIZE, help="Cell size")
    parser.add_option("--debug", action="store_true", dest="debug", help="Debug flag", default=False)

    (options, args) = parser.parse_args()
    main(options, args)
    pygame.quit()