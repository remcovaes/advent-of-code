from dataclasses import dataclass

@dataclass
class SingleInput:
    raw: str

@dataclass
class FullInput:
    single: list[SingleInput]

def parse_line(string: str) -> SingleInput:
    return SingleInput(raw=string)


def read_input() -> FullInput:
    full = FullInput(single=[])
    with open("advent/input", encoding="utf-8") as file:
        for line in file.readlines():
            full.single.append(parse_line(line))
    return full


def solve_part_one(full_input: FullInput):
    total = 0
    for i in full_input.single:
        total += solve_part_one_single(i)
    return total

def solve_part_one_single(single: SingleInput):
    total = len(single.raw)
    return total

def solve_part_two(full_input: FullInput):
    total = 0
    for i in full_input.single:
        total += solve_part_two_single(i)
    return total

def solve_part_two_single(single: SingleInput):
    total = len(single.raw)
    return total

def solve():
    lines = read_input()
    part_a = solve_part_one(lines)
    print("Part 1: ", part_a)

    part_b = solve_part_two(lines)
    print("Part 2: ", part_b)

if __name__ == "__main__":
    solve()
