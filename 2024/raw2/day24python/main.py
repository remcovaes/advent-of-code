from os import copy_file_range
from random import Random 
from typing import List, Tuple
from functools import cache
from itertools import combinations, permutations

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
    left: str
    right: str
    operation: str
    result_field: str
    result: int

class MainInput:
    data: dict[str, int]
    ops: List[SingleInput] 


def parse_single(single: str) -> SingleInput:
    single_input = SingleInput()

    left, op, right, arrow, result = single.split(" ")

    single_input.left = left
    single_input.operation = op
    single_input.right = right
    single_input.result_field = result
    return single_input


def parse_input(s: str) -> MainInput:
    main = MainInput()
    main.ops = []
    main.data = {}
    start, ops = s.split("\n\n")
    for line in start.split("\n"):
        key, value = line.split(": ")
        main.data[key] = int(value)
    for line in ops.split("\n"):
        if line == "":
            continue
        main.ops.append(parse_single(line))
    return main

def process_single2(single: SingleInput) -> int:
    total = 0
    return total

def solve_total_1():
    file = read_file()
    return solver_part1(file)

def solve_total_2():
    file = read_file()
    return solver_part2(file, 4)

def get_wrong_output(input: MainInput):
    z_results = get_wrong_result_for(input, "z")
    x_results = get_wrong_result_for(input, "x")
    y_results = get_wrong_result_for(input, "y")
    wrongs = []
    x_results.reverse()
    y_results.reverse()
    z_results.reverse()
    x_bits = "".join([str(x[1]) for x in x_results])
    y_bits = "".join([str(x[1]) for x in y_results])
    z_bits = "".join([str(x[1]) for x in z_results])

    desired_length = max(len(x_bits), len(y_bits), len(z_bits))

    and_result = int(x_bits, 2) + int(y_bits, 2)
    z_value = int(z_bits, 2)

    and_result_padded = f"{and_result:0{desired_length}b}"
    z_value_padded = f"{z_value:0{desired_length}b}"
    print(and_result_padded)
    print(z_value_padded)
    x_results.reverse()
    y_results.reverse()
    z_results.reverse()
    reversed_and = and_result_padded[::-1]
    reversed_z = z_value_padded[::-1]
    for j in range(len(reversed_and) -1 ):
        res = reversed_and[j]
        z = reversed_z[j]
        if res != z:
            try:
                w = (x_results[j], y_results[j], z_results[j])
                wrongs.append(w)
            except IndexError:
                wrongs.append(())
    return wrongs

def complete_data(input: MainInput):
    i = 0
    has_edited = True
    while True:
        if i >= len(input.ops):
            i = 0
            if not has_edited:
                break
            has_edited = False
            continue
        first = input.ops[i]
        i+=1
        if not (first.right in input.data and first.left in input.data):
            continue
        if first.result_field in input.data:
            continue
        has_edited = True
        left_num = input.data[first.left]
        right_num = input.data[first.right]
        if first.operation == "AND":
            data = left_num & right_num
            input.data[first.result_field] = data

        if first.operation == "XOR":
            data = left_num ^ right_num
            input.data[first.result_field] = data

        if first.operation == "OR":
            data = left_num | right_num
            input.data[first.result_field] = data
    return input
def get_results(input: MainInput):
    z_results = get_result_for(input, "z")
    x_results = get_result_for(input, "x")
    y_results = get_result_for(input, "y")
    return z_results, x_results, y_results

def solver_part1(s: str):
    input = parse_input(s)
    z_results = get_results(input)

    return z_results

def get_wrong_result_for(input: MainInput, s: str):
    z_results = []
    for i, num in input.data.items():
        if i.startswith(s):
            z_results.append((i, num))

    z_results.sort(key=lambda x: x[0])
    return z_results

def get_result_for(input: MainInput, s: str):
    z_results = []
    for i, num in input.data.items():
        if i.startswith(s):
            z_results.append((i, num))

    z_results.sort(key=lambda x: x[0])
    z_results.reverse()
    end_str = ""
    for i in z_results:
        end_str += str(i[1])
    return int(end_str, 2)

def find_affected_ops(input: MainInput, op: list[str], all: set[int]):
    new_aff = set()
    for a in op:
        for i in input.ops:
            if i.right == a or i.left == a or i.result_field == a:
                new_aff.add(i)

    return new_aff

