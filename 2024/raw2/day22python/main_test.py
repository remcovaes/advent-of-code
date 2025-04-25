from main import solve_total_1, solve_total_2, solver_part1, solver_part2

def test_total_1():
    result = solve_total_1()
    assert result == 0

def test_example_1():
    input = """1
2
3
2024"""
    result = solver_part1(input)
    assert result == 23

def test_example_12():
    input = """123"""
    result = solver_part1(input)
    assert result == 1


def test_total_2():
    result = solve_total_2()
    assert result == 0

def test_example_2():
    input = """
"""
    result = solver_part2(input)
    assert result == 0

