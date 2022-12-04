import pytest
from functools import reduce
from utils.examples import read_raw_example_for_day

@pytest.fixture
def day04_example_raw():
    return read_raw_example_for_day(4)


# Common utils

def convert_to_ranges(raw):
    raw = raw.strip()
    ranges = [line.strip('[]').split(',') for line in raw.split("\n")]
    return ranges

def find_common(values):
    common = set(values[0])
    for string in values:
        common = common & set(string)
    return common

def convert_dash_range_to_list(range_string):
    range_string = range_string.strip()
    start,finish = range_string.split('-')
    return range(int(start),int(finish)+1)


# Part 1

def calculate_part1(score, list_assignments):
    elf1,elf2 = [convert_dash_range_to_list(elf) for elf in list_assignments]
    common = find_common([elf1,elf2])
    overlaps = len(common) == len(elf1) or len(common) == len(elf2)
    if overlaps:
        score = score + 1
    return score

def day04_part1(raw):
    range_tuples = convert_to_ranges(raw)
    return reduce(calculate_part1, range_tuples, 0)



def test_day04_part1_example(day04_example_raw): 
    assert day04_part1(day04_example_raw) == 3

def test_day04_part1(day04_raw): 
    assert day04_part1(day04_raw) == 483


# Part 2


def calculate_part2(score, list_assignments):
    elf1,elf2 = [convert_dash_range_to_list(elf) for elf in list_assignments]
    common = find_common([elf1,elf2])
    if(len(common) > 0):
        score = score + 1
    return score

def day04_part2(raw):
    range_tuples = convert_to_ranges(raw)
    return reduce(calculate_part2, range_tuples, 0)



def test_day04_part2_example(day04_example_raw): 
    assert day04_part2(day04_example_raw) == 5

def test_day04_part2(day04_raw): 
    assert day04_part2(day04_raw) == 2633


