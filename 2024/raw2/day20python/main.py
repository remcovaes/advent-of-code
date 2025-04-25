from typing import List, Tuple

Coor = Tuple[int, int]

def up(s: Coor, amount=1):
    return (s[0]-amount, s[1])
def down(s: Coor, amount=1):
    return (s[0]+amount, s[1])
def left(s: Coor, amount=1):
    return (s[0], s[1]-amount)
def right(s: Coor, amount=1):
    return (s[0], s[1]+amount)



def read_file():
    with open("input") as f:
        return f.read()

class MainInput:
    positions: set[Coor]
    start: Coor
    visited: dict[Coor, int]
    cheats: set[tuple[Coor, Coor]]

def parse_input(s: str) -> MainInput:
    main = MainInput()
    main.positions = set()
    main.visited = {}
    main.cheats = set()
    for i, s in enumerate(s.split("\n")):
        for j, b in enumerate(s):
            pos = (int(i), int(j))
            if b == "." or b == "E":
                main.positions.add(pos)
            if b == "S":
                main.positions.add(pos)
                main.visited[pos] = 0
                main.start = pos
    return main


def solve_total_1():
    file = read_file()
    return solver_part1(file, 100, 20)

def solve_total_2():
    file = read_file()
    return solver_part2(file)

def move_step(input, total):
    l = left(input.start)
    r = right(input.start)
    u = up(input.start)
    d = down(input.start)
    moves = [l,r,u,d]
    moved = False
    for m in moves:
        prev = input.visited.get(m)
        if prev != None:
            continue
        if not m in input.positions:
            continue
        moved = True
        total+=1
        input.visited[m] = total
        input.start = m
    return moved, total


def solver_part1(s: str, time_saved: int, cheat_allowed: int):
    input = parse_input(s)
    total = 0
    start = input.start
    while True:
        moved, total = move_step(input, total)
        if not moved:
            break
   
    total_cheats = 0
    c = {}
    for p in input.visited.keys():
        possible_cheats = set()
        for i in range(cheat_allowed +1):
            for j in range(cheat_allowed +1-i):
                x = p[0] + i
                y = p[1] + j
                possible_cheats.add((x,y))
        for i in range(cheat_allowed +1):
            for j in range(cheat_allowed + 1-i):
                x = p[0] - i
                y = p[1] - j
                possible_cheats.add((x,y))
        for i in range(cheat_allowed +1):
            for j in range(cheat_allowed + 1-i):
                x = p[0] + i
                y = p[1] - j
                possible_cheats.add((x,y))
        for i in range(cheat_allowed +1):
            for j in range(cheat_allowed + 1-i):
                x = p[0] - i
                y = p[1] + j
                possible_cheats.add((x,y))
        cheatlist = []
        
        for m in possible_cheats:
            if (p, m) in input.cheats:
                continue
            if m in input.positions:
                cheatlist.append(m)

        for m in cheatlist:
            cheas_secs = abs(m[0] - p[0]) + abs(m[1] - p[1])
            startpos = input.visited[p]
            endpos = input.visited[m]
            cheat_score = (endpos - startpos) 
            saved = cheat_score - cheas_secs
            if  saved >= time_saved:
                input.cheats.add((p, m))
                sav = c.get(saved)
                if sav == None:
                    c[saved] = 0
                c[saved] = c[saved] + 1

                total_cheats += 1

    k = [ i for i in c.keys() ]
    k.sort()
    for i in k:
        print(i, c[i])
    
    return total_cheats

# def solver_part2(s: str):
#     input = parse_input(s)
#     total = 0
#     for i in input.lines:
#         total+=process_single2(i)
#     return total
