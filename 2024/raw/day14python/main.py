from math import floor
import time
from typing import List, Tuple

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
    p: Coor
    v: Coor
    q: int

class MainInput:
    lines: List[SingleInput]
    xlen: int = 101
    ylen: int = 103

def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()
    
    praw, vraw = single.split(" ")
    p1, p2 = praw.split("=")[1].split(",")
    single_input.p = (int(p1), int(p2))

    v1, v2 = vraw.split("=")[1].split(",")
    single_input.v = (int(v1), int(v2))
    return single_input


def parse_input(s: str) -> MainInput:
    main = MainInput()
    main.lines = []
    for line in s.split("\n"):
        if line =="":
            continue
        main.lines.append(parse_single(line))
    return main

def move_robot_seconds(main: MainInput, single: SingleInput, seconds: int) -> int:
    x = (single.p[0] + single.v[0] * seconds) % main.xlen
    y = (single.p[1] + single.v[1] * seconds) % main.ylen
    single.p = (x, y)

    isLeft = x < floor(main.xlen/2)
    isRight = x > floor(main.xlen/2)
    isUp = y < floor(main.ylen/2)
    isDown = y > floor(main.ylen/2)
    single.q = 0
    if isLeft and isUp:
        single.q = 1
    if isLeft and isDown:
        single.q = 2
    if isRight and isUp:
        single.q = 3
    if isRight and isDown:
        single.q = 4


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
    q1 = 0
    q2 = 0 
    q3 = 0
    q4 = 0
    for i in input.lines:
        move_robot_seconds(input, i, 100)
        if i.q == 1:
            q1 +=1
        if i.q == 2:
            q2 +=1
        if i.q == 3:
            q3 +=1
        if i.q == 4:
            q4 +=1
    return q1 * q2 * q3 * q4

def solver_part2(s: str):
    total = 0
    for q in range(1):
        input = parse_input(s)
        print(f"hier round q {q} \n")
        taken = set()
        for i in input.lines:
            move_robot_seconds(input, i, 6587)
            taken.add(i.p)

        time.sleep(.05)
        for i in range(103):
            line = []
            for j in range(101):
                if (i, j) in taken:
                    line.append("#")
                else:
                    line.append(".")
            print(''.join(line))

if __name__ == '__main__':
    solve_total_2()
