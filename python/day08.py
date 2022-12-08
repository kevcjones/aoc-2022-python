import pytest
from utils.examples import read_raw_example_for_day
import math
import sys

@pytest.fixture
def day08_example_raw():
    return read_raw_example_for_day(8)

def is_visible(grid, row_pos, col_pos):
    if row_pos == 0 or row_pos == len(grid) - 1:
        return True
    if col_pos == 0 or col_pos == len(grid[row_pos]) - 1:
        return True

    row = grid[row_pos]
    height = grid[row_pos][col_pos]
    column = [grid[row_pos][col_pos] for row_pos in range(len(grid))]

    left = all(x < height for x in row[:col_pos])
    right = all(x < height for x in row[col_pos + 1:])
    top = all(x < height for x in column[:row_pos])
    bottom = all(x < height for x in column[row_pos + 1:])

    return left or right or top or bottom

def get_score(grid, row_pos, col_pos):
    height = grid[row_pos][col_pos]
    row = grid[row_pos]
    column = [grid[row_pos][col_pos] for row_pos in range(len(grid))]

    left, right, top, bottom = 0, 0, 0, 0

    # west
    for x in reversed(row[:col_pos]):
        left += 1
        if x >= height:
            break

    # east
    for x in row[col_pos + 1:]:
        right += 1
        if x >= height:
            break

    # top
    for x in reversed(column[:row_pos]):
        top += 1
        if x >= height:
            break

    # bottom
    for x in column[row_pos + 1:]:
        bottom += 1
        if x >= height:
            break

    return left * right * top * bottom


def day08_part1(raw):
    raw = raw.splitlines()
    grid = [[int(x) for x in list(line)] for line in raw]
    seen = sum([is_visible(grid, row_index, column_index)
             for row_index in range(len(grid))
             for column_index in range(len(grid[row_index]))])
    return seen

def day08_part2(raw):
    raw = raw.splitlines()
    grid = [[int(x) for x in list(line)] for line in raw]
    scenic_score = max([get_score(grid, row_index, col_index)
              for row_index in range(len(grid))
              for col_index in range(len(grid[row_index]))])
    return scenic_score


def test_day08_part1_example(day08_example_raw): 
    assert day08_part1(day08_example_raw) == 21

def test_day08_part1(day08_raw): 
    assert day08_part1(day08_raw) == 1789

def test_day08_part2_example(day08_example_raw): 
    assert day08_part2(day08_example_raw) == 8

def test_day08_part2(day08_raw): 
    assert day08_part2(day08_raw) == 314820
