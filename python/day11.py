import pytest
from utils.examples import read_raw_example_for_day
import re


@pytest.fixture
def day11_example_raw():
    return read_raw_example_for_day(11)

monkey_id_parser = re.compile(r'^Monkey (\d+):$')

class Monkey:
    starting_items_re = re.compile(r'^ {2}Starting items: (\d+(?:, \d+)*)$')
    worry_op_re = re.compile(r'^ {2}Operation: new = (old [*+] (?:old|\d+))$')
    divisible_re = re.compile(r'^ {2}Test: divisible by (\d+)$')
    throw_to_re = re.compile(r'^ {4}If (true|false): throw to monkey (\d+)$')
    divisor_product = 1

    def __init__(self):
        self.items = []
        self.worry_op = ''
        self.test_divisor = 1
        self.catchers = {
            "true": 0,
            "false": 0
        }
        self.inspected = 0

    def parse(self, text_block):
        lines = text_block.split('\n')

        # get a list of starting items
        self.items = [int(x) for x in Monkey.starting_items_re.match(lines.pop(1)).group(1).split(', ')]
        
        # parse the worry operation
        self.worry_op = Monkey.worry_op_re.match(lines.pop(1)).group(1)

        # parse the test divisor used to decide which catcher to throw to
        self.test_divisor = int(Monkey.divisible_re.match(lines.pop(1)).group(1))
        
        # build a common divisor by multiplying all the test divisors
        Monkey.divisor_product *= self.test_divisor 

        # parse the catchers
        for _ in range(2):
            truth_value, destination_monkey = Monkey.throw_to_re.match(lines.pop(1)).groups()
            self.catchers[truth_value] = int(destination_monkey)

    def inspect_items(self, all_monkeys, ease_worry=True):
        for item in self.items:
            # cause worry
            worry = self.cause_worry(ease_worry, item)
            
            # throw the item to the next monkey
            self.throw_item(all_monkeys, worry)

            # count the inspections
            self.inspected += 1
        self.items = []

    def cause_worry(self, ease_worry, old):

        # cause worry - eval 🤮
        worry = eval(self.worry_op)            
        
        # dampen the worry
        if ease_worry:
            worry //= 3

        # make sure the worry is not too big
        # stops us from exceeding the max int size
        if worry > Monkey.divisor_product:
            worry = worry % Monkey.divisor_product
        return worry

    def throw_item(self, all_monkeys, worry):
        is_divisible = ((worry % self.test_divisor) == 0)
        catcher_monkey = self.catchers[str(is_divisible).lower()]
        all_monkeys[catcher_monkey].catch_item(worry)

    def catch_item(self, item):
        self.items.append(item)

def day11_part1(raw):
    raw_monkeys = raw.split('\n\n')
    monkeys = []
    for raw_monkey in raw_monkeys:
        monkey = Monkey()
        monkey.parse(raw_monkey)
        monkeys.append(monkey)

    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect_items(monkeys, ease_worry=True)
    
    clepto_rankings = sorted(monkeys, reverse=True, key=lambda x: x.inspected)[:2]
    return clepto_rankings[0].inspected * clepto_rankings[1].inspected


def day11_part2(raw):
    monkeys = []
    raw_monkeys = raw.split('\n\n')

    for raw_monkey in raw_monkeys:
        monkey = Monkey()
        monkey.parse(raw_monkey)
        monkeys.append(monkey)

    for _ in range(10000):
        for monkey in monkeys:
            monkey.inspect_items(monkeys, ease_worry=False)
    
    clepto_rankings = sorted(monkeys, reverse=True, key=lambda x: x.inspected)[:2]
    return clepto_rankings[0].inspected * clepto_rankings[1].inspected

# tests

def test_day11_part1_example(day11_example_raw): 
    assert day11_part1(day11_example_raw) == 10605
    
def test_day11_part1(day11_raw): 
    assert day11_part1(day11_raw) == 64032

def test_day11_part2_example(day11_example_raw): 
    assert day11_part2(day11_example_raw) == 2713310158 

def test_day11_part2(day11_raw): 
    assert day11_part2(day11_raw) ==  12729522272
