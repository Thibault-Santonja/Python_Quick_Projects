import pygame


class Board:
    _display = None
    _continue = False

    def __init__(self, size_x: int = 800, size_y: int = 600) -> None:
        self.init_board(size_x=size_x, size_y=size_y)
        self._run()

    def init_board(self, size_x: int = 800, size_y: int = 600) -> None:
        pygame.init()
        self._display = pygame.display.set_mode((size_x, size_y))

    def _run(self) -> None:
        self._continue = True

        while self._continue:
            for event in pygame.event.get():

                # Quit the UI
                if event.type == pygame.QUIT:
                    self._continue = False

                # Get a keyboard action
                if event.type == pygame.KEYDOWN:
                    # Quit the UI
                    if event.key == pygame.K_ESCAPE:
                        self._continue = False

        pygame.quit()
