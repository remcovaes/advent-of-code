
from typing import List, Tuple

type Coor = Tuple[int, int]

def up(s: Coor):
    return (s[0]-1, s[1])
def down(s: Coor):
    return (s[0]+1, s[1])
def left(s: Coor):
    return (s[0], s[1]-1)
def right(s: Coor):
    return (s[0], s[1]+1)



def read_file():
    with open("input") as f:
        return f.read()

class SingleInput:
    single: str

class MainInput:
    lines: List[SingleInput] = []

def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()

    single_input.single = single

    return single_input


def parse_input(s: str) -> MainInput:
    main = MainInput()
    for line in s.split("\n"):
        main.lines.append(parse_single(line))
    return main

def process_single1(single: SingleInput) -> int:
    total = 0
    return total


def process_single2(single: SingleInput) -> int:
    total = 0
    return total

def solve_total_1():
    file = read_file()
    return solver_part1(file)

def solve_total_2():
    file = read_file()
    return solver_part2(file)

def solver_part1(s: str):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        total+=process_single1(i)
    return total

def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        total+=process_single2(i)
    return total
