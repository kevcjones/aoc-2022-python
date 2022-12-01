from os import path

def read_raw_example_for_day(day_number):
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, f'../../input/day{day_number:02}-example.txt')
    with open(file_path) as f:
        return f.read()