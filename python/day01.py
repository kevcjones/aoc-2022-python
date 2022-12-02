import pytest
from utils.examples import read_raw_example_for_day


def convert_raw_to_lists_of_ints(lines_with_gaps):
    lines_with_gaps = lines_with_gaps.strip()
    list_lists = [line for line in lines_with_gaps.split("\n\n")]
    int_lists = [list(map(int, str_lists.split("\n"))) for str_lists in list_lists]
    return int_lists

# find the highest sum of calories consecutive numbers in a list
def day01_part1(calories_lists_raw):
    calories_lists = convert_raw_to_lists_of_ints(calories_lists_raw)
    highest_sum = max([sum(calory_list) for calory_list in calories_lists])
    return highest_sum

# find the top 3 highest sums of calories consecutive numbers in a list
def day01_part2(calories_lists_raw):
    calories_lists = convert_raw_to_lists_of_ints(calories_lists_raw)
    calories_summed = [sum(calory_list) for calory_list in calories_lists]
    return sum(sorted(calories_summed, reverse=True)[:3])

# Tests
@pytest.fixture
def day01_example_raw():
    return read_raw_example_for_day(1)

def test_day01_part1_example(day01_example_raw): 
    assert day01_part1(day01_example_raw) == 24000

def test_day01_part2_example(day01_example_raw): 
    assert day01_part2(day01_example_raw) == 45000

def test_day01_part1(day01_raw): assert day01_part1(day01_raw) == 67016
def test_day01_part2(day01_raw): assert day01_part2(day01_raw) == 200116
