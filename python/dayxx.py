import pytest
from functools import reduce
from utils.examples import read_raw_example_for_day

@pytest.fixture
def dayxx_example_raw():
    return read_raw_example_for_day(x)


# Common utils

def find_common(values):
    common = set(values[0])
    for string in values:
        common = common & set(string)
    return common

def convert_to(raw, converter = lambda x: int(x)):
    raw = raw.strip()
    casted = [converter(line) for line in raw.split("\n")]
    return casted

# Part 1

def calculate_part1(score, value):
    return score + value

def dayxx_part1(raw):
    numbers = convert_to(raw, lambda x: int(x))
    return reduce(calculate_part1, numbers, 0)


def _test_dayxx_part1_example(dayxx_example_raw): 
    assert dayxx_part1(dayxx_example_raw) == 999

def _test_dayxx_part1(dayxx_raw): 
    assert dayxx_part1(dayxx_raw) == 999


# Part 2

# Part 1

def calculate_part2(score, value):
    return score + value

def dayxx_part2(raw):
    numbers = convert_to(raw, lambda x: int(x))
    return reduce(calculate_part2, numbers, 0)


def _test_dayxx_part2_example(dayxx_example_raw): 
    assert dayxx_part2(dayxx_example_raw) == 999

def _test_dayxx_part2(dayxx_raw): 
    assert dayxx_part2(dayxx_raw) == 999