def solver_part2(s: str, count: int):
    orig = parse_input(s)

    swaps = [ 
        # (19,71),
        # (70, 128),
        # (55,6),
        # (31, 82)
    ]
        # (31, 128)
    swapped = []
    for x1, x2 in swaps:
        j = (x1, x2)
        input = orig

        first = input.ops[j[0]].result_field
        second = input.ops[j[1]].result_field
        swapped.append(first)
        swapped.append(second)
        input.ops[j[0]].result_field = second
        input.ops[j[1]].result_field = first
    # for i in range(44):
    #     # random bit
    #     orig.data["x" + str(i).zfill(2)] = Random().randint(0,1)
    #     orig.data["y" + str(i).zfill(2)] = Random().randint(0,1)
        
    orig = complete_data(orig)
    vals = get_wrong_output(orig)
    swapped.sort()
    res = ",".join(swapped)
    for i in vals:
        print(i)
    z_results, x_results, y_results = get_results(orig)
    checksum = x_results & y_results
    print(len(vals))
    if z_results == checksum:
        print("wint")
    result = []
    for i in swaps:
        for j in i:
            result.append(orig.ops[j].result_field)

            print(orig.ops[j].left, orig.ops[j].right)
    result.sort()
    # return ",".join(result)
    wires_to_swap = []
    for i in range(0, len(orig.ops)):
        # 31 must be swapped in my input
        if i == 19:
            continue
        wires_to_swap.append((19,i))
    
    best_swap = []
    highest = 0
    result = swap_spot(wires_to_swap, s, orig, 6)
    
    passed = set()
    for i in diffs:
        for j in range(100):
            input = parse_input(s)
            for x in range(0, len(i), 2):
                j = (i[x], i[x+1])

                first = input.ops[j[0]].result_field
                second = input.ops[j[1]].result_field
                input.ops[j[0]].result_field = second
                input.ops[j[1]].result_field = first
            for k in range(44):
                # random bit
                input.data["x" + str(k).zfill(2)] = Random().randint(0,1)
                input.data["y" + str(k).zfill(2)] = Random().randint(0,1)
            com = complete_data(input)
            z_results, x_results, y_results = get_results(com)
            if x_results + y_results == z_results:
                continue
            else:
                passed.add(i)
                break

    for i in diffs:
        if i not in passed:
            for q in i:
                swapped.append(orig.ops[q].result_field)
            swapped.sort()
            finish = ",".join(swapped)
            print(finish)

    return result
diffs = set()
def swap_spot(wires_to_swap, s: str, orig: MainInput, goal: int):
    best_swap = []
    highest = 0
    for i in wires_to_swap:
        
        input = parse_input(s)
        for x in range(0, len(i), 2):
            j = (i[x], i[x+1])

            first = input.ops[j[0]].result_field
            second = input.ops[j[1]].result_field
            input.ops[j[0]].result_field = second
            input.ops[j[1]].result_field = first

        input = complete_data(input)
        z_results, x_results, y_results = get_results(input)

        new_wrongs = get_wrong_output(input)
        q = len(new_wrongs)
        if q <= goal and len(i) < 8:
            print("goal", goal)
            print("current", q)
            print("ilen", len(i))
            print("wrong", new_wrongs)
            print("swaps", i)
            options = list(range(len(input.ops)))
            for j in i:
                if j in options:
                    options.remove(j)
            combos = []
            if len(i) <8:
                for j in range(0, len(orig.ops)):
                    num = 0
                    if len(i) == 2:
                        num = 70
                    if len(i) == 4:
                        num = 55
                    if len(i) == 6:
                        num = 31
                    if j == num:
                        continue
                    combos.append((*i, num, j))
                iterator = combos 
            else: 
                combos = combinations(options, 2)
                iterator = ((*i, *x) for x in combos)
            minone = goal - 2
            res = swap_spot(iterator, s, orig, minone)
        if len(i) == 8:
            checksum = x_results + y_results
            if checksum == z_results:
                swapped = []
                for q in i:
                    swapped.append(orig.ops[q].result_field)
                swapped.sort()
                finish = ",".join(swapped)
                diffs.add(i)
                print(finish)
                print(finish)
                print(finish)
                print(finish)
                print(finish)
                print(finish)
    return ""

if __name__ == "__main__":
    print(solve_total_2())
