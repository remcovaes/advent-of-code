import pytest

from advent.main import parse_input, read_input, solve_part_one, solve_part_two



@pytest.mark.parametrize(
    [ "input_string", "expected" ],
    [
        [ "^v^v^v^v^v", 2 ],
    ]
)
def test_part_one_single(input_string, expected):
    parsed = parse_input(input_string)
    assert solve_part_one(parsed) == expected

def test_part1_total():
    assert solve_part_one(read_input()) == 2592

@pytest.mark.parametrize(
    [ "input_string", "expected" ],
    [
        [ "^v^v^v^v^v", 11 ],
    ]
)
def test_part2(input_string, expected):
    present = parse_input(input_string)
    assert solve_part_two(present) == expected

def test_part2_total():
    assert solve_part_two(read_input()) == 2360
