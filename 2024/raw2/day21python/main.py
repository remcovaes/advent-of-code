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
    code: str
    com: int
    numpad: Coor
    keypad1: Coor
    keypad2: Coor
    keypad3: Coor

class MainInput:
    lines: List[SingleInput]
    numpad_grid: dict[str, Coor]
    keypad_grid: dict[str, Coor]

def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()
    single_input.code =single 
    single_input.numpad = (3,2)
    single_input.keypad1 = (0,2)
    single_input.keypad2 = (0,2)
    single_input.keypad3 = (0,2)
    single_input.com = int(single.split("A")[0])

    return single_input

numpad_grid = {}
numpad_grid["7"] = (0,0) 
numpad_grid["8"] = (0,1) 
numpad_grid["9"] = (0,2) 
numpad_grid["4"] = (1,0) 
numpad_grid["5"] = (1,1) 
numpad_grid["6"] = (1,2) 
numpad_grid["1"] = (2,0) 
numpad_grid["2"] = (2,1) 
numpad_grid["3"] = (2,2) 
numpad_grid["0"] = (3,1) 
numpad_grid["A"] = (3,2) 

keypad_grid = {}
keypad_grid["^"] = (0,1)
keypad_grid["A"] = (0,2)
keypad_grid["<"] = (1,0)
keypad_grid["v"] = (1,1)
keypad_grid[">"] = (1,2)


def parse_input(s: str) -> MainInput:
    main = MainInput()
    main.lines = []
    for line in s.split("\n"):
        if line == "":
            continue
        main.lines.append(parse_single(line))
    main.numpad_grid = {}
    main.numpad_grid["7"] = (0,0) 
    main.numpad_grid["8"] = (0,1) 
    main.numpad_grid["9"] = (0,2) 
    main.numpad_grid["4"] = (1,0) 
    main.numpad_grid["5"] = (1,1) 
    main.numpad_grid["6"] = (1,2) 
    main.numpad_grid["1"] = (2,0) 
    main.numpad_grid["2"] = (2,1) 
    main.numpad_grid["3"] = (2,2) 
    main.numpad_grid["0"] = (3,1) 
    main.numpad_grid["A"] = (3,2) 

    main.keypad_grid = {}
    main.keypad_grid["^"] = (0,1)
    main.keypad_grid["A"] = (0,2)
    main.keypad_grid["<"] = (1,0)
    main.keypad_grid["v"] = (1,1)
    main.keypad_grid[">"] = (1,2)

    return main

def get_coor_offset(a: Coor, b: Coor) -> Coor:
    return (a[0]-b[0], a[1]-b[1])

def get_keypad_input_for_offset(start: Coor, offset: Coor) -> list[list[str]]:
    result: list[list[str]] = []

    wanted1: list[str] = []
    if offset[0] < 0:
        for _ in range(abs(offset[0])):
            wanted1.append("^")
    if offset[0] > 0:
        for _ in range(offset[0]):
            wanted1.append("v")
    if offset[1] > 0:
        for _ in range(offset[1]):
            wanted1.append(">")
    if offset[1] < 0:
        for _ in range(abs(offset[1])):
            wanted1.append("<")
    wanted1.append("A")
    result.append(wanted1)

    wanted2: list[str] = []
    if offset[1] > 0:
        for _ in range(offset[1]):
            wanted2.append(">")
    if offset[1] < 0:
        for _ in range(abs(offset[1])):
            wanted2.append("<")
    if offset[0] > 0:
        for _ in range(offset[0]):
            wanted2.append("v")
    if offset[0] < 0:
        for _ in range(abs(offset[0])):
            wanted2.append("^")
    wanted2.append("A")
    result.append(wanted2)
    return result

def get_keypad_single(offset: Coor, up_first: bool) -> list[str]:
    if up_first:
        wanted1: list[str] = []
        if offset[0] < 0:
            for _ in range(abs(offset[0])):
                wanted1.append("^")
        if offset[0] > 0:
            for _ in range(offset[0]):
                wanted1.append("v")
        if offset[1] > 0:
            for _ in range(offset[1]):
                wanted1.append(">")
        if offset[1] < 0:
            for _ in range(abs(offset[1])):
                wanted1.append("<")
        wanted1.append("A")
        return wanted1 
    wanted1: list[str] = []
    if offset[1] > 0:
        for _ in range(offset[1]):
            wanted1.append(">")
    if offset[1] < 0:
        for _ in range(abs(offset[1])):
            wanted1.append("<")
    if offset[0] > 0:
        for _ in range(offset[0]):
            wanted1.append("v")
    if offset[0] < 0:
        for _ in range(abs(offset[0])):
            wanted1.append("^")
    wanted1.append("A")
    return wanted1

def last_keypard(keys: list[str]):
    pos = (0,2)
    current3 = 0
    for nested2 in keys:
        for key2 in nested2:
            wanted3 = keypad_grid[key2]
            offset = get_coor_offset(wanted3, pos)
            
            keyboard3_presses = get_keypad_input_for_offset(pos, offset)
            current3+=len(keyboard3_presses[0])
            pos = wanted3
    return current3

