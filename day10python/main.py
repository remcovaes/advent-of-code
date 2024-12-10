
from typing import List


def read_file():
    with open("input") as f:
        return f.read()

class Coor:
    x: int
    y: int
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Coor):
            return self.x == other.x and self.y == other.y
        return False

class MainInput:
    lines: List[List[int]] = []
    possibleTrailHeads: List[Coor] = []



def parse_input(s: str) -> MainInput:
    main = MainInput()
    for y, line in enumerate(s.split("\n")):
        parsed = line.split()
        current = []
        for x, letter in enumerate(parsed[0]):
            num = int(letter) if letter != "." else 8
            current.append(num)
            if num == 0:
                coor = Coor(x,y)
                main.possibleTrailHeads.append(coor)
        main.lines.append(current)
    return main

def handleTrailHead(main: MainInput, coor: Coor, height: int):
    if height == 9:
        s = set()
        s.add((coor.x, coor.y))
        return s

    maxY = len(main.lines)
    maxX = len(main.lines[0])

    nextPossibleCoords = [
        Coor(coor.x-1,coor.y),
        Coor(coor.x,coor.y-1),
        Coor(coor.x+1,coor.y),
        Coor(coor.x,coor.y+1),
    ]

    nextCoords = []
    for c in nextPossibleCoords:
        if c.x < 0 or c.x >= maxX:
            continue
        if c.y < 0 or c.y >= maxY:
            continue
        newHeight = main.lines[c.y][c.x]
        if newHeight != (height + 1):
            continue
        nextCoords.append(c)
    total = set()
    for i in nextCoords:
        newHeight = height + 1
        newset =  handleTrailHead(main, i, newHeight)
        for i in newset:
            total.add(i)
    return total

def handleTrailHeadB(main: MainInput, coor: Coor, height: int):
    if height == 9:
        return 1

    maxY = len(main.lines)
    maxX = len(main.lines[0])

    nextPossibleCoords = [
        Coor(coor.x-1,coor.y),
        Coor(coor.x,coor.y-1),
        Coor(coor.x+1,coor.y),
        Coor(coor.x,coor.y+1),
    ]

    nextCoords = []
    for c in nextPossibleCoords:
        if c.x < 0 or c.x >= maxX:
            continue
        if c.y < 0 or c.y >= maxY:
            continue
        newHeight = main.lines[c.y][c.x]
        if newHeight != (height + 1):
            continue
        nextCoords.append(c)
    total = 0
    for i in nextCoords:
        newHeight = height + 1
        total += handleTrailHeadB(main, i, newHeight)
    return total



def process_single1(single: MainInput) -> int:
    total = 0
    for i in single.possibleTrailHeads:
        total+=len(handleTrailHead(single, i, 0))
    return total


def process_single2(single: MainInput) -> int:
    total = 0
    for i in single.possibleTrailHeads:
        total+=handleTrailHeadB(single, i, 0)
    return total

def solve_total_1():
    file = read_file()
    return solver_part1(file.strip("\n"))

def solve_total_2():
    file = read_file()
    return solver_part2(file.strip("\n"))

def solver_part1(s: str):
    input = parse_input(s)
    total=process_single1(input)
    return total

def solver_part2(s: str):
    input = parse_input(s)
    total=process_single2(input)
    return total
