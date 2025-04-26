from dataclasses import dataclass


@dataclass
class Present:
    l: int
    w: int
    h: int

def parse_present(string: str) -> Present:
    match string.split("x"):
        case [l, w, h]:
            return Present(l=int(l), w=int(w), h=int(h))
        case _:
            raise RuntimeError("not handled")

def read_input() -> list[Present]:
    presents: list[Present] = []
    with open("advent/input", encoding="utf-8") as file:
        for line in file.readlines():
            presents.append(parse_present(line))
    return presents


def solve_part_one(presents: list[Present]):
    total = 0
    for i in presents:
        total += solve_part_one_single(i)
    return total

def solve_part_one_single(present: Present):
    side_a = present.l * present.w
    side_b = present.w * present.h
    side_c = present.h * present.l
    surface = 2 * side_a + 2 * side_b + 2 * side_c
    smallest = min(side_a, side_b, side_c)
    return surface + smallest

def solve_part_two(presents: list[Present]):
    total = 0
    for i in presents:
        total += solve_part_two_single(i)
    return total

def solve_part_two_single(present: Present):
    wrap_length_a = present.l + present.l + present.w + present.w
    wrap_length_b = present.l + present.l + present.h + present.h
    wrap_length_c = present.h + present.h + present.w + present.w
    wrap_length = min(wrap_length_a, wrap_length_b, wrap_length_c)
    bow_length = present.l * present.w * present.h
    return wrap_length + bow_length



def solve():
    lines = read_input()
    part_a = solve_part_one(lines)
    print("Part 1: ", part_a)

    part_b = solve_part_two(lines)
    print("Part 2: ", part_b)

if __name__ == "__main__":
    solve()
