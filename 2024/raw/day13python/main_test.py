from main import SingleInput, find_least_move_a, solve_total_1, solve_total_2, solver_part1, solver_part2, find_least_move_b

def test_total_1():
    result = solve_total_1()
    assert result == 38714

def test_example_1():
    input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400"""
    result = solver_part1(input)
    assert result == 280

def test_example_1_3():
    input = """Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176"""
    result = solver_part1(input)
    assert result == 0


def test_example_1_1():
    input = """Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176"""
    result = solver_part1(input)
    assert result == 480

def test_example_1_4():
    input = """Button A: X+15, Y+26
Button B: X+39, Y+21
Prize: X=1061, Y=6652"""
    result = solver_part1(input)
    assert result == 0

def test_part2():
    s= SingleInput()
    s.button_a = (15,41)
    s.button_b = (90,53)

    s.price = (3420, 2593)
    assert find_least_move_a(s) == find_least_move_b(s)


def test_total_2():
    result = solve_total_2()
    assert result == 0

def test_example_2():
    input = """
"""
    result = solver_part2(input)
    assert result == 0

