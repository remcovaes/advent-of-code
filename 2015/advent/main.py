def read_input():
    with open("advent/input", encoding="utf-8") as file:
        return "".join(file.readlines())

def solve_part_one(input_string: str):
    floor = 0
    for letter in input_string:
        if letter == "(":
            floor += 1
        if letter == ")":
            floor -= 1
    return floor

def solve_part_two(input_string: str):
    floor = 0
    i = 0
    for letter in input_string:
        i+=1
        if letter == "(":
            floor += 1
        if letter == ")":
            floor -= 1
        if floor == -1:
            break
    return i

def solve():
    lines = read_input()
    part_a = solve_part_one(lines)
    print("Part 1: ", part_a)

    part_b = solve_part_two(lines)
    print("Part 2: ", part_b)

if __name__ == "__main__":
    solve()
