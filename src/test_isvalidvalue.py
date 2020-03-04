#!/usr/bin/python3

import pytest

from isvalidvalue import is_valid_value


@pytest.fixture
def grid():
    return [
        [0, 1, 0, 0, 0, 5, 0, 8, 3],
        [0, 0, 0, 8, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 5],
        [3, 0, 0, 0, 6, 9, 0, 0, 7],
        [0, 0, 6, 0, 0, 0, 5, 0, 0],
        [4, 0, 0, 7, 3, 0, 0, 0, 6],
        [7, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [8, 6, 0, 2, 0, 0, 0, 1, 0],
    ]


def test_row(grid):
    assert is_valid_value(2, 0, 2, grid)
    assert is_valid_value(1, 0, 2, grid) is False


def test_column(grid):
    assert is_valid_value(6, 0, 0, grid)
    assert is_valid_value(7, 0, 0, grid) is False


def test_square(grid):
    assert is_valid_value(2, 0, 0, grid)
    assert is_valid_value(9, 0, 4, grid) is False
