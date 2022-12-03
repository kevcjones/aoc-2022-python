import pytest
from functools import reduce
from utils.examples import read_raw_example_for_day

@pytest.fixture
def day03_example_raw():
    return read_raw_example_for_day(3)


# Common utils

def score_from_charcode(character):
    value = ord(character)
    if(value > 96):
        return value - 96
    else:
        return value - 38

def find_common_strings_in_list(listOfStrings):
    common = set(listOfStrings[0])
    for string in listOfStrings:
        common = common & set(string)
    return common

# Part 1

def convert_raw_to_sacks(sacks_raw):
    sacks_raw = sacks_raw.strip()
    sacks = [line for line in sacks_raw.split("\n")]
    return sacks

def split_string_in_half(string):
    halfSize = int(len(string)/2)
    half1,half2 = string[:halfSize], string[halfSize:]
    return half1, half2

def calculate_part1(score, sack):
    half1,half2 = split_string_in_half(sack)
    common = find_common_strings_in_list([half1,half2])
    score = score + score_from_charcode(list(common)[0])
    return score

def day03_part1(sacks_raw):
    sacks = convert_raw_to_sacks(sacks_raw)
    return reduce(calculate_part1, sacks, 0)

def test_day03_part1_example(day03_example_raw): 
    assert day03_part1(day03_example_raw) == 157

def test_day03_part1(day03_raw): 
    assert day03_part1(day03_raw) == 7785


# Part 2

def split_into_teams(sacks_raw):
    sacks_raw = sacks_raw.strip()
    sacks = convert_raw_to_sacks(sacks_raw)
    teams = [sacks[i:i+3] for i in range(0, len(sacks), 3)]
    return teams

def calculate_part2(priority, team):
    common = find_common_strings_in_list(team)
    priority = priority + score_from_charcode(list(common)[0])
    return priority

def day03_part2(sacks_raw):
    teams = split_into_teams(sacks_raw)
    return reduce(calculate_part2, teams, 0)

def test_day03_part2_example(day03_example_raw): 
    assert day03_part2(day03_example_raw) == 70

def test_day03_part2(day03_raw): 
    assert day03_part2(day03_raw) == 2633


