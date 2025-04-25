from main import solve_total_1, solve_total_2, solver_part1

def test_total_1():
    result = solve_total_1()
    assert result > 492991
    assert result != 1743300
    assert result != 538305
    assert result < 1907164
    assert result != 1743693
    assert result != 538388
    assert result != 787332
    assert result != 890292
    assert result != 690418
    assert result == 0

def test_example_1111():
    input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
    result = solver_part1(input, 2, 2)
    assert result == 285


def test_example_1():
    input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
    result = solver_part1(input, 50, 20)
    assert result == 286

def test_total_2():
    result = solve_total_2()
    assert result == 0

def test_example_2():
    input = """
"""
    result = solver_part2(input)
    assert result == 0

