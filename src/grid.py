#!/usr/bin/python3
import pprint
import copy
from typing import List
from isvalidvalue import is_valid_value

GridType = List[List[int]]


def grid_print(grid: List[List[int]]):
    """ Print the provided grid """
    print("------------")
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(grid)


class Grid:
    def __init__(self, grid: GridType):
        self.grid = grid
        self.count = 0
        self.solutions: List[GridType] = []

    def solve(self):
        """ Perform the solve """
        self.count = 0
        self.solution = []
        self._grid_solve(self.grid)

    def results(self):
        """ Print the results of solving the grid """
        print(f"no of solutions = {self.count}")
        for i, s in enumerate(self.solutions):
            print(f"solution = {i+1}")
            grid_print(s)

    def _record_solution(self, grid: GridType):
        """ Record a found solution """
        self.count += 1
        self.solutions.append(copy.deepcopy(grid))

    def _grid_solve(self, grid: GridType) -> bool:
        """ Given a grid solve it """
        # Look for an empty position
        for y in range(9):
            for x in range(9):
                # Empty position
                if grid[y][x] == 0:
                    for v in range(1, 10):
                        if is_valid_value(v, y, x, grid):
                            # update grid and call recursively
                            grid[y][x] = v

                            if not self._grid_solve(grid):
                                grid[y][x] = 0

                    # Failed to find any solutions
                    return False
        # Record successful solution
        self._record_solution(grid)
        return True
