from dataclasses import dataclass
from enum import Enum
from functools import cache

class Operation(Enum):
    AND = 1
    LSHIFT = 2
    NOT = 3
    OR = 4
    RSHIFT = 5
    NOOP = 6


@dataclass
class SingleInput:
    a: int | str
    b: int | str | None
    operation: Operation
    result: str

@dataclass
class FullInput:
    single: dict[str, SingleInput]
    
def parse_int_or_string(i:  str):
    if i.isdigit():
        return int(i)
    return i

def parse_line(string: str) -> SingleInput:
    [ operation, result ] = string.split(" -> ")
    if "AND" in operation:
        [a, b] = operation.split(" AND ")
        return SingleInput(
            a=parse_int_or_string(a),
            b=parse_int_or_string(b),
            result=result,
            operation=Operation.AND,
        )
    if "LSHIFT" in operation:
        [a, b] = operation.split(" LSHIFT ")
        return SingleInput(
            a=parse_int_or_string(a),
            b=parse_int_or_string(b),
            result=result,
            operation=Operation.LSHIFT,
        )
    if "RSHIFT" in operation:
        [a, b] = operation.split(" RSHIFT ")
        return SingleInput(
            a=parse_int_or_string(a),
            b=parse_int_or_string(b),
            result=result,
            operation=Operation.RSHIFT,
        )
    if "OR" in operation:
        [a, b] = operation.split(" OR ")
        return SingleInput(
            a=parse_int_or_string(a),
            b=parse_int_or_string(b),
            result=result,
            operation=Operation.OR,
        )
    if "NOT" in operation:
        a = operation.lstrip("NOT ")
        return SingleInput(
            a=parse_int_or_string(a),
            b=None,
            result=result,
            operation=Operation.NOT,
        )

    return SingleInput(
        a=parse_int_or_string(operation),
        b=None,
        result=result,
        operation=Operation.NOOP,
    )


def handle_num_ops(full_input: FullInput, outcome: str) -> int:
    @cache
    def get_single(outcome:str):
        single_input = full_input.single[outcome]

        int_a = single_input.a if isinstance(single_input.a, int) else get_single(single_input.a)
        int_b = single_input.b if isinstance(single_input.b, int) or single_input.b is None else get_single(single_input.b)

        match single_input.operation:
            case Operation.NOOP:
                return int_a
            case Operation.NOT:
                return ~int_a
            case Operation.AND:
                if int_b is None:
                    raise ValueError("should not happen")

                return int_a & int_b
            case Operation.LSHIFT:
                if int_b is None:
                    raise ValueError("should not happen")

                return int_a << int_b

            case Operation.RSHIFT:
                if int_b is None:
                    raise ValueError("should not happen")

                return int_a >> int_b

            case Operation.OR:
                if int_b is None:
                    raise ValueError("should not happen")

                return int_a | int_b
    return get_single(outcome)


def parse_input_full(string: str) -> FullInput:
    full = FullInput(single={})
    for line in string.split("\n"):
        if line == "":
            continue
        if "->" not in line:
            continue
        parsed_line = parse_line(line)
        full.single[parsed_line.result] = parsed_line
    return full

def read_input() -> FullInput:
    with open("advent/input", encoding="utf-8") as file:
        return parse_input_full(file.read())


def solve_part_one(full_input: FullInput):
    return handle_num_ops(full_input, "a")


def solve_part_two(full_input: FullInput):
    full_input.single["b"] = SingleInput(a=3176, result="b", operation=Operation.NOOP, b=None)
    return handle_num_ops(full_input, "a")

def solve_part_two_single(single: SingleInput):
    total = 0
    return total

def solve():
    lines = read_input()
    part_a = solve_part_one(lines)
    print("Part 1: ", part_a)

    part_b = solve_part_two(lines)
    print("Part 2: ", part_b)

if __name__ == "__main__":
    solve()
