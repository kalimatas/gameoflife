#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Conway's Game of life
"""

from optparse import OptionParser
from sprites.boxes import Box

VERSION = "%prog 1.0"
DESCRIPTION = "Conway's Game of life"

DEFAULT_HEIGHT = 40
DEFAULT_WIDTH = 80
DEFAULT_SIZE = 10
CELL_DEAD = '.'
CELL_LIVE = 'o'

def main():
    pass

if __name__ == "__main__":
    parser = OptionParser(version=VERSION, description=DESCRIPTION)
    parser.add_option("--width", type="int", dest="width", default=DEFAULT_WIDTH, help="Field width")
    parser.add_option("--height", type="int", dest="height", default=DEFAULT_HEIGHT, help="Field height")
    parser.add_option("--size", type="int", dest="size", default=DEFAULT_SIZE, help="Cell size")
    parser.add_option("--debug", action="store_true", dest="debug", help="Debug flag", default=False)

    (options, args) = parser.parse_args()

    main()