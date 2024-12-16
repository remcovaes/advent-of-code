from typing import List, Tuple

Coor = Tuple[int, int]
Box = Tuple[int, int, str]

def up(s: Coor):
    return (s[0]-1, s[1])
def down(s: Coor):
    return (s[0]+1, s[1])
def left(s: Coor):
    return (s[0], s[1]-1)
def right(s: Coor):
    return (s[0], s[1]+1)

def upb(s: Box):
    return (s[0]-1, s[1], s[2])
def downb(s: Box):
    return (s[0]+1, s[1], s[2])
def leftb(s: Box):
    return (s[0], s[1]-1, s[2])
def rightb(s: Box):
    return (s[0], s[1]+1, s[2])





def read_file():
    with open("input") as f:
        return f.read()

class SingleInput:
    single: str

class MainInput:
    lines: List[SingleInput]
    robot_pos: Coor
    boxes: set[Box]
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
                main.walls.add((i,j *2))
                main.walls.add((i ,j * 2 + 1))
            if s == "O":
                main.boxes.add((i,j * 2, "A"))
                main.boxes.add((i,j * 2 + 1, "B"))
            if s == "@":
                main.robot_pos = (i,j * 2)

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

def move_box(c: Box, s: str):
    if s == ">":
        return rightb(c)
    if s == "<":
        return leftb(c)
    if s == "^":
        return upb(c)
    if s == "v":
        return downb(c)
    raise Exception("invalid move")


def process_single1(main: MainInput, single: SingleInput):
    move = single.single
    next_pos = move_robot(main.robot_pos, move)
    if next_pos in main.walls:
        return
    a_box = (*next_pos, "A")
    b_box = (*next_pos, "B")
    if not a_box in main.boxes and not b_box in main.boxes:
        main.robot_pos = next_pos
        return

    boxes_to_move = set()
    boxes_to_move = set()

    boxes_moved = set()

    robot_pos = main.robot_pos
    while True:
        robot_pos = move_robot(robot_pos, move)
        start = len(boxes_to_move)
        boxes_to_check = set()
        for b in boxes_to_move:
            boxes_to_check.add(move_robot((b[0], b[1]), move))

        if len(boxes_to_check) == 0:
            boxes_to_check.add(robot_pos)
        for box_to_check in boxes_to_check:
            a_box = (*box_to_check, "A")
            b_box = (*box_to_check, "B")
            if (a_box in main.boxes) and move != "<":
                hit_a = a_box
                hit_b = (hit_a[0], hit_a[1] + 1, "B")
                boxes_to_move.add(hit_a)
                boxes_to_move.add(hit_b)
                boxes_moved.add(move_box(hit_a, move))
                boxes_moved.add(move_box(hit_b, move))
            if (b_box in main.boxes) and move != ">":
                hit_b = b_box
                hit_a = (hit_b[0], hit_b[1] - 1, "A")
                boxes_to_move.add(hit_a)
                boxes_to_move.add(hit_b)
                boxes_moved.add(move_box(hit_a, move))
                boxes_moved.add(move_box(hit_b, move))
        if start == len(boxes_to_move):
            break
        
    for b in boxes_moved:
        wall = (b[0], b[1])
        if wall in main.walls:
            return

    for b in boxes_to_move:
        if b in main.boxes:
            main.boxes.remove(b)
    for b in boxes_moved:
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
        if box[2] == "A":
            total = total + box[0] * 100 + box[1]
    return total

def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        total+=process_single2(i)
    return total

if __name__ == "__main__":
    print(solve_total_1())
