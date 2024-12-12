
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
    points: List[Tuple[int,int, str]]


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

def solver_part1(s: str):
    input = parse_input(s)
    total = 0
    gardens: List[Garden] = []
    for i, line in enumerate(input.lines):
        for j, letter in enumerate(line.single):
            leftLetter = input.lines[i].single[j-1] if j-1 >=0 and j-1 < len(line.single) else "@"
            upLetter = input.lines[i-1].single[j]if i-1 >=0 else "@"

            l = len(line.single)
            rightLetter = input.lines[i].single[j+1] if j+1 < l else "@"

            if letter == leftLetter or letter == upLetter or rightLetter == letter:
                append = False
                for ga in gardens:
                    if (i-1, j, letter) in ga.points or (i, j-1, letter) in ga.points or (i, j+1, letter) in ga.points:
                        append = True
                        ga.points.append((i,j, letter))
                        break
                    if letter == rightLetter:
                        ind2 = 1
                        while True:
                            if j-1 <0:
                                break
                            if i+ind2 >= len(input.lines):
                                break
                            botLeft= input.lines[i+ind2].single[j-1] 
                            bot = input.lines[i+ind2].single[j]
                            if bot != letter:
                                break
                            if botLeft == letter:
                                while True:
                                    
                            
                            ind2 = ind2 + 1
                        ind = 1
                        while True:
                            if i-1 <0:
                                break
                            if j+ind >= len(line.single):
                                break
                            topRight = input.lines[i-1].single[j+ind] 
                            rLetter = input.lines[i].single[j+ind]
                            if rLetter != letter:
                                break
                            if topRight == letter and rLetter == letter:
                                if (i-1, j+ind, letter) in ga.points:
                                    append = True
                                    ga.points.append((i,j, letter))
                                    break
                            
                            ind = ind + 1


                if append:
                    continue
            g = Garden()
            g.points = [ (i,j, letter) ]
            gardens.append(g)

    for g in gardens:
        total = total + find_area(g)

    return total

def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        total+=process_single2(i)
    return total
