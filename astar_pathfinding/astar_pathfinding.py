#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# An A* pathfinding project in Python using pygame for the UI
#
# by Thibault Santonja 2021
#
import pygame


def launch_astar(window_width: int = 800, nb_rows: int = 50):
    from astar_pathfinding import Grid
    # Init UI
    pygame.init()
    window = pygame.display.set_mode((window_width, window_width))

    # Init the grid and run it
    grid = Grid.Grid(nb_rows, window, window_width)
    grid.run()


if __name__ == "__main__":
    launch_astar()
