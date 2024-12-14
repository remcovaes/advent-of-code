from main import solve_total_1, solve_total_2, solver_part1, solver_part2

def test_total_1():
    result = solve_total_1()
    assert result == 0

def test_example_1():
    input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
    result = solver_part1(input)
    assert result == 0

def test_example2_1():
    input = """p=2,4 v=2,-3"""
    result = solver_part1(input)
    assert result == 0


def test_total_2():
    result = solve_total_2()
    assert result == 0

def test_example_2():
    input = """
"""
    result = solver_part2(input)
    assert result == 0

