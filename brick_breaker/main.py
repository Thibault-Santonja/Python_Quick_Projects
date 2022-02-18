from brick_breaker import Board


def launch_game() -> None:
    """
    Init the UI and launch it
    """
    board = Board.Board()
    board.launch()


if __name__ == "__main__":
    launch_game()
