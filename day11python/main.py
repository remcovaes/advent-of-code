from functools import lru_cache 
from typing import List


def read_file():
    with open("input") as f:
        return f.read()

class SingleInput:
    single: int

class MainInput:
    lines: List[int] = []

def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()

    single_input.single = int(single)

    return single_input


def parse_input(s: str) -> MainInput:
    main = MainInput()
    m = s.strip("\n")
    for line in m.split(" "):
        main.lines.append(int(line))
    return main


cache = {}

@lru_cache(maxsize=12800)
def process_single1(single) -> int:
    if single[1] == 0:
        return 1
    current = single
    todo = []
    total = 1
    while current[1] > 0:
        if current[0] == 0:
            current = (1, current[1] - 1)
            continue
        s = str(current[0])
        if len(s) % 2 == 0:
            slice = int(len(s) / 2) 
            strnum =s[:slice] 
            current = (int(strnum), current[1] -1)
            todo.append((int(s[(slice):]), current[1]))
        else:
            current = (current[0] * 2024, current[1] -1)
    for i in todo:
        total = total + process_single1(i)
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
        total+=process_single1((i, 75))
    return total

def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        total+=process_single2(i, 5)
    return total

#print("result: ", solve_total_1())
