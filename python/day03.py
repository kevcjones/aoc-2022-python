import pytest
from utils.examples import read_raw_example_for_day

def getScoreFromPresent(presentCharacter):
    value = ord(presentCharacter)
    if(value > 96):
        return value - 96
    else:
        return value - 38

def splitEveryThirdSack(sacks):
    return [sacks[i:i+3] for i in range(0, len(sacks), 3)]

def convert_raw_to_sacks(sacks_raw):
    sacks_raw = sacks_raw.strip()
    sacks = [line for line in sacks_raw.split("\n")]
    return sacks

def convert_raw_to_teams(sacks_raw):
    sacks_raw = sacks_raw.strip()
    sacks = convert_raw_to_sacks(sacks_raw)
    teams = splitEveryThirdSack(sacks)
    return teams


def day03_part1(sacks_raw):
    sacks = convert_raw_to_sacks(sacks_raw)
    gifts = []
    for sack in sacks:
        halfSize = int(len(sack)/2)
        half1,half2 = sack[:halfSize], sack[halfSize:]
        common = set(half1) & set(half2)
        gifts.append(getScoreFromPresent(list(common)[0]))
    return sum(gifts)


def day03_part2(sacks_raw):
    teams = convert_raw_to_teams(sacks_raw)
    priorityList = []
    for team in teams:
        common = set(team[0]) & set(team[1]) & set(team[2])
        priorityList.append(getScoreFromPresent(list(common)[0]))
    return sum(priorityList)

# # Tests
@pytest.fixture
def day03_example_raw():
    return read_raw_example_for_day(3)

def test_day03_part1_example(day03_example_raw): 
    assert day03_part1(day03_example_raw) == 157

def test_day03_part2_example(day03_example_raw): 
    assert day03_part2(day03_example_raw) == 70

def test_day03_part1(day03_raw): assert day03_part1(day03_raw) == 7785
def test_day03_part2(day03_raw): assert day03_part2(day03_raw) == 2633
