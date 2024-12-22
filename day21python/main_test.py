from main import solve_total_1, solve_total_2, solver_part1, solver_part2, Coor, expand_once

def test_total_1():
    result = solve_total_1()
    assert result < 1923319447377845
    assert result != 299477992525726
    assert result != 751150578280014
    assert result != 127223151517798
    assert result != 307387965392383
    assert result != 124727638943851
    assert result == 0

def test_example_12():
    input = """029A
980A
179A
456A
379A"""
    result = solver_part1(input)
    assert result == 0

def test_example_1():
    input = """480A
143A
983A
382A
974A"""
    result = solver_part1(input)
    assert result == 0

def test_example_1222():
    input = """456A"""
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

def test_expand_once2aasf():
    result = expand_once("A", "<", 1)
    assert result == 4
    result = expand_once("<", "A", 1)
    assert result == 4

#
# def test_expand_onc2e():
#     result = expand_once_keys("A", "<", 2)
#     assert result == ["v","<" ,"<" ,"A" ]
#
#
#
# def test_expand_once():
#     result = expand_once_keys("A", "<", 1)
#     assert result == ["v","<" ,"<" ,"A" ]
#
# def test_expand_twice():
#     result = expand_once("A", "<", 1)
#     assert len(result) == 4
#     result = expand_once("A", "<", 2)
#     assert len(result) == 10
#     result = expand_once("A", "<", 3)
#     assert len(result) == 28
#     result = expand_once("A", "<", 4)
#     assert len(result) == 69
#     result = expand_once("A", "<", 5)
#     assert len(result) == 170
#
#
# def test_expand_twice():
#     result = expand_once("A", "<", 2)
#     assert result == 8
#     result = expand_once("A", "^", 3)
#     assert result == 19
#     result = expand_once("A", "^", 4)
#     assert result == 49
#     result = expand_once("A", "^", 5)
#     assert result == 122
#

