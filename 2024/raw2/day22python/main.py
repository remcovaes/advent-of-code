from typing import List, Tuple
from functools import cache
import sys
sys.setrecursionlimit(5000)
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
    single: int

class MainInput:
    lines: List[SingleInput]

def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()

    single_input.single = int(single)

    return single_input


def parse_input(s: str) -> MainInput:
    main = MainInput()
    main.lines = []
    for line in s.split("\n"):
        if line == "":
            continue
        main.lines.append(parse_single(line))
    return main

@cache
def get_num(num: int):
    secret = num

    num = secret * 64
    mix_num = num ^ secret
    tota_first = mix_num % 16777216

    div = tota_first // 32
    total_sec = div ^ tota_first 
    total_sec_pruned= total_sec % 16777216

    sec = total_sec_pruned * 2048
    new_sec = sec ^ total_sec_pruned
    return new_sec % 16777216

def get_next(num: int, it:int):
    if it == 0:
        return num
   
    total = get_num(num)

    return get_next(total, it-1)

def get_diffs_for(sec: int):
    num1 = sec
    num2 = get_num(num1)
    num3 = get_num(num2)
    num4 = get_num(num3)
    num5 = get_num(num4)

    last_digit = [num1 % 10, num2 % 10, num3 % 10, num4 % 10, num5 % 10]
    diffs = [last_digit[i+1] - last_digit[i] for i in range(4)]
    score = num5 % 10
    return (diffs[0], diffs[1], diffs[2], diffs[3]), score

scores = {}
def process_single1(single: SingleInput) -> int:
    diffset = set()
    for i in range(1997):
        diffs, score = get_diffs_for(get_next(single.single, i))
        if diffs in diffset:
            continue
        diffset.add(diffs)
        old_score = scores.get(diffs)
        if old_score is None:
            scores[diffs] = score
        else:
            scores[diffs] = old_score + score
    return 0


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
    j = 0
    for i in input.lines:
        j+=1
        print(j)
        total+=process_single1(i)
    for k, v in scores.items():
        if v > total:
            total = v
    return total

def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        total+=process_single2(i)
    return total

if __name__ == "__main__":
    print(solve_total_1())
