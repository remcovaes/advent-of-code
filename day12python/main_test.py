from main import solve_total_1, solve_total_2, solver_part1, solver_part2

def test_total_1():
    result = solve_total_1()
    assert result != 1329974
    assert result == 0

def test_example_1():
    input = """AAAA
BBCD
BBCC
EEEC"""
    result = solver_part1(input)
    assert result == 140

def test_example3_1():
    input = """AAAA
ABAB
ABBB"""
    result = solver_part1(input)
    assert result == 140


def test_example2_1():
    input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
    result = solver_part1(input)
    assert result == 1930


def test_total_2():
    result = solve_total_2()
    assert result == 0

def test_example_2():
    input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
    result = solver_part2(input)
    assert result == 368
 
