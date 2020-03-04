from typing import List


def is_valid_value(v: int, y: int, x: int, grid: List[List[int]]) -> bool:
    """
    Returns true if this is a valid value for this position.

    Note that the y and x are the opposite to what you would expect,
    due to the arrangement of the indices in the grid.
    """
    # if the number is not present in
    #   this row
    for i in range(9):
        if grid[y][i] == v:
            return False
    #   this column
    for i in range(9):
        if grid[i][x] == v:
            return False
    #   or this square
    xorigin = (x // 3) * 3
    yorigin = (y // 3) * 3
    for yy in range(3):
        for xx in range(3):
            if grid[yorigin + yy][xorigin + xx] == v:
                return False

    return True
