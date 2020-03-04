#!/usr/bin/python3
from grid import Grid, GridType

# Sudoku from the Evening Standard 5/02/2020
sudoku = [
    [0, 0, 7, 3, 0, 0, 0, 4, 0],
    [6, 3, 0, 0, 5, 4, 9, 0, 0],
    [0, 9, 0, 2, 0, 0, 0, 0, 8],
    [0, 1, 0, 0, 0, 0, 7, 0, 2],
    [0, 8, 0, 0, 1, 2, 0, 3, 0],
    [2, 0, 5, 0, 0, 0, 0, 6, 0],
    [3, 0, 0, 0, 0, 9, 0, 7, 0],
    [0, 0, 1, 5, 6, 0, 0, 0, 4],
    [0, 6, 0, 0, 0, 1, 8, 0, 3],
]


def main(grid: GridType):
    g = Grid(grid)
    g.solve()
    g.results()


if __name__ == "__main__":
    main(sudoku)
