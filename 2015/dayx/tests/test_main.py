import pytest

from advent.main import parse_line, read_input, solve_part_one, solve_part_one_single, solve_part_two, solve_part_two_single


@pytest.mark.parametrize(
    [ "input_string", "expected" ],
    [
        [ "abc", 3 ],
    ]
)
def test_part_one_single(input_string, expected):
    present = parse_line(input_string)
    assert solve_part_one_single(present) == expected

def test_part1_total():
    assert solve_part_one(read_input()) == 0

@pytest.mark.parametrize(
    [ "input_string", "expected" ],
    [
        [ "abc", 3 ],
    ]
)
def test_part2(input_string, expected):
    present = parse_line(input_string)
    assert solve_part_two_single(present) == expected

def test_part2_total():
    assert solve_part_two(read_input()) == 0
