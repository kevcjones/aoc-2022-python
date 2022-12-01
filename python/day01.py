

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

def parse_raw_into_list_of_int_lists(lines_with_gaps):
    lines_with_gaps = lines_with_gaps.strip()
    list_lists = [line for line in lines_with_gaps.split("\n\n")]
    int_lists = [list(map(int, str_lists.split("\n"))) for str_lists in list_lists]
    return int_lists


def day01a(elf_calories_raw):
    elf_calories_list = parse_raw_into_list_of_int_lists(elf_calories_raw)
    highest_count = max([sum(calory_list) for calory_list in elf_calories_list])
    return highest_count

def day01b(elf_calories_raw):
    elf_calories_list = parse_raw_into_list_of_int_lists(elf_calories_raw)
    counts = [sum(calory_list) for calory_list in elf_calories_list]
    return sum(sorted(counts, reverse=True)[:3])

def test_01a_ex0(): 
    assert day01a(elf_calories) == 24000

def test_01b_ex0(): 
    assert day01b(elf_calories) == 45000

def test_01a(day01_raw): assert day01a(day01_raw) == 67016
def test_01b(day01_raw): assert day01b(day01_raw) == 200116
