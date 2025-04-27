from dataclasses import dataclass
from itertools import batched, pairwise

@dataclass
class SingleInput:
    raw: str

@dataclass
class FullInput:
    single: list[SingleInput]

def parse_line(string: str) -> SingleInput:
    return SingleInput(raw=string)

def parse_input_full(string: str) -> FullInput:
    full = FullInput(single=[])
    for line in string.split("\n"):
        full.single.append(parse_line(line))
    return full

def read_input() -> FullInput:
    with open("advent/input", encoding="utf-8") as file:
        return parse_input_full(file.read())


def solve_part_one(full_input: FullInput):
    total = 0
    for i in full_input.single:
        total += solve_part_one_single(i)
    return total

def solve_part_one_single(single: SingleInput):
    if "ab" in single.raw:
        return 0
    if "cd" in single.raw:
        return 0
    if "pq" in single.raw:
        return 0
    if "xy" in single.raw:
        return 0
    no_double = True
    for batch in pairwise(single.raw):
        if batch[0] == batch[1]:
            no_double = False
            break
    if no_double:
        return 0

    count_vowels = 0
    for letter in single.raw:
        if letter in "aeiou":
            count_vowels +=1
    
    if count_vowels < 3:
        return 0

    return 1

def solve_part_two(full_input: FullInput):
    total = 0
    for i in full_input.single:
        total += solve_part_two_single(i)
    return total

def solve_part_two_single(single: SingleInput):
    for i, letter in enumerate(single.raw):
        if (i + 2) >= len(single.raw):
            return 0
        if letter == single.raw[i+2]:
            break


    found = set()
    previous = None
    for batch in pairwise(iter(single.raw)):
        if len(batch) != 2:
            continue
        if previous == batch:
            previous = None
            continue
        if batch in found:
            return 1
        found.add(batch)
        previous = batch
    return 0








def solve():
    lines = read_input()
    part_a = solve_part_one(lines)
    print("Part 1: ", part_a)

    part_b = solve_part_two(lines)
    print("Part 2: ", part_b)

if __name__ == "__main__":
    solve()
