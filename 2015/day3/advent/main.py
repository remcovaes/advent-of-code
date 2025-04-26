from dataclasses import dataclass
from typing import Literal

@dataclass
class FullInput:
    single: list[Literal["<", ">", "^", "v"]]

@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

def parse_input(string: str) -> FullInput:
    full = FullInput(single=[])
    for chat in string:
        match chat:
            case str(a):
                full.single.append(a)
    return full

def read_input() -> FullInput:
    with open("advent/input", encoding="utf-8") as file:
        return parse_input("".join(file.readlines()))


def solve_part_one(full_input: FullInput):
    visited = set()
    current = Coordinate(x=0,y=0)
    visited.add(current)
    for i in full_input.single:
        match i:
            case "<":
                current = Coordinate(current.x -1, current.y)
            case ">":
                current = Coordinate(current.x +1, current.y)
            case "v":
                current = Coordinate(current.x, current.y -1)
            case "^":
                current = Coordinate(current.x, current.y +1)
        visited.add(current)

    return len(visited)

def solve_part_two(full_input: FullInput):
    visited = set()
    current_santa = Coordinate(x=0,y=0)
    current_robot = Coordinate(x=0,y=0)

    visited.add(current_santa)
    turn_santa = True
    for i in full_input.single:
        current = current_santa if turn_santa else current_robot
        match i:
            case "<":
                current= Coordinate(current.x -1, current.y)
            case ">":
                current= Coordinate(current.x +1, current.y)
            case "v":
                current= Coordinate(current.x, current.y -1)
            case "^":
                current= Coordinate(current.x, current.y +1)
        visited.add(current)
        if turn_santa:
            current_santa = current
        else:
            current_robot = current
        turn_santa = not turn_santa

    return len(visited)
def solve():
    lines = read_input()
    part_a = solve_part_one(lines)
    print("Part 1: ", part_a)

    part_b = solve_part_two(lines)
    print("Part 2: ", part_b)

if __name__ == "__main__":
    solve()
