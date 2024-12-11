
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

def process_single1(single: int) -> int:
    c = cache.get(single)
    if c != None:
        print('cache hit')
        return c

    print('cache miss', cache)
    currentList = [single]
    for i in range(25):
        print(i)
        temp: List[int] = []
        for j in range(len(currentList)):
            num = currentList[j]
            if num == 0:
                temp.append(1)
                continue
            s = str(num)
            if len(s) % 2 == 0:
                slice = int(len(s) / 2) 
                strnum =s[:slice] 
                temp.append(int(strnum))
                temp.append(int(s[(slice):]))
            else:
                temp.append(num * 2024)
        currentList = temp

    cache[single] = len(currentList)        
    return len(currentList)


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

print("result: ", solve_total_1())
