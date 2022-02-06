#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

from snake import Board


def launch_game() -> None:
    """
    Init the UI and launch it
    """
    board = Board.Board()
    board.run()


if __name__ == "__main__":
    launch_game()