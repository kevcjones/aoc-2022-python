import pytest
from utils.examples import read_raw_example_for_day

decryption_key = {
    # X LOSE
    "A X": "A Z", 
    "B X": "B X",
    "C X": "C Y", 
    # Y DRAW
    "A Y": "A X",   
    "B Y": "B Y", 
    "C Y": "C Z",
    # Z WIN 
    "A Z": "A Y", 
    "B Z": "B Z",    
    "C Z": "C X", 
}

score_book = {
    "A Y": 8, # ROCK PAPER WIN 2  
    "B Z": 9, # PAPER SCISSORS WIN 3   
    "C X": 7, # SCISSORS ROCK LOSS 1
    "A X": 4, # ROCK ROCK DRAW 1
    "B Y": 5, # PAPER PAPER DRAW 2
    "C Z": 6, # SCISSORS SCISSORS DRAW 3
    "A Z": 3, # ROCK SCISSORS LOSE 3
    "B X": 1, # PAPER ROCK LOSE 1
    "C Y": 2 # SCISSORS PAPER LOSE 2
}



def convert_raw_to_hands(hands_raw):
    hands_raw = hands_raw.strip()
    hands = [line for line in hands_raw.split("\n")]
    return hands

def day02_part1(hands_raw):
    hands = convert_raw_to_hands(hands_raw)
    scores = [score_book[hand] for hand in hands]
    return sum(scores)

def day02_part2(hands_raw):
    hands = convert_raw_to_hands(hands_raw)
    scores = [score_book[decryption_key[hand]] for hand in hands]
    return sum(scores)

# Tests
@pytest.fixture
def day02_example_raw():
    return read_raw_example_for_day(2)

def test_day02_part1_example(day02_example_raw): 
    assert day02_part1(day02_example_raw) == 15

def test_day02_part2_example(day02_example_raw): 
    assert day02_part2(day02_example_raw) == 12

def test_day02_part1(day02_raw): assert day02_part1(day02_raw) == 10404
def test_day02_part2(day02_raw): assert day02_part2(day02_raw) == 10334
