from os import stat_result
from typing import List, Tuple, Dict
from enum import Enum

Dir = Enum('Dir', [('NORTH', 1), ('EAST', 2), ('SOUTH', 3), ('WEST', 4)])

CoorDir = Tuple[int, int, Dir]
Coor = Tuple[int, int]

def up(s: CoorDir):
    return (s[0]-1, s[1], s[2])
def down(s: CoorDir):
    return (s[0]+1, s[1], s[2])
def left(s: CoorDir):
    return (s[0], s[1]-1, s[2])
def right(s: CoorDir):
    return (s[0], s[1]+1, s[2])


def turn_left(s: CoorDir):
    if s[2] == Dir.NORTH:
        return (s[0], s[1], Dir.EAST)
    if s[2] == Dir.EAST:
        return (s[0], s[1], Dir.SOUTH)
    if s[2] == Dir.SOUTH:
        return (s[0], s[1], Dir.WEST)
    if s[2] == Dir.WEST:
        return (s[0], s[1], Dir.NORTH)

def turn_right(s: CoorDir):
    if s[2] == Dir.NORTH:
        return (s[0], s[1], Dir.WEST)
    if s[2] == Dir.EAST:
        return (s[0], s[1], Dir.NORTH)
    if s[2] == Dir.SOUTH:
        return (s[0], s[1], Dir.EAST)
    if s[2] == Dir.WEST:
        return (s[0], s[1], Dir.SOUTH)


def read_file():
    with open("input") as f:
        return f.read()

class SingleInput:
    single: str

class MainInput:
    start: CoorDir
    walls: set[Coor]
    visited: Dict[CoorDir, Tuple[int, set[Coor]]]
    path: set[Coor]
    finish: Coor

def parse_input(s: str) -> MainInput:
    main = MainInput()
    main.walls = set()
    main.visited = {}
    main.path = set()

    j = 0
    for line in s.split("\n"):
        i = 0
        for letter in line:
            if letter == "#":
                main.walls.add((j, i))
            if letter == "S":
                main.start = (j, i, Dir.EAST)
            if letter == ".":
                main.path.add((j, i))
            if letter == "E":
                main.finish = (j,i)
                main.path.add((j, i))
            i+=1
        j+=1
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

def get_dir_from_current(start: CoorDir, p: Coor) -> Dir:
    if p[0] > start[0]:
        return Dir.SOUTH
    if p[0] < start[0]:
        return Dir.NORTH
    if p[1] > start[1]:
        return Dir.EAST
    if p[1] < start[1]:
        return Dir.WEST
    raise Exception("not found")

def solver_part1(s: str):
    input = parse_input(s)
    start_set: set[Coor] = set()
    start_set.add((input.start[0], input.start[1]))
    input.visited[input.start] = (0, start_set)
    changed = False
    scores = []
    while True:
        for position, m in input.visited.copy().items():
            score = m[0]
            v = m[1]
            possible_next_points = [
                left(position),
                right(position),
                up(position),
                down(position)
            ]
            point = [(point[0], point[1]) for point in possible_next_points if (point[0], point[1]) in input.path]
            for p in point:
                new_dir = get_dir_from_current(position, p)
                turns = 0
                if new_dir != position[2]:
                    turns = 1
                    if new_dir == Dir.SOUTH and position[2] == Dir.NORTH:
                        turns = 2
                    if new_dir == Dir.NORTH and position[2] == Dir.SOUTH:
                        turns = 2
                    if new_dir == Dir.EAST and position[2] == Dir.WEST:
                        turns = 2
                    if new_dir == Dir.WEST and position[2] == Dir.EAST:
                        turns = 2
                new_pos = (*p, new_dir)
                prev = input.visited.get(new_pos)
                new_score = turns * 1000 + 1 + score
                if prev == None or prev[0] > new_score:
                    new_set = set(v)
                    new_set.add(p)
                    input.visited[new_pos] = (new_score, new_set)
                    changed = True
                if prev != None and prev[0] == new_score:
                    new_set = set(v)
                    for i in prev[1]:
                        new_set.add(i)
                    input.visited[new_pos] = (new_score, new_set)
                if p == input.finish:
                    scores.append(input.visited[new_pos])
        if not changed:
            break
        changed = False
    lowest = (999999999999999999,)
    for i in scores:
        if i[0] < lowest[0]:
            lowest = i
    return len(lowest[1])

def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        total+=process_single2(i)
    return total
