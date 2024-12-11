from main import solve_total_1, solve_total_2, solver_part1, solver_part2

def test_total_1():
    result = solve_total_1()
    assert result == 0

def test_example_1():
    input = """125 17"""
    result = solver_part1(input)
    assert result == 55312

def test_total_2():
    result = solve_total_2()
    assert result == 0

def test_example_2():
    input = """125 17"""
    result = solver_part2(input)
    assert result == 0

