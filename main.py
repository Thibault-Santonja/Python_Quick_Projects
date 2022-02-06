#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        match arg:  # noqa
            case "snake":
                from snake import main as snake
                snake.launch_game()
            case "astar":
                from astar_pathfinding import astar_pathfinding
                astar_pathfinding.launch_astar()
            case _:
                print(f"Unrecognized argument : {arg}")
