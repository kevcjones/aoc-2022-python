

elf_calories = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def convert_raw_to_lists_of_ints(lines_with_gaps):
    lines_with_gaps = lines_with_gaps.strip()
    list_lists = [line for line in lines_with_gaps.split("\n\n")]
    int_lists = [list(map(int, str_lists.split("\n"))) for str_lists in list_lists]
    return int_lists

# Solution

def day01_part1(calories_lists_raw):
    calories_lists = convert_raw_to_lists_of_ints(calories_lists_raw)
    highest_sum = max([sum(calory_list) for calory_list in calories_lists])
    return highest_sum

def day01_part2(calories_lists_raw):
    calories_lists = convert_raw_to_lists_of_ints(calories_lists_raw)
    calories_summed = [sum(calory_list) for calory_list in calories_lists]
    return sum(sorted(calories_summed, reverse=True)[:3])

# Tests

def test_day01_part1_example1(): 
    assert day01_part1(elf_calories) == 24000

def test_day01_part2_example1(): 
    assert day01_part2(elf_calories) == 45000

def test_day01_part1(day01_raw): assert day01_part1(day01_raw) == 67016
def test_day01_part2(day01_raw): assert day01_part2(day01_raw) == 200116
