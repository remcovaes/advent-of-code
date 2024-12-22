from main import solve_total_1, solve_total_2, solver_part1, solver_part2, process_single1, parse_input

def test_total_1():
    result = solve_total_1()
    assert result != "172141540"
    assert result == 0

def test_example_1():
    input = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
    target = "117440"
    result = solver_part1(input, target)
    assert result == "".join("4,6,3,5,6,3,5,2,1,0".split(","))

def test_example222_1():
    input = """Register A: 0
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
    result = solver_part1(input, "117440")
    assert result == "".join("4,6,3,5,6,3,5,2,1,0".split(","))


def test_example21():
    input = """Register A: 0
Register B: 0
Register C: 9

Program: 2,6"""
    input = parse_input(input)
    process_single1(input)
    assert input.b == 1

def test_example31():
    input = """Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4"""
    input = parse_input(input)
    process_single1(input)
    assert input.output == "012"

def test_example41():
    input = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
    input = parse_input(input)
    process_single1(input)
    assert input.output == "".join("4,2,5,6,7,7,7,7,3,1,0".split(","))
    assert input.a == 0

def test_example51():
    input = """Register A: 0
Register B: 29
Register C: 0

Program: 1,7"""
    input = parse_input(input)
    process_single1(input)
    assert input.b == 26

def test_example61():
    input = """Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0"""
    input = parse_input(input)
    process_single1(input)
    assert input.b == 44354

def test_example62():
    input = """Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0"""
    input = parse_input(input)
    process_single1(input)
    assert input.b == 44354


def test_total_2222():
    result = solve_total_2()
    assert result == 0

# def test_example_2():
#     input = """
# """
#     result = solver_part2(input)
#     assert result == 0

