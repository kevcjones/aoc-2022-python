import pytest
from utils.examples import read_raw_example_for_day

@pytest.fixture
def day05_example_raw():
    return read_raw_example_for_day(5)


def get_crates_and_moves(raw):
    crates_raw,moves_raw = raw.split('\n\n')
    return crates_raw,moves_raw

def get_rows_of_crate_letters(crates_raw):
    crates_rows = [crate_letter[1::4] for crate_letter in crates_raw.split('\n')[:-1]]
    return crates_rows

def transpose_to_stack_lists(crates_rows):
    stacks = ["".join([stack[crate] for stack in crates_rows]).strip() for crate in range(len(crates_rows[0]))]
    return stacks

def parse_move_instructions(moves_raw):
    moves = [list(map(int, move.split()[1::2])) for move in moves_raw.split('\n') if move]
    return moves

def compute_it(raw, order=-1):
    crates_raw, moves_raw = get_crates_and_moves(raw)
    crates_rows = get_rows_of_crate_letters(crates_raw)
    stacks = transpose_to_stack_lists(crates_rows)
    moves = parse_move_instructions(moves_raw)
    for mv in moves:
        count = mv[0]
        from_stack = mv[1] - 1
        to_stack = mv[2] - 1
        # slice and splice
        stacks[to_stack] = stacks[from_stack][:count][::order] + stacks[to_stack]
        stacks[from_stack] = stacks[from_stack][count:]
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
