from main import solve_total_1, solve_total_2, solver_part1, solver_part2

def test_total_1():
    result = solve_total_1(70, 1024)
    assert result == 0

def test_example_11():
    input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
5,1
5,1
5,1
5,1
5,1
0,8
8,0"""
    result = solver_part1(input, 6, 12)
    assert result == (6, 1)


def test_example_1():
    input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
0,1
1,0"""
    result = solver_part1(input, 6, 12)
    assert result == (6, 1)

def test_total_2():
    result = solve_total_2()
    assert result == 0

def test_example_2():
    input = """
"""
    result = solver_part2(input)
    assert result == 0

