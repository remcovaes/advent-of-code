import hashlib

def read_input() -> str:
    with open("advent/input", encoding="utf-8") as file:
        return file.read()

def solve_part_one(full_input: str):
    total = 0
    while True:
        total += 1
        hash_str = hashlib.md5(str.encode(full_input + str(total))).hexdigest()
        if hash_str[:5] == "00000":
            return total


def solve_part_two(full_input: str):
    total = 0
    while True:
        total += 1
        hash_str = hashlib.md5(str.encode(full_input + str(total))).hexdigest()
        if hash_str[:6] == "000000":
            return total

def solve():
    lines = read_input()
    part_a = solve_part_one(lines)
    print("Part 1: ", part_a)

    part_b = solve_part_two(lines)
    print("Part 2: ", part_b)

if __name__ == "__main__":
    solve()
