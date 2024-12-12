
from typing import List, Tuple


def read_file():
    with open("input") as f:
        return f.read()

class SingleInput:
    single: str

class MainInput:
    lines: List[SingleInput] = []

def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()

    single_input.single = single

    return single_input


def parse_input(s: str) -> MainInput:
    main = MainInput()
    for line in s.split("\n"):
        main.lines.append(parse_single(line))
    return main

def process_single2(single: SingleInput) -> int:
    total = 0
    return total

def solve_total_1():
    file = read_file()
    return solver_part1(file)

def solve_total_2():
    file = read_file()
    return solver_part2(file)


class Garden:
    points: set[Tuple[int,int, str]]


def find_area(g: Garden):
    total = 0
    for p in g.points:
        left = 0 if (p[0], p[1]-1, p[2]) in g.points else 1
        top = 0 if (p[0]-1, p[1], p[2])in g.points else 1
        bottom = 0 if (p[0]+1, p[1], p[2])in g.points else 1
        right = 0 if (p[0], p[1]-1, p[2])in g.points else 1
        total = total + left + top + bottom + right
    t = total * len(g.points)
    return t

def has_conn(gardens:dict[Tuple[int,int,str],Garden], points:set[Tuple[int,int,str]], visited:set[Tuple[int,int,str]], p: Tuple[int,int,str]):
    left = (p[0], p[1]-1,p[2])
    right = (p[0], p[1]+1,p[2])
    down = (p[0]-1, p[1],p[2])
    up = (p[0]+1, p[1],p[2])
    
    exists = []
    for i in [left, right, down, up]:
        if i in points:
            if not i in visited:
                exists.append(i)
    if len(exists) == 0:
        return None
    for j in exists:
        g = gardens.get(j)
        if g:
            return g
    for j in exists:
        visited.add(p)
        result = has_conn(gardens, points,visited, j)
        if result != None:
            return result


    

def solver_part1(s: str):
    input = parse_input(s)
    total = 0
    gardens: dict[Tuple[int,int,str],Garden] = {}
    points: set[Tuple[int,int,str]] = set()
    for i, line in enumerate(input.lines):
        for j, letter in enumerate(line.single):
            points.add((i, j, letter))
    for p in points:
        g =  has_conn(gardens, points,set(), p)
        if g is None:
            n = Garden()
            n.points = set()
            n.points.add(p)
            gardens[p] = n
        else:
            g.points.add(p)
            gardens[p] = g

    gs =set(gardens.values())
    for g in gs:
        total = total + find_area(g)

    return total

def up(s: Tuple[int,int, str]):
    return (s[0]-1, s[1], s[2])
def down(s: Tuple[int,int, str]):
    return (s[0]+1, s[1], s[2])
def left(s: Tuple[int,int, str]):
    return (s[0], s[1]-1, s[2])
def right(s: Tuple[int,int, str]):
    return (s[0], s[1]+1, s[2])


def find_area2(g: Garden):
    totaltotal = 0
    for p in g.points:
        l = left(p)
        hasLeft = l in g.points
        u = up(p)
        hasTop = u in g.points
        d = down(p)
        hasBot = d in g.points
        r = right(p)
        hasRight = r in g.points
        topleft = up(left(p))
        topright = up(right(p))
        downleft = down(left(p))
        downright = down(right(p))
        total = 0
        if not hasTop:
            if topleft in g.points or not hasLeft:
                total = total + 0.5
            if topright in g.points or not hasRight:
                total = total + 0.5
        if not hasRight:
            if topright in g.points or not hasTop:
                total = total + 0.5
            if downright in g.points or not hasBot:
                total = total + 0.5
        if not hasLeft:
            if topleft in g.points or not hasTop:
                total = total + 0.5
            if downleft in g.points or not hasBot:
                total = total + 0.5
        if not hasBot:
            if downright in g.points or not hasRight:
                total = total + 0.5
            if downleft in g.points or not hasLeft:
                total = total + 0.5
        totaltotal = totaltotal + total
    t = totaltotal * len(g.points)
    return t

def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    gardens: dict[Tuple[int,int,str],Garden] = {}
    points: set[Tuple[int,int,str]] = set()
    for i, line in enumerate(input.lines):
        for j, letter in enumerate(line.single):
            points.add((i, j, letter))
    for p in points:
        g =  has_conn(gardens, points,set(), p)
        if g is None:
            n = Garden()
            n.points = set()
            n.points.add(p)
            gardens[p] = n
        else:
            g.points.add(p)
            gardens[p] = g

    gs =set(gardens.values())
    for g in gs:
        total = total + find_area2(g)

    return total

