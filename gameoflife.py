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
white = (255, 255, 255)

def init_screen(width, height, size):
    """
    Initialize pygame screen
    """
    pygame.init()
    pygame.display.set_caption(DESCRIPTION)
    screen = pygame.display.set_mode([width * size, height * size])
    return screen

def update_display(screen, board, boxes, options, rand_col = False, keep_background = False):
    """
    Updating display
    """
    for dy in range(options.height):
        for dx in range(options.width):
            if board[dx][dy] == CELL_LIVE:
                if rand_col:
                    boxes[dx][dy] = Box([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], [dx * options.size, dy * options.size], options.size)
                else:
                    boxes[dx][dy] = Box(white, [dx * options.size, dy * options.size], options.size)
            elif not keep_background:
                boxes[dx][dy] = Box(black, [dx * options.size, dy * options.size], options.size)

            screen.blit(boxes[dx][dy].image, boxes[dx][dy].rect)

    pygame.display.update()

def rules_of_life(board, options):
    """
    Rules of the games
    """
    total_pop = 0
    pop_list = [['0' for i in range(options.height)] for j in range(options.width)]

    def borderless(pos, max):
        if pos < 0:
            pos = max + pos
        elif pos >= max:
            pos = abs(pos) % max
        return pos

    for y in range(options.height):
        for x in range(options.width):
            pop = 0
            buf = []

            # bottom row
            if board[borderless(x - 1, options.width)][borderless(y - 1, options.height)] == CELL_LIVE:
                pop += 1
            if board[borderless(x, options.width)][borderless(y - 1, options.height)] == CELL_LIVE:
                pop += 1
            if board[borderless(x + 1, options.width)][borderless(y - 1, options.height)] == CELL_LIVE:
                pop += 1

            # middle row
            if board[borderless(x - 1, options.width)][borderless(y, options.height)] == CELL_LIVE:
                pop += 1
            if board[borderless(x + 1, options.width)][borderless(y, options.height)] == CELL_LIVE:
                pop += 1

            # upper row
            if board[borderless(x - 1, options.width)][borderless(y + 1, options.height)] == CELL_LIVE:
                pop += 1
            if board[borderless(x, options.width)][borderless(y + 1, options.height)] == CELL_LIVE:
                pop += 1
            if board[borderless(x + 1, options.width)][borderless(y + 1, options.height)] == CELL_LIVE:
                pop += 1

            total_pop += pop
            pop_list[x][y] = pop

    # apply rules
    for y in range(options.height):
        for x in range(options.width):
            if board[x][y] == CELL_LIVE and (pop_list[x][y] < 2 or pop_list[x][y] > 3):
                board[x][y] = CELL_DEAD
            elif board[x][y] == CELL_DEAD and pop_list[x][y] == 3:
                board[x][y] = CELL_LIVE

    return board

def main(options, args):
    # prepare boxes
    boxes = [['' for i in range(options.height)] for j in range(options.width)]

    # fill board with dead cells
    board = [[CELL_DEAD for i in range(options.height)] for j in range(options.width)]

    # set screen params
    screen = init_screen(options.width, options.height, options.size)

    running = True
    button_down = False
    keep_background = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                running = False

            if event.type == KEYDOWN and event.key == K_r:
                # set random
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                button_down = True
                button_type = event.button

            if event.type == MOUSEBUTTONUP:
                button_down = False

            if button_down:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                sp_x = mouse_x / options.size
                sp_y = mouse_y / options.size

                if button_type == 1:
                    board[sp_x][sp_y] = CELL_LIVE
                elif button_type == 3:
                    board[sp_x][sp_y] = CELL_DEAD

                update_display(screen, board, boxes, options)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            if event.type == KEYDOWN and event.key == K_b:
                if not keep_background:
                    keep_background = True
                else:
                    keep_background = False

        update_display(screen, board, boxes, options, rand_col=True, keep_background=keep_background)
        board = rules_of_life(board, options)
        pygame.time.delay(10)

if __name__ == "__main__":
    parser = OptionParser(version=VERSION, description=DESCRIPTION)
    parser.add_option("--width", type="int", dest="width", default=DEFAULT_WIDTH, help="Field width")
    parser.add_option("--height", type="int", dest="height", default=DEFAULT_HEIGHT, help="Field height")
    parser.add_option("--size", type="int", dest="size", default=DEFAULT_SIZE, help="Cell size")
    parser.add_option("--debug", action="store_true", dest="debug", help="Debug flag", default=False)

    (options, args) = parser.parse_args()
    main(options, args)
    pygame.quit()