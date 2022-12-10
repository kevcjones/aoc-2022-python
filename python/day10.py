import pytest
from utils.examples import read_raw_example_for_day
import math

@pytest.fixture
def day10_example_raw():
    return read_raw_example_for_day(10)

def convert(raw):
    raw = raw.strip()
    cycles = [1]
    lines = [x for x in raw.split("\n")]
    for line in lines:
        if line.startswith("noop"):
            cycles.append(0)
        elif line.startswith("addx"):
            [_, val] = line.split()
            cycles.append(0)
            cycles.append(int(val))
    return cycles

def convert2(raw):
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
    first_20 = sum(cycles[:20]) * 20
    first_60 = sum(cycles[:60]) * 60
    first_100 = sum(cycles[:100]) * 100
    first_140 = sum(cycles[:140]) * 140
    first_180 = sum(cycles[:180]) * 180
    first_220 = sum(cycles[:220]) * 220
    return first_20 + first_60 + first_100 + first_140 + first_180 + first_220

def process_part2(buffer: list):
    
    line = 40
    crt = ['█'  if abs(pos - (i % line)) <= 1 else '.' for i, pos in enumerate(buffer)]
    for i in range(0, len(buffer) // line):
        print(''.join(crt[i * line:(i + 1) * line]))
    
    
    return crt


def day10_part1(raw):
    cycles = convert(raw)
    return process_part1(cycles)

def day10_part2(raw):
    taly = convert2(raw)
    return process_part2(taly)


def test_day10_part1_example(day10_example_raw): 
    assert day10_part1(day10_example_raw) == 13140
def test_day10_part2_example(day10_example_raw): 
    assert day10_part2(day10_example_raw) == 0

def test_day10_part1(day10_raw): 
    assert day10_part1(day10_raw) == 0 

def test_day10_part2(day10_raw): 
    assert day10_part2(day10_raw) == 0
