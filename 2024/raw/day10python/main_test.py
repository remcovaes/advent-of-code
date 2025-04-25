from main import solve_total_1


def test_total_1():
    result = solve_total_1()
    assert result == 501


def test_example_1():
    input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    result = solver_part(input)
    assert result == 36


def test_example_2():
    input = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""
    result = solver_part1(input)
    assert result == 2


def test_example_3():
    input = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""
    result = solver_part1(input)
    assert result == 4


def test_example_4():
    input = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""
    result = solver_part1(input)
    assert result == 2


def test_total_2():
    result = solve_total_2()
    assert result == 0


def test_example_B2():
    input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    result = solver_part2(input)
    assert result == 81


def test_example_B3():
    input = """
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
"""
    result = solver_part2(input)
    assert result == 13
