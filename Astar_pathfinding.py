#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# An A* pathfinding project in Python using pygame for the UI
#
# by Thibault Santonja 2021
#
import pygame
import numpy as np
import unittest
import queue
import math

# Init colors as global variable (yeah, I can do better but nevermind :D )
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200, 50, 50)
GREEN = (0, 200, 100)
BLUE = (0, 100, 200)
GREY = (100, 100, 100)


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

    def __init__(self, row: int, col: int, width: int, color=WHITE) -> None:
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
        return self.color == GREY

    def is_to_visit(self) -> bool:
        """Returns if the case must be visited"""
        return self.color == GREEN

    def is_obstacle(self) -> bool:
        """Returns if the case is an obstacle"""
        return self.color == BLACK

    def is_start(self) -> bool:
        """Returns if the case is the begin"""
        return self.color == BLUE

    def is_end(self) -> bool:
        """Returns if the case is the end"""
        return self.color == RED

    def reset(self) -> None:
        """Reset the case (to white color)"""
        self.color = WHITE

    def set_visited(self) -> None:
        """Set case as visited"""
        self.color = GREY

    def set_to_visit(self) -> None:
        """Set case as to visit"""
        self.color = GREEN

    def set_obstacle(self) -> None:
        """Set case as obstacle"""
        self.color = BLACK

    def set_start(self) -> None:
        """Set case as start"""
        self.color = BLUE

    def set_end(self) -> None:
        """Set case as end"""
        self.color = RED

    def set_path(self) -> None:
        """Set case as path"""
        self.color = BLUE

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


class Grid(object):
    """
	This class corresponds to the grid.
	It stores:
	- the number of rows (and columns)
	- the case size (heigh and width)
	- the grid
	- the pygame window
	- the window width (in pixels)
	"""

    def __init__(self, nb_rows, window, window_width) -> None:
        super(Grid, self).__init__()
        self.__nb_rows = nb_rows
        self.__size = window_width // nb_rows
        self.__grid = np.empty((nb_rows, nb_rows), dtype=object)
        self.window = window
        self.window_width = window_width

    def get_nb_row(self) -> int:
        """Returns the length of grid rows (or column as long as it's a square grid)"""
        return self.__nb_rows

    def get_grid(self) -> object:
        """Returns the grid"""
        return self.__grid

    def __create_grid(self) -> None:
        """Initialize grid cases"""
        for x in range(self.__nb_rows):
            for y in range(self.__nb_rows):
                self.__grid[x][y] = Case(x, y, self.__size)

    def __draw_grid(self) -> None:
        """Draw the grid in the UI (pygame)"""
        for i in range(self.__nb_rows):
            pygame.draw.line(self.window, GREY, (0, i * self.__size), (self.window_width, i * self.__size))
            for j in range(self.__nb_rows):
                pygame.draw.line(self.window, GREY, (j * self.__size, 0), (j * self.__size, self.window_width))

    def __draw_cases(self) -> None:
        """Draws each case"""
        self.window.fill(WHITE)

        for row in self.__grid:
            for case in row:
                case.draw(self.window)

        self.__draw_grid()
        pygame.display.update()

    def __get_click_position(self, position: tuple) -> tuple:
        """Returns the corresponding case number to a click position (it's row and column numbers)"""
        y, x = position
        return y // self.__size, x // self.__size

    def __get_case(self, position: tuple) -> object:
        """Returns a specific case"""
        row, col = position
        return self.__grid[row][col]

    def __make_path(self, origin, current):
        # Draw the full founded path from end to start
        while current in origin:
            current = origin[current]
            current.set_path()
            self.__draw_cases()

    def run(self) -> None:
        """Launch the UI, create the grid and let the user draw and launch the A* path finding"""

        # Initialize the grid
        self.__create_grid()

        # Initialize variables
        start = None  # Store the start point
        end = None  # Store the end point
        run = True  # Store the UI state

        # Run the app
        while run:
            # Draw the grid and draw each cases
            self.__draw_cases()

            # For each received event, check it's type and process an action (if necessary)
            for event in pygame.event.get():

                # Quit the UI
                if event.type == pygame.QUIT:
                    run = False

                # Get a mouse click
                if pygame.mouse.get_pressed()[0]:  # LEFT CLICK
                    # Get where the click happens (on which case)
                    case = self.__get_case(self.__get_click_position(pygame.mouse.get_pos()))

                    # If the start isn't set, set it, else if the end isn't set, set it and
                    # finally, if start and end are set, create an obstacle
                    if not start and case != end:
                        start = case  # Save the starting case
                        start.set_start()
                    elif not end and case != start:
                        end = case  # Save the ending case
                        end.set_end()
                    elif case != end and case != start:
                        case.set_obstacle()

                elif pygame.mouse.get_pressed()[2]:  # RIGHT CLICK
                    # Get where the click happens (on which case)
                    case = self.__get_case(self.__get_click_position(pygame.mouse.get_pos()))

                    # Reset the case type / color
                    case.reset()

                    # If it's the start or the end, reset the corresponding variable
                    if case == start:
                        start = None
                    elif case == end:
                        end = None

                # Get a keyboard action
                if event.type == pygame.KEYDOWN:
                    # If the start and the end are seted, init each cases' neighbors
                    # and launch A* algorithm
                    if event.key == pygame.K_SPACE and start and end:
                        for row in self.__grid:
                            for case in row:
                                case.update_neighbors(self)  # Init neighbors

                        # Launch A* algorithm
                        self.__search_path_A_star(start, end)

                    # Quit the UI
                    if event.key == pygame.K_ESCAPE:
                        run = False

        pygame.quit()

    def __search_path_A_star(self, start, end):
        """
		Uses A* algorithm to find a path:

		f = g + h
		take the lowest f
		g : cost from start to n
		h : estimate cost from n to end

		pseudo-code :
		```
		closedList = List()
		openList = PriorityQueue()
		openList.add(depart)

		while openList is not empty
		   u = openList.get()

		   if u.coordinate == objective.coordinate
			   createThePath(u)
			   END

		   for each neighbors v of u in g
			   if (v is not in closedList) or (not exists in openList with a lower cost)
					v.cost = u.cost + 1 
					v.f = v.cost + distance(v.coordinates, objective.coordinates)
					openList.add(v)

		   closedList.add(u)

		END with error (no path founded)
		```
		"""
        # For h, that represent the cost
        count = 0

        # Init the opened node set
        open_set = {start}

        # Init the opened node priority queue
        opened = queue.PriorityQueue()
        # Start is equal to 0
        opened.put((0, count, start))

        # Init list of weights to infinite
        g_score = {case: float('inf') for row in self.__grid for case in row}
        # Start is equal to 0
        g_score[start] = 0

        # Init list of totals to infinite
        f_score = {case: float('inf') for row in self.__grid for case in row}
        # Start is equal the distance to end
        f_score[start] = start.get_distance(end)

        # Liste origin case to a case n
        origin = {}

        while not opened.empty():
            # Get (one of) the most interesting case to study
            current = opened.get()[2]
            # Remove it from the cases to study set
            open_set.remove(current)

            # Check if it's the end and conclude the algorithm
            if current == end:
                self.__make_path(origin, end)
                return True

            # Analyse every neighbors
            for neighbor in current.neighbors:
                # Increase the score (lower is better)
                g_score_tmp = g_score[current] + 1

                # Check if the current path score is better than it's neighbors
                if g_score_tmp < g_score[neighbor]:
                    # Update the neighbors better path and score since the current
                    # is better (lower cost)
                    origin[neighbor] = current
                    g_score[neighbor] = g_score_tmp
                    f_score[neighbor] = g_score_tmp + neighbor.get_distance(end)

                    # If the neighbor is not in the to study list, add it
                    if neighbor not in open_set:
                        count += 1
                        opened.put((f_score[neighbor], count, neighbor))
                        open_set.add(neighbor)
                        neighbor.set_to_visit()

            # Redraw cases
            self.__draw_cases()

            # Set studied case as visited (except if it's the start to keep it's color)
            if current != start:
                current.set_visited()

        # If nothing is found
        return False


