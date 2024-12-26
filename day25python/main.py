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

class MainInput:
    keys: List[list[int]]
    locks: List[list[int]]

def parse_input(s: str) -> MainInput:
    main = MainInput()
    main.keys = []
    main.locks = []
    for line in s.split("\n\n"):
        rows = line.split("\n")
        is_lock = False
        for i in rows[0]:
            if i != "#":
                is_lock = False
                continue
            is_lock = True

        count = [-1,-1,-1,-1,-1]
        for r in rows:
            for c, i in enumerate(r):
                if i == "#":
                    count[c] += 1
        if is_lock:
            main.locks.append(count)
        else:
            main.keys.append(count)


    return main


def solve_total_1():
    file = read_file()
    return solver_part1(file)

def solver_part1(s: str):
    input = parse_input(s)
    total = 0

    for lock in input.locks:
        for key in input.keys:
            if lock[0] + key[0] > 5:
                continue
            if lock[1] + key[1] > 5:
                continue
            if lock[2] + key[2] > 5:
                continue
            if lock[3] + key[3] > 5:
                continue
            if lock[4] + key[4] > 5:
                continue
            total+=1
            
    return total


