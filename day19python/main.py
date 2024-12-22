from typing import List, Tuple
from functools import cache

Coor = Tuple[int, int]

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
    lines: List[SingleInput]
    options: Tuple

def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()

    single_input.single = single

    return single_input


def parse_input(s: str) -> MainInput:
    main = MainInput()
    main.lines = []
    main.options = ()
    splitted = s.split("\n\n")
    for i in splitted[0].split(", "):
        main.options = ( *main.options, i )
    for line in splitted[1].split("\n"):
        if line =="":
            continue
        main.lines.append(parse_single(line))
    return main

@cache
def process_single1(main: tuple, single: str) -> int:
    if single == "":
        return 1
    first_letter = single[0]
    possible_starts = []
    for i in main:
        if not i.startswith(first_letter):
            continue
        if len(i) > len(single):
            continue
        if single[:len(i)] != i:
            continue
        possible_starts.append(i)

    total = 0
    for i in possible_starts:
        remainder = single[len(i):]
        total+= process_single1(main, remainder)
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
    count = 0
    for i in input.lines:
        print(count)
        total+= process_single1(input.options, i.single)
        count+=1
    return total

def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        total+=process_single2(i)
    return total

if __name__ == "__main__":
    print(solve_total_1())
