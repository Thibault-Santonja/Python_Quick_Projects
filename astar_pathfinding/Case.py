from astar_pathfinding import config
import pygame


class Case(object):
    """
    This class corresponds to a case in the array.
    It's defined by:
    - a 'row' and a 'col' number
    - a 'width' (and a heigh as long as we have a square)
    - 'x' and 'Y' which corresponds to the case place on the UI (in pixel)
    - a 'color':
        - White at begin
        - Grey if visited
        - Green if it will be visited in a few time (in "to visit" A* list)
        - Black if it's an obstacle
        - Red for the end
        - Blue for the start and finally the full path

    The object will also stores it's "neighbors"

    """

    def __init__(self, row: int, col: int, width: int, color=config.WHITE) -> None:
        super(Case, self).__init__()
        self.__row = row
        self.__col = col
        self.__width = width
        self.__x = row * self.__width
        self.__y = col * self.__width
        self.color = color
        self.neighbors = []

    def get_pos(self) -> tuple:
        """Returns the case position (in the array)"""
        return self.__row, self.__col

    def is_visited(self) -> bool:
        """Returns if the case was visited"""
        return self.color == config.GREY

    def is_to_visit(self) -> bool:
        """Returns if the case must be visited"""
        return self.color == config.GREEN

    def is_obstacle(self) -> bool:
        """Returns if the case is an obstacle"""
        return self.color == config.BLACK

    def is_start(self) -> bool:
        """Returns if the case is the begin"""
        return self.color == config.BLUE

    def is_end(self) -> bool:
        """Returns if the case is the end"""
        return self.color == config.RED

    def reset(self) -> None:
        """Reset the case (to white color)"""
        self.color = config.WHITE

    def set_visited(self) -> None:
        """Set case as visited"""
        self.color = config.GREY

    def set_to_visit(self) -> None:
        """Set case as to visit"""
        self.color = config.GREEN

    def set_obstacle(self) -> None:
        """Set case as obstacle"""
        self.color = config.BLACK

    def set_start(self) -> None:
        """Set case as start"""
        self.color = config.BLUE

    def set_end(self) -> None:
        """Set case as end"""
        self.color = config.RED

    def set_path(self) -> None:
        """Set case as path"""
        self.color = config.BLUE

    def draw(self, window) -> None:
        """Draw the cell in the UI"""
        pygame.draw.rect(window, self.color, (self.__x, self.__y, self.__width, self.__width))

    def get_distance(self, case) -> float:
        """Returns the distance from this case to another"""
        x, y = case.get_pos()
        return abs(x - self.__row) + abs(y - self.__col)

    def update_neighbors(self, grid: object):
        """Update neighbours list"""

        # Reset
        self.neighbors = []

        # Init variables
        nb_row = grid.get_nb_row()
        grid = grid.get_grid()

        # Add BOTTOM neighbour if it exists and if it's not an obstacle
        if self.__row < nb_row - 1 and not grid[self.__row + 1][self.__col].is_obstacle():
            self.neighbors.append(grid[self.__row + 1][self.__col])

        # Add TOP neighbour if it exists and if it's not an obstacle
        if self.__row > 0 and not grid[self.__row - 1][self.__col].is_obstacle():
            self.neighbors.append(grid[self.__row - 1][self.__col])

        # Add RIGHT neighbour if it exists and if it's not an obstacle
        if self.__col < nb_row - 1 and not grid[self.__row][self.__col + 1].is_obstacle():
            self.neighbors.append(grid[self.__row][self.__col + 1])

        # Add LEFT neighbour if it exists and if it's not an obstacle
        if self.__col > 0 and not grid[self.__row][self.__col - 1].is_obstacle():
            self.neighbors.append(grid[self.__row][self.__col - 1])
