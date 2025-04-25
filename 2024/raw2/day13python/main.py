from math import ceil, floor
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
    button_a: Coor
    button_b: Coor
    price: Coor


class MainInput:
    lines: List[SingleInput] = []

def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()
    lines = single.split('\n')
    a = lines[0]
    b = lines[1]
    price = lines[2]

    ax, ay = a.split(":")[1].strip(" ").split(", ")
    anumx = int(ax.split("+")[1])
    anumy = int(ay.split("+")[1])

    single_input.button_a = (anumx, anumy)

    bx, by = b.split(":")[1].strip(" ").split(", ")
    bnumx = int(bx.split("+")[1])
    bnumy = int(by.split("+")[1])

    single_input.button_b = (bnumx, bnumy)
    
    bx, by = price.split(":")[1].strip(" ").split(", ")
    px = int(bx.split("=")[1])
    py = int(by.split("=")[1])
    single_input.price = (10000000000000 + px,10000000000000 + py)


    return single_input


def parse_input(s: str) -> MainInput:
    main = MainInput()
    for line in s.split("\n\n"):
        main.lines.append(parse_single(line))
    return main

def move_b_back(single: SingleInput, x=1):
    single.price = (
        single.price[0] + single.button_b[0] * x,
        single.price[1] + single.button_b[1] * x
    )
def move_a_back(single: SingleInput, x=1):
    single.price = (
        single.price[0] + single.button_a[0] * x,
        single.price[1] + single.button_a[1] * x
    )

def move_b(single: SingleInput, x=1):
    single.price = (
        single.price[0] - single.button_b[0] * x,
        single.price[1] - single.button_b[1] * x
    )
def move_a(single: SingleInput, x=1):
    single.price = (
        single.price[0] - single.button_a[0] * x,
        single.price[1] - single.button_a[1] * x
    )

def find_least_move_a(r: SingleInput):
    single = SingleInput()
    single.button_a = (r.button_a[0], r.button_a[1])
    single.button_b = (r.button_b[0], r.button_b[1])
    single.price = (r.price[0], r.price[1])

    stepsA = 0
    stepsB = 0
    reached = False
    while(single.price != (0, 0)):
        if stepsA < 0:
            return (-1, -1)
        has_neg = single.price[0] < 0 or single.price[1] < 0
        if (has_neg or reached):
            reached = True
            move_a_back(single)
            stepsA-=1
            try_b = 0
            while(single.price[0] > 0 and single.price[1] > 0):
                move_b(single)
                try_b+=1

                if single.price == (0, 0):
                    return (stepsA, try_b)
            for j in range(try_b):
                move_b_back(single)
            
        else:
            move_a(single)
            stepsA+=1
    
    return (stepsA, stepsB)
        

def find_least_move_b(r: SingleInput):
    single = SingleInput()
    single.button_a = (r.button_a[0], r.button_a[1])
    single.button_b = (r.button_b[0], r.button_b[1])
    single.price = (r.price[0], r.price[1])

    stepsA = 0
    stepsB = 0
    reached = False
    stepsize = 10000000000
    while(single.price != (0, 0)):
        if stepsA < 0:
            return (-1, -1)
        has_neg = single.price[0] < 0 or single.price[1] < 0
        if (has_neg or reached):
            if has_neg and stepsize != 1:
                move_a_back(single, stepsize)
                stepsA = stepsA - stepsize
                stepsize = int(stepsize / 10)
                continue

            reached = True
            if single.price[1] > 0:
                # This is to low on purpose
                i = 0
                while True:
                    i+=1
                    if i > 210:
                        return (-1,-1)
                    b_moves = floor(single.price[1] / single.button_b[1])
                    if b_moves == 0:
                        b_moves = 1
                    stepsB += b_moves
                    move_b(single, b_moves)
                    
                    move_a_to_pos = ceil(single.price[0]/-single.button_a[0])
                    move_a_back(single, move_a_to_pos)
                    stepsA -= move_a_to_pos
                    if single.price[0] == 0 and single.price[1] == 0:
                        return (stepsA, stepsB)
            else :
                i = 0
                # This is to low on purpose
                while True:
                    i+=1
                    if i > 200:
                        return (-1,-1)
                    b_moves = floor(single.price[0] / single.button_b[0])
                    if b_moves == 0:
                        b_moves = 1
                    stepsB += b_moves
                    move_b(single, b_moves)

                    move_a_to_pos = ceil(single.price[1]/-single.button_a[1])
                    move_a_back(single, move_a_to_pos)
                    stepsA -= move_a_to_pos
                    
                    if single.price[0] == 0 and single.price[1] == 0:
                        return (stepsA, stepsB)



            while(single.price[0] > 0 and single.price[1] > 0):
                move_b(single)
                try_b+=1
                if single.price == (0, 0):
                    return (stepsA, try_b)
            for j in range(try_b):
                move_b_back(single)
            
        else:
            move_a(single, stepsize)
            stepsA+=stepsize
    
    return (stepsA, stepsB)
        


def process_single1(single: SingleInput) -> int:
    a = find_least_move_b(single)
    if a[0] == -1:
        return 0
    
    swapped = SingleInput()
    swapped.button_a = single.button_b
    swapped.button_b = single.button_a
    swapped.price = single.price
    b = find_least_move_b(swapped)
    price_a_1 = a[0] * 3
    price_a_2 = a[1]
    total_a = price_a_1 + price_a_2

    price_b_1 = b[0] 
    price_b_2 = b[1]* 3
    total_b = price_b_1 + price_b_2
    if total_a < total_b:
        return total_a
    return total_b


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
        print(total)
        total+=process_single1(i)
    return total

def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    for i in input.lines:
        total+=process_single2(i)
    return total

if __name__ == '__main__':
    print(solve_total_1())
