import pytest
from utils.examples import read_raw_example_for_day
import math

@pytest.fixture
def day10_example_raw():
    return read_raw_example_for_day(10)

def convert(raw):
    input = raw.split('\n')
    value = 1
    summed_taly = [1]
    for op in input:
        if op == 'noop':
            summed_taly.append(value)
        else:
            parts = op.split()
            if parts[0] == 'addx':
                summed_taly.append(value)
                value += int(parts[1])
                summed_taly.append(value)
    return summed_taly

def process_part1(cycles: list):
    return sum(cycle * value for cycle, value in zip(cycles[19:220:40], [20, 60, 100, 140, 180, 220]))

def process_part2(buffer: list):
    line = 40
    crt = ['█'  if abs(pos - (i % line)) <= 1 else '.' for i, pos in enumerate(buffer)]
    return [''.join(crt[i * line:(i + 1) * line]) for i in range(0, len(buffer) // line)]

def day10_part1(raw):
    cycles = convert(raw)
    return process_part1(cycles)

def day10_part2(raw):
    taly = convert(raw)
    return process_part2(taly)

def test_day10_part1_example(day10_example_raw): 
    assert day10_part1(day10_example_raw) == 13140
def test_day10_part2_example(day10_example_raw): 
    assert day10_part2(day10_example_raw) == [
        '██..██..██..██..██..██..██..██..██..██..',
        '███...███...███...███...███...███...███.',
        '████....████....████....████....████....',
        '█████.....█████.....█████.....█████.....',
        '██████......██████......██████......████',
        '███████.......███████.......███████.....',
    ]  

def test_day10_part1(day10_raw): 
    assert day10_part1(day10_raw) == 14560

def test_day10_part2(day10_raw): 
    assert day10_part2(day10_raw) == [
        '████.█..█.███..█..█.████.███..█..█.████.',
        '█....█.█..█..█.█..█.█....█..█.█..█....█.',
        '███..██...█..█.████.███..█..█.█..█...█..',
        '█....█.█..███..█..█.█....███..█..█..█...',
        '█....█.█..█.█..█..█.█....█....█..█.█....',
        '████.█..█.█..█.█..█.████.█.....██..████.',
    ] 
