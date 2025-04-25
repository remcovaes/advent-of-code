from typing import List, Tuple
from functools import cache
from itertools import combinations

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
    f: str
    t: str
    total: tuple[str, str]

class MainInput:
    lines: List[SingleInput]

def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()

    f,t = single.split("-")
    single_input.f = f
    single_input.t = t
    if t < f:
        single_input.total = (t, f)
    else:
        single_input.total = (f, t)


    return single_input


def parse_input(s: str) -> MainInput:
    main = MainInput()
    main.lines = []
    for line in s.split("\n"):
        if line == "":
            continue
        main.lines.append(parse_single(line))
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

def solver_part1(s: str):
    input = parse_input(s)
    groups:set[tuple[str, str, str]] = set()
    connection = set()
    for i in input.lines:
        connection.add(i.total)
    ip_list = input.lines

    for current in ip_list:
        print(current)
        potential = []
        for i in ip_list:
            if current.t == i.t or current.t== i.f:
                potential.append(i)
        for i in potential:
            first = current.f
            second = i.f if i.f != current.t else i.t
            if first == second:
                continue
            if (first,second) in connection or (second, first) in connection:
                groups.add(tuple(sorted([current.t, first, second])))
    
    total = 0
    for i in groups:
        for j in i:
            if j.startswith("t"):
                total+=1
                break    
    return total

failes = set()
@cache
def get_longest_chain(start: str, end: str, current_chain_tup: tuple[tuple[str, str], ...], ip_list: tuple[tuple[str, str]]):
    current_chain = set(current_chain_tup)

    longest_chain = set()
    if (start, end) in failes:
        return []

    next_options = []
    for i in ip_list:
        if i in current_chain:
            continue
           
        if start == i[0] or start == i[1]:
            next_options.append(i)
    for i in next_options:
        if end == i[0] or end == i[1]:
            chain = current_chain.copy()
            chain.add(i)
            if len(chain) > len(longest_chain):
                longest_chain = chain
                continue
        s = i[0] if i[0] != start else i[1]
        current = current_chain.copy()
        count = 0
        for c in current:
            if i[0] == c[0] or i[0] == c[1]:
                count +=1
                continue
        count2 = 0
        for c in current:
            if i[1] == c[0] or i[1] == c[1]:
                count2 +=1
                continue
        if count > 1:
            continue
        if count2 > 1:
            continue
        current.add(i)
        curtup = tuple(current)
        current_longst = get_longest_chain(s, end, curtup, ip_list)
        if len(current_longst) > len(longest_chain):
            longest_chain = current_longst
        else:
            for i in current_longst:
                failes.add(i)
                print(i)
        if len(longest_chain) == 0:
            failes.add((start, end))
            print(0)
    return longest_chain


def all_connectted(c: set[tuple[str, str]], all: set[tuple[str, str]]):
    for i in c:
        con = i[1]
        for j in c:
            to = j[1]
            if con == to:
                continue
            if not ((con, to) in all or (to,con) in all):
                return False
    return True 

def is_connected(c: set[tuple[str, str]], all_points: set[tuple[str,str]]):
    all_others = []
    for i in c:
        all_others.append(i[1])
    combos = list(combinations(all_others, 2))
    for i in combos:
        if not (i in all_points or (i[1], i[0]) in all_points):
            return False
    return True



def solver_part2(s: str):
    input = parse_input(s)

    connection: list[tuple[str,str]] = []
    for i in input.lines:
        connection.append(i.total)
    connection.sort(key=lambda x: x[0])
    current = []
    current_set = set()
    i = 0
    groups: list[list[tuple[str,str]]] = []
    
    all_connections = set(connection)
    group = []
    for i in connection:
        if len(group) == 0:
            group.append(i)
        last = group[-1]
        if last == i:
            continue
        if last[0] == i[0]:
            group.append(i)
        else:
            groups.append(group)
            group = [i]

    for group in groups:
        longest = []
        for i in range(2, len(group) + 1):
            current_group = set()
            perms = list(combinations(group, i))
            for j in perms:
                if is_connected(set(j), all_connections):
                    longest = j
        if len(longest) > len(current):
            current = longest



    sep = set()
    for i in current:
        sep.add(i[0])
        sep.add(i[1])
    sorted_sep = list(sep)
    sorted_sep.sort()
    return ",".join(sorted_sep)









# def solver_part2(s: str):
#     input = parse_input(s)
#     connection = set()
#     for i in input.lines:
#         connection.add(i.total)
#     ip_list = input.lines
#
#     longest_chain = []
#     inp: set[tuple[str,str]] = set()
#     for current in ip_list:
#         start = current.t
#         end = currenf
#         inp.add((start,end))
#     for current in ip_list:
#         start = current.t
#         end = current.f
#         c_chain = get_longest_chain(start, end, ((start, end),), tuple(inp)) 
#         if len(c_chain) > len(longest_chain):
#             longest_chain = c_chain
#     results = set()
#     for i in longest_chain:
#         results.add(i[1])
#         results.add(i[0])
#     endstr = []
#     l = list(results)
#     l.sort()
#     lllist = list(longest_chain)
#     lllist.sort()
#     for i in l:
#         endstr.append(i)
#
#     return ",".join(endstr)

if __name__ == "__main__":
    print(solver_part2(read_file()))

