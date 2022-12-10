import pytest
from utils.examples import read_raw_example_for_day
from functools import reduce

@pytest.fixture
def day10_example_raw():
    return read_raw_example_for_day(10)

def process_instructions(acc, op):
    value, sums = acc
    if op == 'noop':
        sums.append(value)
    else:
        _,add = op.split()
        sums.append(value)
        value += int(add)
        sums.append(value)
    return (value, sums)

def convert(raw):
    input = raw.split('\n')
    _,sums = reduce(process_instructions, input, (1, [1]))
    return sums

def day10_part1(raw):
    sums = convert(raw)
    return sum(cycle * value for cycle, value in zip(sums[19:220:40], [20, 60, 100, 140, 180, 220]))

def day10_part2(raw):
    buffer = convert(raw)
    line = 40
    crt = ['█'  if abs(pos - (i % line)) <= 1 else '.' for i, pos in enumerate(buffer)]
    return [''.join(crt[i * line:(i + 1) * line]) for i in range(0, len(buffer) // line)]


# tests

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
