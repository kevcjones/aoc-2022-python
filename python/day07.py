import pytest
from functools import reduce
from utils.examples import read_raw_example_for_day

@pytest.fixture
def day07_example_raw():
    return read_raw_example_for_day(7)


# Common utils

def convert_to(raw, converter = lambda x: int(x)):
    raw = raw.strip()
    casted = [converter(line) for line in raw.split("\n")]
    return casted

    
def build_file_list(result, ins):
    if(ins[0] == '$'):
        # if ins string contains cd
        if(ins[2] == 'c'):
            dir = ins.split(' ')[-1]
            if(dir == '/'):
                result['current'] = ['/']
            elif dir == '..':
                result['current'].pop()
            else:
                result['current'].append(dir+'/')
    else:
        info,name = ins.split(' ')
        if info == 'dir':
            path = ''.join(result['current'])+name+'/'
            result["dir"][path] = {"key":path, "size": 0}
        else:
            path = ''.join(result['current'])+name
            result['dir'][path] = {"key":path, "size": int(info)}
    return result

def calculate_folder_size(paths):
    for path in paths['dir']:
        if(paths['dir'][path]['key'][-1] == '/') and (paths['dir'][path]['size'] == 0):
            size = 0
            for k in paths['dir']:
                if(k.startswith(path) and paths['dir'][k]['key'][-1] != '/'):
                    size += int(paths['dir'][k]['size'])
            paths['dir'][path]['size'] = size
    return paths  

def get_only_folders_in_size_order(output):
    all_by_size = sorted(output['dir'].values(), key=lambda x: x['size'], reverse=False)
    folders = [x for x in all_by_size if x['key'][-1] == '/']
    return folders


def get_folders_by_size(instructions):
    files = {"current": [], "dir":{'/': {"key":"/", "size": 0}}}
    all_files = reduce(build_file_list, instructions, files)
    all_files_sized = calculate_folder_size(all_files)
    return get_only_folders_in_size_order(all_files_sized)


def day07_part1(raw):
    instructions = convert_to(raw, lambda x: str(x))
    folders = get_folders_by_size(instructions)

    # Add up folders until we go over 100000
    sum = 0
    for i in range(len(folders)):
        if(folders[i]['size'] < 100000):
            sum += folders[i]['size']

    return sum

def day07_part2(raw):
    instructions = convert_to(raw, lambda x: str(x))
    folders = get_folders_by_size(instructions)

    # find the first folder that will free up enough space
    target = 30000000
    space = 70000000
    remaining = space - int(folders[-1]['size'])
    for i in range(len(folders)):
        if(folders[i]['size'] + remaining > target):
            return folders[i]['size']



def test_day07_part1_example(day07_example_raw): 
    assert day07_part1(day07_example_raw) == 95437

def test_day07_part1(day07_raw): 
    assert day07_part1(day07_raw) == 1491614

def test_day07_part2_example(day07_example_raw): 
    assert day07_part2(day07_example_raw) == 24933642

def test_day07_part2(day07_raw): 
    assert day07_part2(day07_raw) == 6400111
