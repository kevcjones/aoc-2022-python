import pytest
from utils.examples import read_raw_example_for_day
import math

@pytest.fixture
def day09_example_raw():
    return read_raw_example_for_day(9)

def convert(raw):
    raw = raw.strip()
    offsets = {'L': (-1, 0), 'R': (1, 0), 'D': (0, -1), 'U': (0, 1)}
    casted = [ (offsets[line[0]], int(line[1:])) for line in raw.split("\n")]
    return casted

def move(moves, length):
    xs = [0] * length
    ys = [0] * length
    visited = { (xs[-1], ys[-1]) }
    for (mx, my), distance in moves:
        for _ in range(distance):
            xs[0] += mx
            ys[0] += my
            for i in range(length - 1):
                d_x = xs[i + 1] - xs[i]
                d_y = ys[i + 1] - ys[i]
                if abs(d_x) == 2 or abs(d_y) == 2:
                    xs[i + 1] = xs[i] + int(d_x / 2)
                    ys[i + 1] = ys[i] + int(d_y / 2)
            visited.add( (xs[-1], ys[-1]) )
    return len(visited)

def move_gpt_converted(moves, length):
    # Initialize the rope at (0, 0)
    rope = [(0, 0)] * length

    # Store the visited points in a set
    visited = {rope[-1]}

    for (mx, my), distance in moves:
        for _ in range(distance):
            # Move the first point in the rope
            rope[0] = (rope[0][0] + mx, rope[0][1] + my)

            # Move each point in the rope next to its neighbor
            for i in range(length - 1):
                x, y = rope[i]
                nx, ny = rope[i + 1]
                dx = nx - x
                dy = ny - y
                if abs(dx) == 2 or abs(dy) == 2:
                    rope[i + 1] = (x + int(dx / 2), y + int(dy / 2))

            # Add the last point in the rope to the set of visited points
            visited.add(rope[-1])

    # Return the number of visited points
    return len(visited)


def day09_part1(raw):
    moves = convert(raw)
    return move_gpt_converted(moves, 2)

def day09_part2(raw):
    moves = convert(raw)
    return move_gpt_converted(moves, 10)


def test_day09_part1(day09_raw): 
    assert day09_part1(day09_raw) == 6339

def test_day09_part2(day09_raw): 
    assert day09_part2(day09_raw) == 2541