# @cache
# def get_data(start:Coor, key:str, it: int):
#     if it == 1:
#         wanted = keypad_grid[key]
#         offset = get_coor_offset(wanted, start)
#         keyboard2_presses = get_keypad_single(offset)
#         offset = wanted
#
#         return last_keypard(keyboard2_presses)
#
#     wanted = keypad_grid[key]
#     offset = get_coor_offset(wanted, start)
#     keyboard2_presses = get_keypad_single(offset)
#     total = 0
#     for key in keyboard2_presses:
#         total += get_data(start, key, it-1)
#     return total
#
def get_robot_moves(start: str, target: str) -> list[list[str]]:
    s = keypad_grid[start]
    t = keypad_grid[target]
    offset = get_coor_offset(t, s)
    wanted1: list[str] = []
    if offset[1] > 0:
        for _ in range(offset[1]):
            wanted1.append(">")
    if offset[1] < 0:
        for _ in range(abs(offset[1])):
            wanted1.append("<")
    if offset[0] > 0:
        for _ in range(offset[0]):
            wanted1.append("v")
    if offset[0] < 0:
        for _ in range(abs(offset[0])):
            wanted1.append("^")
    wanted1.append("A")
    wanted2: list[str] = []
    if offset[0] > 0:
        for _ in range(offset[0]):
            wanted2.append("v")
    if offset[0] < 0:
        for _ in range(abs(offset[0])):
            wanted2.append("^")
    if offset[1] > 0:
        for _ in range(offset[1]):
            wanted2.append(">")
    if offset[1] < 0:
        for _ in range(abs(offset[1])):
            wanted2.append("<")
    wanted2.append("A")
    wanted3: list[str] = []
    if offset[0] > 0:
        for _ in range(offset[0]):
            wanted3.append("v")
    if offset[1] > 0:
        for _ in range(offset[1]):
            wanted3.append(">")
    if offset[1] < 0:
        for _ in range(abs(offset[1])):
            wanted3.append("<")
    if offset[0] < 0:
        for _ in range(abs(offset[0])):
            wanted3.append("^")
    wanted3.append("A")
    wanted4: list[str] = []
    if offset[0] < 0:
        for _ in range(abs(offset[0])):
            wanted4.append("^")
    if offset[1] > 0:
        for _ in range(offset[1]):
            wanted4.append(">")
    if offset[1] < 0:
        for _ in range(abs(offset[1])):
            wanted4.append("<")
    if offset[0] > 0:
        for _ in range(offset[0]):
            wanted4.append("v")
    wanted4.append("A")
    p =  [ wanted1,wanted2,wanted3, wanted4]
    
    possible = []
    for i in p:
        numpadpos = s
        pos = True
        for key1 in i:
            if key1 == "<":
                numpadpos = left(numpadpos)
            if key1 == ">":
                numpadpos = right(numpadpos)
            if key1 == "^":
                numpadpos = up(numpadpos)
            if key1 == "v":
                numpadpos = down(numpadpos)
            if numpadpos == (0,0):
                pos = False
                break
        if pos:
            possible.append(i)


    return possible


@cache
def expand_once(start: str, target: str, i: int, up_first:bool) -> int:
    keyssets = get_robot_moves(start, target)
    if i == 1:
        return len(keyssets[0])
    lowest = 99999999999999999999999999999
    for keys in keyssets:
        total = 0
        prev = 'A'
        for k in keys:
            expanded1 = expand_once(prev, k, i-1, True)
            total += expanded1 
            prev = k
        if total < lowest:
            lowest = total

    return lowest

@cache
def get_score(moves: list[str], numpadstart: Coor, robots: int) -> int:
    numpadpos = numpadstart
    for key1 in moves:
        if key1 == "<":
            numpadpos = left(numpadpos)
        if key1 == ">":
            numpadpos = right(numpadpos)
        if key1 == "^":
            numpadpos = up(numpadpos)
        if key1 == "v":
            numpadpos = down(numpadpos)
        if numpadpos == (3,0):
            return 9999999999999999999999 

    s = "A"
    total = 0
    robot_positions = ["A" for i in range(robots)]
    for i, m in enumerate(moves):
        print(moves[i-1])
        l = expand_once(moves[i-1], m,robots, True)
        robot_positions[0] = m
        total = total + l
        s = m

    return total

def process_single1(main: MainInput, single: SingleInput, robots: int) -> tuple[int, int]:
    total = 0
    start = "A"

    for i in single.code:
        start_pos = numpad_grid[start]
        i_pos = numpad_grid[i]
        offset = get_coor_offset(i_pos, start_pos)
        print(i)
        m1 = get_keypad_single(offset, True)
        m2 = get_keypad_single(offset, False)
        start = i

        s1 = get_score(tuple(m1), start_pos, robots)
        s2 = get_score(tuple(m2), start_pos, robots)
        total+= min(s1, s2)
    s = single.com
    return total, s



def process_single2(single: SingleInput) -> int:
    total = 0
    return total

def solve_total_1(robots: int):
    file = read_file()
    return solver_part1(file, robots)

def solve_total_2():
    file = read_file()
    return solver_part2(file)

def solver_part1(s: str, robots: int):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        sub1a, sub1b = process_single1(input, i, robots)

        total+=sub1a * sub1b
    return total

def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        total+=process_single2(i)
    return total

if __name__ == "__main__":
    print('res', solve_total_1(25))


