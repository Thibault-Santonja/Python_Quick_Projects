#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# An A* pathfinding project in Python using pygame for the UI
#
# by Thibault Santonja 2021
#
import pygame
from astar_pathfinding import Grid


def launch_astar():
    window_width = 800
    nb_rows = 50

    # Init UI
    pygame.init()
    window = pygame.display.set_mode((window_width, window_width))

    # Init the grid and run it
    grid = Grid.Grid(nb_rows, window, window_width)
    grid.run()

