from dataclasses import dataclass
from typing import Literal

@dataclass(eq=True, frozen=True)
class Coordinate:
    x: int
    y: int

@dataclass
class Instruction:
    action: Literal["on", "off", "toggle"]
    start: Coordinate  
    end: Coordinate  

@dataclass
class FullInput:
    instructions: list[Instruction]
    grid: dict[Coordinate, bool]
    
def string_to_coor(string: str) -> Coordinate:
    [s,e] = string.split(",")
    return Coordinate(x=int(s), y=int(e))
  
def parse_line(string: str) -> Instruction:
    [firstPart, endPart] = string.split(" through ")
    if firstPart.startswith("turn on"):
        start_string = firstPart.strip("turn on ")
        start_coor = string_to_coor(start_string)
        end_coor = string_to_coor(endPart)
        return Instruction(action="on", start=start_coor, end=end_coor)

    if firstPart.startswith("turn off"):
        start_string = firstPart.strip("turn off ")
        start_coor = string_to_coor(start_string)
        end_coor = string_to_coor(endPart)
        return Instruction(action="off", start=start_coor, end=end_coor)

    if firstPart.startswith("toggle"):
        start_string = firstPart.strip("toggle ")
        start_coor = string_to_coor(start_string)
        end_coor = string_to_coor(endPart)
        return Instruction(action="toggle", start=start_coor, end=end_coor)
    raise RuntimeError("could not parse")

def parse_input_full(string: str) -> FullInput:
    full = FullInput(instructions=[], grid={})
    for line in string.split("\n"):
        if line == "":
            continue
        full.instructions.append(parse_line(line))
    return full

def read_input() -> FullInput:
    with open("advent/input", encoding="utf-8") as file:
        return parse_input_full(file.read())


def solve_part_one(full_input: FullInput):
    total = 0
    for i in full_input.instructions:
        x_range = range(i.start.x, i.end.x + 1)
        y_range = range(i.start.y, i.end.y + 1)
        for x in x_range:
            for y in y_range:
                if i.action == "on":
                    full_input.grid[Coordinate(x=x, y=y)] = True

                if i.action == "off":
                    full_input.grid[Coordinate(x=x, y=y)] = False
                if i.action == "toggle":
                    prev = full_input.grid.get(Coordinate(x=x, y=y))
                    full_input.grid[Coordinate(x=x, y=y)] = not prev if prev is not None else True
    for light in full_input.grid.values():
        if light:
            total += 1
    return total

def solve_part_two(full_input: FullInput):
    total = 0
    brightness_grid: dict[Coordinate, int] = {}
    for i in range(1000):
        for j in range(1000):
            brightness_grid[Coordinate(x=i, y=j)] = 0
        

    for i in full_input.instructions:
        x_range = range(i.start.x, i.end.x + 1)
        y_range = range(i.start.y, i.end.y + 1)
        for x in x_range:
            for y in y_range:
                if i.action == "on":
                    brightness_grid[Coordinate(x=x, y=y)] += 1
                if i.action == "off":
                    if brightness_grid[Coordinate(x=x, y=y)] > 0:
                        brightness_grid[Coordinate(x=x, y=y)] -= 1
                if i.action == "toggle":
                    brightness_grid[Coordinate(x=x, y=y)] += 2
    for light in brightness_grid.values():
        total += light
    return total

def solve():
    lines = read_input()
    part_a = solve_part_one(lines)
    print("Part 1: ", part_a)

    part_b = solve_part_two(lines)
    print("Part 2: ", part_b)

if __name__ == "__main__":
    solve()
