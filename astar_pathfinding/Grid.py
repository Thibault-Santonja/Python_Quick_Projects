import numpy as np
import queue
import pygame

from astar_pathfinding import Case, config


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

    def get_grid(self):
        """Returns the grid"""
        return self.__grid

    def __create_grid(self) -> None:
        """Initialize grid cases"""
        for x in range(self.__nb_rows):
            for y in range(self.__nb_rows):
                self.__grid[x][y] = Case.Case(x, y, self.__size)

    def __draw_grid(self) -> None:
        """Draw the grid in the UI (pygame)"""
        for i in range(self.__nb_rows):
            pygame.draw.line(self.window, config.GREY, (0, i * self.__size), (self.window_width, i * self.__size))
            for j in range(self.__nb_rows):
                pygame.draw.line(self.window, config.GREY, (j * self.__size, 0), (j * self.__size, self.window_width))

    def __draw_cases(self) -> None:
        """Draws each case"""
        self.window.fill(config.WHITE)

        for row in self.__grid:
            for case in row:
                case.draw(self.window)

        self.__draw_grid()
        pygame.display.update()

    def __get_click_position(self, position: tuple) -> tuple:
        """Returns the corresponding case number to a click position (it's row and column numbers)"""
        y, x = position
        return y // self.__size, x // self.__size

    def __get_case(self, position: tuple):
        """Returns a specific case"""
        row, col = position
        return self.__grid[row][col]

    def __make_path(self, origin, current) -> None:
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

    def __search_path_A_star(self, start, end) -> bool:
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
