#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

from snake import main as snake
from astar_pathfinding import astar_pathfinding
import sys


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        match arg:
            case "snake":
                snake.launch_game()
            case "astar":
                astar_pathfinding.launch_astar()
            case _:
                print(f"Unrecognized argument : {arg}")
