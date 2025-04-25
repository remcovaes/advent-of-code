from typing import List, Tuple

Coor = Tuple[int, int]
CoorWithScore = Tuple[int, int, int]

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
    unsafe: set[Coor]
    current: set[Coor]
    falling: List[Coor]


def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()

    single_input.single = single

    return single_input


def parse_input(s: str, start: int) -> MainInput:
    main = MainInput()
    main.unsafe = set()
    main.current = set()
    main.current.add((0, 0))
    main.falling = []
    splitted = s.split("\n")
    i = 0
    for line in splitted:
        if line == '':
            continue
        a, b = line.split(",")
        if i < start:
            main.unsafe.add(( int(a), int(b)))
            i +=1
        else:
            main.falling.append(( int(a), int(b)))
    return main

def process_single1(single: SingleInput) -> int:
    total = 0
    return total


def process_single2(single: SingleInput) -> int:
    total = 0
    return total

def get_pos_from_score(c: CoorWithScore):
    return (c[0], c[1])
    


def solve_total_1(dim: int, start: int):
    file = read_file()
    return solver_part1(file, dim, start)

def solve_total_2():
    file = read_file()
    return solver_part2(file)

def solver_part1(s: str, dim: int, start: int):
    input = parse_input(s, start)
    i = 0
    stops = []
    for fall in input.falling:
        print(i)
        i +=1
        copyInput = MainInput()
        copyInput.current = set()
        copyInput.current.add((0,0))
        copyInput.unsafe = input.unsafe.copy()
        for l in range(i):
            copyInput.unsafe.add(input.falling[l])
        e = can_exit(dim, copyInput)
        if not e:
            print(fall)
            return fall

def can_exit(dim: int, input: MainInput):
    change = True
    while change:
        change = False
        to_add = []
        for m in input.current:
            l = left(m)
            r = right(m)
            d = down(m)
            u = up(m)
            for i in [l,r,d,u]:
                if i[0] > dim:
                    continue
                if i[1] > dim:
                    continue
                if i[0] < 0:
                    continue
                if i[1] < 0:
                    continue
                if i in input.unsafe:
                    continue
                if i in input.current:
                    continue
                to_add.append(i)
        for i in to_add:
            change = True
            input.current.add(i)
    return (dim, dim) in input.current



def solver_part2(s: str):
    input = parse_input(s)
    total = 0
    return total
if __name__ == "__main__":
    print(solve_total_1(70, 1024))
