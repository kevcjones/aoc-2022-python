import pytest
from functools import reduce
from utils.examples import read_raw_example_for_day
import re


@pytest.fixture
def day05_example_raw():
    return read_raw_example_for_day(5)

def parse_move_instructions(moves_raw):
    moves = [list(map(int, x.split()[1::2])) for x in moves_raw.split('\n') if x]
    return moves

def transpose_to_stack_lists(crates_rows):
    stacks = ["".join([y[x] for y in crates_rows]).strip() for x in range(len(crates_rows[0]))]
    return stacks

def get_rows_of_crate_letters(crates_raw):
    crates_rows = [crate_letter[1::4] for crate_letter in crates_raw.split('\n')[:-1]]
    return crates_rows

def get_crates_and_moves(raw):
    crates_raw,moves_raw = raw.split('\n\n')
    return crates_raw,moves_raw

def compute_it(raw, order=-1):
    crates_raw, moves_raw = get_crates_and_moves(raw)
    crates_rows = get_rows_of_crate_letters(crates_raw)
    stacks = transpose_to_stack_lists(crates_rows)
    moves = parse_move_instructions(moves_raw)
    for count,from_stack,to_stack in moves:
        stacks[to_stack - 1] = stacks[from_stack - 1][:count][::order] + stacks[to_stack - 1]
        stacks[from_stack - 1] = stacks[from_stack - 1][count:]
    return "".join(stack[0] for stack in stacks)

# Part 1

def day05_part1(raw):
    return compute_it(raw)

def test_day05_part1_example(day05_example_raw): 
    assert day05_part1(day05_example_raw) == 'CMZ'

def test_day05_part1(day05_raw): 
    assert day05_part1(day05_raw) == 'WSFTMRHPP'

def day05_part2(raw):
    return compute_it(raw, 1)

def test_day05_part2_example(day05_example_raw): 
    assert day05_part2(day05_example_raw) == 'MCD'

def test_day05_part2(day05_raw): 
    assert day05_part2(day05_raw) == 'GSLCMFBRP'
