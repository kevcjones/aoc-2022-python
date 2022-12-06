import pytest
from utils.examples import read_raw_example_for_day

@pytest.fixture
def day06_example_raw():
    return read_raw_example_for_day(5)



def find_unique_sequence(raw, size=4):
    for i in range(0, len(raw)):
        if len(set(raw[i:i+size])) == size:
            return i+size
    

# Part 1
def test_day06_part1_example(): 
    assert find_unique_sequence('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5

def test_day06_part1_example1(): 
    assert find_unique_sequence('nppdvjthqldpwncqszvftbrmjlhg') == 6

def test_day06_part1_example2(): 
    assert find_unique_sequence('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10

def test_day06_part1_example3(): 
    assert find_unique_sequence('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

def test_day06_part1(day06_raw): 
    assert find_unique_sequence(day06_raw) == 1987

def test_day06_part2_example(): 
    assert find_unique_sequence('mjqjpqmgbljsphdztnvjfqwrcgsmlb',14) == 19

def test_day06_part2_example1(): 
    assert find_unique_sequence('bvwbjplbgvbhsrlpgdmjqwftvncz',14) == 23

def test_day06_part2_example2(): 
    assert find_unique_sequence('nppdvjthqldpwncqszvftbrmjlhg',14) == 23

def test_day06_part2_example3(): 
    assert find_unique_sequence('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',14) == 29

def test_day06_part2(day06_raw): 
    assert find_unique_sequence(day06_raw,14) == 3059