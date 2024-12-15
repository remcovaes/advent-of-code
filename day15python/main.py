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
    single: str

class MainInput:
    lines: List[SingleInput]
    robot_pos: Coor
    boxes: set[Coor]
    walls: set[Coor]

def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()

    single_input.single = single

    return single_input


def parse_input(s: str) -> MainInput:
    main = MainInput()
    main.lines = []
    main.boxes = set()
    main.walls = set()
    splitted = s.split("\n\n")
    for i, item in enumerate(splitted[0].split("\n")):
        items = item
        for j, s in enumerate(items):
            if s == "#":
                main.walls.add((i,j))
            if s == "O":
                main.boxes.add((i,j))
            if s == "@":
                main.robot_pos = (i,j)

    s = splitted[1].replace("\n", "")
    for n in s:
        for line in n.split():
            main.lines.append(parse_single(line))
    return main

def move_robot(c: Coor, s: str):
    if s == ">":
        return right(c)
    if s == "<":
        return left(c)
    if s == "^":
        return up(c)
    if s == "v":
        return down(c)
    raise Exception("invalid move")

def process_single1(main: MainInput, single: SingleInput):
    move = single.single
    next_pos = move_robot(main.robot_pos, move)
    if next_pos in main.walls:
        return
    if not next_pos in main.boxes:
        main.robot_pos = next_pos
        return

    boxes_to_move = []
    boxes_moved = []
    next_box = next_pos
    while True:
        boxes_moved.append(next_box)
        next_box = move_robot(next_box, move)
        boxes_to_move.append(next_box)
        if next_box in main.walls:
            return
        if next_box not in main.boxes:
            break
    for b in boxes_moved:
        main.boxes.remove(b)
    for b in boxes_to_move:
        main.boxes.add(b)
    main.robot_pos = next_pos




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
        process_single1(input, i)
    for box in input.boxes:
        total = total + box[0] * 100 + box[1]
    return total

def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        total+=process_single2(i)
    return total