if __name__ == '__main__':
    window_width = 800
    nb_rows = 50

    # Init UI
    pygame.init()
    window = pygame.display.set_mode((window_width, window_width))

    # Init the grid and run it
    grid = Grid(nb_rows, window, window_width)
    grid.run()

# For the test :
# CaseTest().run()


class CaseTest(unittest.TestCase):
    def run(self, **kwargs):
        print("\nRun all tests :")

        case1 = Case(row=1, col=1, width=1)
        case2 = Case(row=1, col=5, width=1)

        self.testCaseInit(case1)
        self.testCaseVisited(case1)
        self.testCaseToVisit(case1)
        self.testCaseObstacle(case1)
        self.testCaseStart(case1)
        self.testCaseEnd(case1)
        self.testCaseReset(case1)

        self.testCaseDistance(case1, case2)

        print("\nRun all test is finished !")

    def testCase(self):
        case1 = Case(row=1, col=1, width=1)
        case2 = Case(row=5, col=1, width=1)
        print(" - test fct()")

        self.assertEqual(case1.get_pos(), (1, 1))

    def testCaseInit(self, case):
        print(" - test CaseInit()")
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseVisited(self, case):
        print(" - test CaseVisited()")
        case.set_visited()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), True)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseToVisit(self, case):
        print(" - test CaseToVisit()")
        case.set_to_visit()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), True)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseObstacle(self, case):
        print(" - test CaseObstacle()")
        case.set_obstacle()
        self.assertEqual(case.is_obstacle(), True)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseStart(self, case):
        print(" - test CaseStart()")
        case.set_start()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), True)
        self.assertEqual(case.is_end(), False)

    def testCaseEnd(self, case):
        print(" - test CaseEnd()")
        case.set_end()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), True)

    def testCaseReset(self, case):
        print(" - test CaseReset()")
        case.reset()
        self.assertEqual(case.is_obstacle(), False)
        self.assertEqual(case.is_visited(), False)
        self.assertEqual(case.is_to_visit(), False)
        self.assertEqual(case.is_start(), False)
        self.assertEqual(case.is_end(), False)

    def testCaseDistance(self, case1, case2):
        print(" - test CaseDistance()")

        self.assertEqual(case1.get_distance(case2), 4)
